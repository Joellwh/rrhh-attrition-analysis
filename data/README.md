# Datos

## Qué hay acá

```
data/
├── raw/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv   versionado · 227.977 bytes
└── processed/
    └── clean_data.csv                          derivado · no se versiona
```

## Los datos son ficticios

**Ningún registro de este dataset corresponde a una persona real.**

Es el *IBM HR Analytics Employee Attrition & Performance*, un conjunto de datos
sintético creado por científicos de datos de IBM para demostración y enseñanza.
Los 1.470 empleados, sus salarios, sus evaluaciones y sus renuncias son
inventados. Se publica abiertamente y se redistribuye en cientos de proyectos
educativos, incluido este.

Se aclara porque el dashboard publica los 1.470 registros completos y, sin este
aviso, alguien podría razonablemente pensar que se trata de información real de
recursos humanos de una empresa.

## Por qué el CSV crudo está versionado

Lo habitual es no commitear datos. Esa regla existe para datos grandes, privados
o que cambian seguido, y acá no aplica ninguno de los tres casos: son 228 KB de
un dataset público y fijo que además *es* el objeto del proyecto.

Versionarlo compra dos cosas:

- **El repo es autocontenido.** Alguien clona y corre el análisis sin descargar
  nada. Antes el CSV se bajaba del repo de un tercero: si esa persona lo borraba,
  el proyecto dejaba de poder reproducirse.
- **El CI no depende de la red.** El workflow corre el pipeline completo sin
  pedirle nada a servidores ajenos.

La integridad se verifica por checksum. El sha256 esperado vive en
`src/paths.py` (`RAW_CSV_SHA256`) y lo comprueba `tests/test_pipeline.py`:

```
a5c31e38bd7fafc9bc333884eb181b06b41b8e5e488e8f7ccb27199fb3be7659
```

El archivo tiene finales de línea CRLF tal como vino del origen, y
`.gitattributes` lo marca como binario para que git no los convierta. Sin eso,
el checksum daría distinto en Linux y en Windows.

## `data/processed/` no se versiona

`clean_data.csv` lo genera `src/data_preparation.py` a partir del CSV crudo:
elimina tres columnas constantes (`EmployeeCount`, `Over18`, `StandardHours`),
convierte las categóricas y codifica `Attrition` a 0/1. Es derivado y
reproducible, así que no tiene sentido versionarlo.

```bash
python src/data_preparation.py
```

## Volver a descargar el crudo

No hace falta, pero si borraste el archivo:

```bash
git checkout -- data/raw/          # lo recupera del repo
python src/download_data.py        # o lo vuelve a bajar del origen
```

`download_data.py` verifica status HTTP, tamaño, encabezado y sha256 antes de
escribir nada. Si algo no coincide, aborta sin tocar el archivo existente.

## Si alguna vez usás datos reales

El dashboard lleva los 1.470 registros **embebidos dentro del HTML**. Publicado
en GitHub Pages, eso queda en internet abierto e indexable por buscadores.

Con datos reales de una empresa esto no sirve: necesitás un hosting con control
de acceso (Cloudflare Pages + Access, o Power BI Service con permisos), y
seguramente una revisión de qué campos se pueden exponer.

## Fuente

Publicado originalmente por IBM como dataset de muestra. La copia versionada acá
proviene de un espejo público en GitHub; la URL exacta está en
`src/download_data.py`.
