"""
Construye el dashboard interactivo de rotación a partir de los datos limpios.

Reemplaza los tres scripts encadenados que había antes (extraer datos, inyectar,
empalmar CSS) por un solo comando:

    python src/build_dashboard.py

Flujo y validaciones:

    data/processed/clean_data.csv
            │
            ▼
      [ falta el archivo? ]  ──► FileNotFoundError con qué correr primero
            │
            ▼
      indexa a blob JSON compacto
            │
            ├─ [ 0 filas? ]        ──► ValueError, corta antes de generar
            ├─ [ falta columna? ]  ──► KeyError con el nombre
            └─ [ el JSON trae '</script'? ] ──► ValueError (rompería el HTML)
            │
            ▼
      assets/dashboard_template.html
            │
            ├─ [ falta el marcador? ] ──► ValueError
            │
            ▼
      [ el HTML final pesa menos de lo mínimo? ] ──► ValueError
            │
            ▼
      dashboards/rrhh_dashboard.html   (entregable versionado)
      _site/index.html                 (lo que publica el CI)

Las validaciones existen para que un pipeline roto falle acá y no publique
un dashboard vacío.
"""

import json
import sys

import pandas as pd

import paths

MARCADOR = "__DATA_PLACEHOLDER__"

# Categóricas: van al blob como índice entero contra una lista de valores, para
# no repetir el texto 1.470 veces.
CAT_COLS = [
    "Department",
    "JobRole",
    "Gender",
    "MaritalStatus",
    "BusinessTravel",
    "EducationField",
]

# Numéricas y ordinales: van como entero directo.
NUM_COLS = [
    "Age", "MonthlyIncome", "DistanceFromHome", "JobLevel",
    "JobSatisfaction", "EnvironmentSatisfaction", "WorkLifeBalance",
    "RelationshipSatisfaction", "JobInvolvement", "YearsAtCompany",
    "YearsSinceLastPromotion", "YearsWithCurrManager", "YearsInCurrentRole",
    "TotalWorkingYears", "StockOptionLevel", "TrainingTimesLastYear",
    "NumCompaniesWorked", "Education", "PercentSalaryHike", "EmployeeNumber",
]

# El dataset tiene 1.470 empleados. Si el blob sale con muchos menos, algo se
# rompió aguas arriba y no queremos publicarlo.
MIN_FILAS = 1_000
# La plantilla sola pesa ~56 KB; con datos supera los 150 KB.
MIN_BYTES_SALIDA = 100_000


def construir_blob(df: pd.DataFrame) -> str:
    """Indexa el DataFrame a un blob JSON compacto para el cliente."""
    if len(df) == 0:
        raise ValueError(
            "clean_data.csv no tiene filas. No se genera el dashboard.\n"
            "Regeneralo con:  python src/data_preparation.py"
        )
    if len(df) < MIN_FILAS:
        raise ValueError(
            f"clean_data.csv tiene solo {len(df)} filas y se esperan al menos "
            f"{MIN_FILAS}. Algo filtró de más aguas arriba; no se genera el dashboard."
        )

    faltantes = [c for c in ["Attrition", "OverTime", *CAT_COLS, *NUM_COLS] if c not in df.columns]
    if faltantes:
        raise KeyError(f"Faltan columnas en clean_data.csv: {faltantes}")

    dims = {c: sorted(df[c].unique().tolist()) for c in CAT_COLS}
    idx = {c: {v: i for i, v in enumerate(vals)} for c, vals in dims.items()}

    cols = ["Attrition", "OverTime"] + CAT_COLS + NUM_COLS
    rows = []
    for _, r in df.iterrows():
        row = [int(r["Attrition"]), 1 if r["OverTime"] == "Yes" else 0]
        row += [idx[c][r[c]] for c in CAT_COLS]
        row += [int(r[c]) for c in NUM_COLS]
        rows.append(row)

    blob = json.dumps(
        {"cols": cols, "dims": dims, "rows": rows},
        ensure_ascii=False,
        separators=(",", ":"),
    )

    # El blob viaja dentro de <script type="application/json">. Un '</script'
    # ahí adentro cerraría la etiqueta antes de tiempo y rompería la página.
    if "</script" in blob:
        raise ValueError("El blob de datos contiene '</script': rompería el HTML.")

    return blob


def build() -> dict:
    df = pd.read_csv(paths.require(paths.PROCESSED_CSV))
    blob = construir_blob(df)

    plantilla = paths.require(paths.DASHBOARD_TEMPLATE).read_text(encoding="utf-8")
    if plantilla.count(MARCADOR) != 1:
        raise ValueError(
            f"La plantilla debe contener exactamente un {MARCADOR}, "
            f"tiene {plantilla.count(MARCADOR)}."
        )

    html = plantilla.replace(MARCADOR, blob)

    if MARCADOR in html:
        raise ValueError("Quedó el marcador sin reemplazar en la salida.")
    tam = len(html.encode("utf-8"))
    if tam < MIN_BYTES_SALIDA:
        raise ValueError(
            f"El HTML generado pesa {tam} bytes, menos del mínimo de "
            f"{MIN_BYTES_SALIDA}. No se escribe: parece un dashboard degenerado."
        )

    # Entregable versionado + copia que publica el CI.
    # newline="\n" explícito: sin esto Windows escribe CRLF y el CI en Linux LF,
    # así que el mismo commit produciría archivos distintos según dónde corra.
    paths.ensure_dir(paths.DASHBOARDS_DIR)
    paths.DASHBOARD_HTML.write_text(html, encoding="utf-8", newline="\n")
    paths.ensure_dir(paths.SITE_DIR)
    (paths.SITE_DIR / "index.html").write_text(html, encoding="utf-8", newline="\n")

    bajas = int(df["Attrition"].sum())
    return {
        "filas": len(df),
        "bajas": bajas,
        "tasa": bajas / len(df) * 100,
        "bytes": tam,
        "blob_kb": len(blob.encode("utf-8")) / 1024,
    }


if __name__ == "__main__":
    try:
        r = build()
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"\nEl build se abortó:\n{e}", file=sys.stderr)
        sys.exit(1)

    print(f"Dashboard generado: {r['bytes'] / 1024:.1f} KB "
          f"({r['blob_kb']:.1f} KB de datos)")
    print(f"  {r['filas']} empleados, {r['bajas']} bajas, {r['tasa']:.2f}% de rotación")
    print(f"  -> {paths.DASHBOARD_HTML.relative_to(paths.ROOT)}")
    print(f"  -> {(paths.SITE_DIR / 'index.html').relative_to(paths.ROOT)}")
