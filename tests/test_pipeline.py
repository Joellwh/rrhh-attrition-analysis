"""
Tests del pipeline de datos y del build del dashboard.

Para qué sirven: el riesgo real de este proyecto no es que explote, es que
produzca silenciosamente un dashboard con números equivocados o vacío y lo
publique igual. Cada assert de acá fija un número verificado contra los datos
reales, así que si algo aguas arriba cambia el resultado, el CI lo frena antes
de desplegar.

Los valores esperados salieron de correr el pipeline sobre el dataset
versionado en data/raw/ y contrastar contra las consultas de sql/queries.sql.
"""

import hashlib
import json

import pandas as pd
import pytest

import build_dashboard
import paths

# --- valores de referencia, verificados contra los datos ---
FILAS = 1470
COLUMNAS = 32
BAJAS = 237
TASA_GENERAL = 16.12

ROL_PEOR = "Sales Representative"
ROL_PEOR_TASA = 39.76

DEPTO_PEOR = "Sales"
DEPTO_PEOR_TASA = 20.63

TASA_CON_HORAS_EXTRA = 30.53

# Columnas constantes que data_preparation.py tiene que eliminar.
CONSTANTES_ELIMINADAS = ["EmployeeCount", "Over18", "StandardHours"]


@pytest.fixture(scope="module")
def df():
    """Los datos limpios. Si faltan, el mensaje dice qué correr."""
    return pd.read_csv(paths.require(paths.PROCESSED_CSV))


# ============ datos crudos ============

def test_csv_crudo_versionado_e_intacto():
    """El CSV viene con el repo y es exactamente el que esperamos."""
    ruta = paths.require(paths.RAW_CSV)
    digest = hashlib.sha256(ruta.read_bytes()).hexdigest()
    assert digest == paths.RAW_CSV_SHA256, (
        "El CSV crudo cambió. Si el cambio es intencional, actualizá "
        "RAW_CSV_SHA256 en src/paths.py."
    )


# ============ datos limpios ============

def test_forma_del_dataset(df):
    assert len(df) == FILAS
    assert df.shape[1] == COLUMNAS


def test_se_eliminaron_las_columnas_constantes(df):
    presentes = [c for c in CONSTANTES_ELIMINADAS if c in df.columns]
    assert presentes == [], f"data_preparation.py dejó pasar constantes: {presentes}"


def test_no_quedan_columnas_de_varianza_cero(df):
    """Una columna con un solo valor no puede explicar nada y ensucia el análisis."""
    sin_varianza = [c for c in df.columns if df[c].nunique() == 1]
    assert sin_varianza == [], f"Columnas sin variación: {sin_varianza}"


def test_attrition_quedo_codificada_como_entero(df):
    """El .map() a 0/1 tiene que sobrevivir al ida y vuelta por CSV."""
    assert set(df["Attrition"].unique()) == {0, 1}
    assert pd.api.types.is_integer_dtype(df["Attrition"])


def test_sin_nulos(df):
    con_nulos = df.columns[df.isna().any()].tolist()
    assert con_nulos == [], f"Columnas con nulos: {con_nulos}"


# ============ los numeros del negocio ============

def test_rotacion_general(df):
    assert int(df["Attrition"].sum()) == BAJAS
    assert df["Attrition"].mean() * 100 == pytest.approx(TASA_GENERAL, abs=0.01)


def test_rol_con_mas_rotacion(df):
    tasas = df.groupby("JobRole")["Attrition"].mean() * 100
    peor = tasas.idxmax()
    assert peor == ROL_PEOR
    assert tasas[peor] == pytest.approx(ROL_PEOR_TASA, abs=0.01)


def test_departamento_con_mas_rotacion(df):
    tasas = df.groupby("Department")["Attrition"].mean() * 100
    peor = tasas.idxmax()
    assert peor == DEPTO_PEOR
    assert tasas[peor] == pytest.approx(DEPTO_PEOR_TASA, abs=0.01)


def test_horas_extra(df):
    tasas = df.groupby("OverTime")["Attrition"].mean() * 100
    assert tasas["Yes"] == pytest.approx(TASA_CON_HORAS_EXTRA, abs=0.01)
    # La brecha es el hallazgo central del análisis: si se achica, algo cambió.
    assert tasas["Yes"] > tasas["No"] * 2


# ============ build del dashboard ============

def test_el_blob_tiene_una_fila_por_empleado(df):
    blob = json.loads(build_dashboard.construir_blob(df))
    assert len(blob["rows"]) == FILAS
    assert len(blob["cols"]) == len(blob["rows"][0])
    # La primera columna del blob es Attrition: las bajas del dashboard tienen
    # que ser las mismas que las de los datos.
    assert sum(fila[0] for fila in blob["rows"]) == BAJAS


def test_el_blob_no_puede_romper_el_html(df):
    """El blob viaja dentro de <script>: un '</script' cerraría la etiqueta."""
    assert "</script" not in build_dashboard.construir_blob(df)


def test_la_plantilla_tiene_exactamente_un_marcador():
    tpl = paths.require(paths.DASHBOARD_TEMPLATE).read_text(encoding="utf-8")
    assert tpl.count(build_dashboard.MARCADOR) == 1


def test_build_completo_produce_un_dashboard_valido():
    r = build_dashboard.build()
    assert r["filas"] == FILAS
    assert r["bajas"] == BAJAS
    assert r["tasa"] == pytest.approx(TASA_GENERAL, abs=0.01)

    html = paths.DASHBOARD_HTML.read_text(encoding="utf-8")
    assert build_dashboard.MARCADOR not in html
    assert len(html.encode("utf-8")) > build_dashboard.MIN_BYTES_SALIDA
    # Lo que publica el CI tiene que ser idéntico al entregable versionado.
    assert (paths.SITE_DIR / "index.html").read_bytes() == paths.DASHBOARD_HTML.read_bytes()


def test_el_build_escribe_siempre_con_LF():
    """Si no, el mismo commit produce archivos distintos en Windows y en el CI."""
    assert b"\r" not in paths.DASHBOARD_HTML.read_bytes()


# ============ que pasa cuando las cosas van mal ============

def test_un_dataset_vacio_no_genera_dashboard(df):
    with pytest.raises(ValueError, match="no tiene filas"):
        build_dashboard.construir_blob(df.iloc[0:0])


def test_un_dataset_recortado_no_genera_dashboard(df):
    """El caso peligroso: un filtro que deja pocas filas y se publica igual."""
    with pytest.raises(ValueError, match="se esperan al menos"):
        build_dashboard.construir_blob(df.head(10))


def test_si_falta_una_columna_falla_con_el_nombre(df):
    with pytest.raises(KeyError, match="MonthlyIncome"):
        build_dashboard.construir_blob(df.drop(columns=["MonthlyIncome"]))


def test_un_archivo_que_falta_dice_que_correr():
    inexistente = paths.PROCESSED_DIR / "no_existe.csv"
    with pytest.raises(FileNotFoundError):
        paths.require(inexistente)
