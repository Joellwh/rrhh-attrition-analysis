"""
Rutas del proyecto, resueltas desde la ubicación de este archivo.

Todos los scripts importan de acá en lugar de construir rutas relativas al
directorio de trabajo. Así `python src/run_eda.py` desde la raíz y
`cd src && python run_eda.py` producen exactamente el mismo resultado.

    ROOT/
    ├── data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv   (versionado)
    ├── data/processed/clean_data.csv                    (derivado)
    ├── sql/queries.sql
    ├── assets/dashboard_template.html
    ├── dashboards/rrhh_dashboard.html                   (entregable)
    ├── reports/*.png                                    (entregables)
    └── _site/index.html                                 (lo publica el CI)
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = ROOT / "reports"
SQL_DIR = ROOT / "sql"
DOCS_DIR = ROOT / "docs"
ASSETS_DIR = ROOT / "assets"
DASHBOARDS_DIR = ROOT / "dashboards"
SITE_DIR = ROOT / "_site"

RAW_CSV = RAW_DIR / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
PROCESSED_CSV = PROCESSED_DIR / "clean_data.csv"
QUERIES_SQL = SQL_DIR / "queries.sql"
DATA_DICTIONARY_MD = DOCS_DIR / "data_dictionary.md"
DASHBOARD_TEMPLATE = ASSETS_DIR / "dashboard_template.html"
DASHBOARD_HTML = DASHBOARDS_DIR / "rrhh_dashboard.html"

# sha256 del CSV crudo tal como está versionado en el repo. src/download_data.py
# lo usa para no sobrescribir con una descarga corrupta, y tests/ lo verifica.
RAW_CSV_SHA256 = "a5c31e38bd7fafc9bc333884eb181b06b41b8e5e488e8f7ccb27199fb3be7659"

# Cómo regenerar cada archivo derivado. require() lo muestra cuando falta.
_COMO_GENERAR = {
    PROCESSED_CSV: "Generalo con:  python src/data_preparation.py",
    RAW_CSV: "El CSV viene versionado en el repo. Si lo borraste, recuperalo con:\n"
             "  git checkout -- data/raw/\n"
             "o volvé a descargarlo con:  python src/download_data.py",
    DASHBOARD_TEMPLATE: "Falta la plantilla del dashboard. Recuperala con:\n"
                        "  git checkout -- assets/",
}


def ensure_dir(path: Path) -> Path:
    """Crea el directorio (y sus padres) si no existe, y lo devuelve."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def require(path: Path) -> Path:
    """
    Devuelve la ruta si el archivo existe. Si no, falla con un mensaje que dice
    qué correr para generarlo, en vez de un FileNotFoundError pelado.
    """
    if path.exists():
        return path

    try:
        mostrada = path.relative_to(ROOT)
    except ValueError:
        mostrada = path

    ayuda = _COMO_GENERAR.get(path, "Revisá que el archivo exista en el repo.")
    raise FileNotFoundError(f"No se encontró {mostrada}\n{ayuda}")
