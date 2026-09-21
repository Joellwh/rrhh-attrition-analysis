"""
Descarga (opcional) del dataset IBM HR Analytics Employee Attrition & Performance.

NO hace falta correr esto para usar el proyecto: el CSV viene versionado en
data/raw/. Este script existe solo para volver a bajarlo si se borró, y valida
todo antes de escribir para no dejar un archivo corrupto en su lugar.

Flujo:

    descarga a archivo temporal
        ├─ status HTTP != 200      -> aborta
        ├─ el cuerpo no es un CSV  -> aborta (una pagina de error HTML da 200)
        ├─ sha256 distinto al fijado en paths.RAW_CSV_SHA256 -> aborta
        └─ todo OK                 -> recien ahi reemplaza data/raw/*.csv
"""

import hashlib
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

import paths

URL = (
    "https://raw.githubusercontent.com/sk-shane-Alam/"
    "IBM-HR-Analytics-Employee-Attrition-Analysis/main/"
    "IBM%20HR%20Employee%20Attrition%20Data.csv"
)

TIMEOUT_SEG = 30
# El CSV real pesa ~228 KB. Cualquier cosa mucho mas chica es una pagina de error.
MIN_BYTES = 100_000
# Primera columna del encabezado del dataset.
ENCABEZADO_ESPERADO = "Age,Attrition"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def _validar(tmp: Path) -> None:
    """Falla ruidosamente si lo descargado no es el CSV esperado."""
    tam = tmp.stat().st_size
    if tam < MIN_BYTES:
        raise ValueError(
            f"La descarga pesa {tam} bytes, muy poco para este dataset "
            f"(se esperan ~{MIN_BYTES}+). Probablemente el servidor devolvió "
            f"una página de error con status 200."
        )

    primera = tmp.read_text(encoding="utf-8", errors="replace").split("\n", 1)[0]
    if not primera.startswith(ENCABEZADO_ESPERADO):
        raise ValueError(
            f"El contenido no parece el CSV esperado.\n"
            f"  Primera línea: {primera[:120]!r}\n"
            f"  Se esperaba que empezara con: {ENCABEZADO_ESPERADO!r}"
        )

    obtenido = _sha256(tmp)
    if obtenido != paths.RAW_CSV_SHA256:
        raise ValueError(
            f"El sha256 no coincide: el archivo remoto cambió.\n"
            f"  esperado: {paths.RAW_CSV_SHA256}\n"
            f"  obtenido: {obtenido}\n"
            f"No se sobrescribió nada. Si el cambio es legítimo, actualizá "
            f"RAW_CSV_SHA256 en src/paths.py y volvé a correr los tests."
        )


def download_dataset() -> Path:
    destino = paths.RAW_CSV
    paths.ensure_dir(paths.RAW_DIR)

    print(f"Descargando dataset desde {URL} ...")
    tmp_dir = Path(tempfile.mkdtemp(prefix="rrhh-download-"))
    tmp = tmp_dir / "descarga.csv"
    try:
        try:
            with urllib.request.urlopen(URL, timeout=TIMEOUT_SEG) as resp:
                if resp.status != 200:
                    raise ValueError(f"El servidor respondió {resp.status}, se esperaba 200.")
                tmp.write_bytes(resp.read())
        except urllib.error.HTTPError as e:
            raise ValueError(
                f"El servidor respondió {e.code} ({e.reason}).\n"
                f"El dataset se descarga de un repo de terceros que puede haber "
                f"desaparecido. El CSV está versionado en el repo: recuperalo con "
                f"'git checkout -- data/raw/' en vez de volver a descargarlo."
            ) from e
        except urllib.error.URLError as e:
            raise ValueError(
                f"No se pudo conectar ({e.reason}). Revisá la conexión o usá el "
                f"CSV versionado: git checkout -- data/raw/"
            ) from e
        except TimeoutError as e:
            raise ValueError(
                f"La descarga superó los {TIMEOUT_SEG} segundos y se abortó."
            ) from e

        _validar(tmp)
        shutil.move(str(tmp), str(destino))
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    print(f"Dataset verificado y guardado en: {destino.relative_to(paths.ROOT)}")
    print(f"  {destino.stat().st_size} bytes, sha256 {paths.RAW_CSV_SHA256[:12]}…")
    return destino


if __name__ == "__main__":
    try:
        download_dataset()
    except ValueError as e:
        print(f"\nLa descarga se abortó sin tocar el archivo existente:\n{e}", file=sys.stderr)
        sys.exit(1)
