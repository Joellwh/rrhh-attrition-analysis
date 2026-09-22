# IBM HR Analytics — Análisis de Rotación de Empleados

[![build y publicar dashboard](https://github.com/Joellwh/rrhh-attrition-analysis/actions/workflows/pages.yml/badge.svg)](https://github.com/Joellwh/rrhh-attrition-analysis/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

Análisis completo de los factores que explican la rotación de personal en una
plantilla de 1.470 empleados, siguiendo la metodología **CRISP-DM**, con un
dashboard ejecutivo interactivo como entregable final.

###  [Ver el dashboard en vivo](https://joellwh.github.io/rrhh-attrition-analysis/)

La insignia de arriba no es decorativa: en cada push, GitHub Actions instala las
dependencias fijadas, corre los tests, reconstruye el dashboard desde los datos
y verifica que traiga los 1.470 empleados antes de publicarlo. Si algo no da,
no se despliega.

> **Los datos son ficticios.** Es el dataset sintético de demostración de IBM.
> Ningún registro corresponde a una persona real. Ver [`data/README.md`](data/README.md).

---

## Contexto del negocio

La rotación de empleados es cara: implica gastos de contratación, capacitación y
pérdida de conocimiento institucional. Este proyecto simula un escenario donde
una empresa busca entender por qué se le van los empleados y qué puede hacer
para retenerlos.

---

## Hallazgos clave

| Hallazgo | Dato |
|---|---|
| Tasa de rotación general | **16,12%** (237 de 1.470) |
| Rol más afectado | **Sales Representative**, 39,76% |
| Departamento más afectado | **Ventas**, 20,63% |
| Con horas extra | **30,53%** contra 10,44% sin horas extra |
| Brecha salarial | Quien se va gana en promedio **$2.046 menos** por mes |

Las horas extra son el factor individual más fuerte: triplican la tasa de
rotación. El detalle de cada hallazgo, con sus salvedades estadísticas, está en
[`docs/06_conclusions_recommendations.md`](docs/06_conclusions_recommendations.md).

### Una salvedad importante

El grupo "promovido en el último año" muestra más rotación (18,93%), pero ese
resultado está confundido con la antigüedad: ese grupo tiene la mitad de años en
la empresa (4,4 contra 8,7). No es que promover haga renunciar a la gente, es
que son empleados nuevos. Está documentado en `sql/queries.sql` y en las
conclusiones.

---

## Recomendaciones de negocio

1. Reducir las horas extra obligatorias, empezando por Ventas y Laboratorio.
2. Revisar la competitividad salarial en los niveles de entrada.
3. Ofrecer trabajo híbrido o subsidio de transporte para quienes viven lejos.
4. Programas de mentoría para empleados nuevos y jóvenes.
5. Encuestas de satisfacción dirigidas a los equipos con mayor rotación.

---

## Reproducir el análisis

Todo el proyecto se reproduce con los datos que vienen en el repo. No hace falta
descargar nada.

```bash
git clone https://github.com/Joellwh/rrhh-attrition-analysis.git
cd rrhh-attrition-analysis
```

```bash
python -m venv venv && venv\Scripts\activate        # Windows
python -m venv venv && source venv/bin/activate     # macOS / Linux
```

```bash
pip install -r requirements.txt
```

Después, **en este orden** (cada paso consume lo que produjo el anterior):

| # | Comando | Qué hace | Qué produce |
|---|---|---|---|
| 1 | `python src/data_preparation.py` | Limpia el CSV crudo | `data/processed/clean_data.csv` |
| 2 | `python src/explore_data.py` | Explora y documenta variables | `docs/data_dictionary.md` |
| 3 | `python src/run_eda.py` | Análisis exploratorio | `reports/*.png` |
| 4 | `python src/run_sql_queries.py` | 14 consultas sobre SQLite | Salida por consola |
| 5 | `python src/build_dashboard.py` | Arma el dashboard | `dashboards/rrhh_dashboard.html` |

El paso 1 es obligatorio antes que el resto: los demás scripts leen
`clean_data.csv`. Si lo salteás, cada script te dice exactamente qué correr.

### Tests

```bash
pytest
```

19 tests que fijan los números verificados del análisis (tasa general, rol y
departamento peores, efecto de las horas extra) y los casos de fallo del build.
Existen para que un pipeline roto no publique un dashboard con números
equivocados o vacío.

### Reconstruir el dashboard

El dashboard se genera desde una plantilla y los datos, nunca se edita a mano:

```bash
python src/build_dashboard.py
```

Para cambiar el diseño, editá `assets/dashboard_template.html` y volvé a
construir. El CI verifica que el HTML versionado coincida con lo que produce el
código, así que una edición manual del archivo generado se detecta sola.

---

## Estructura del proyecto

```
rrhh-attrition-analysis/
├── assets/
│   └── dashboard_template.html       Plantilla del dashboard (HTML + CSS + JS)
├── data/
│   ├── README.md                     Procedencia y advertencias sobre los datos
│   ├── raw/
│   │   └── WA_Fn-UseC_-...csv        Dataset de IBM, versionado (228 KB)
│   └── processed/                    Derivado, se regenera (no versionado)
├── dashboards/
│   └── rrhh_dashboard.html           Dashboard interactivo, entregable
├── docs/
│   ├── 01_business_understanding.md  Las 6 fases de CRISP-DM, una por archivo
│   ├── ...
│   └── data_dictionary.md            Las 35 variables, qué significa cada una
├── notebooks/
│   └── 01_eda.ipynb                  Análisis exploratorio en Jupyter
├── reports/                          10 gráficos generados por run_eda.py
├── sql/
│   └── queries.sql                   14 consultas de negocio
├── src/
│   ├── paths.py                      Rutas del proyecto, independientes del cwd
│   ├── download_data.py              Descarga opcional, con verificación
│   ├── explore_data.py               Exploración y diccionario de datos
│   ├── data_preparation.py           Limpieza y transformación
│   ├── run_eda.py                    EDA y visualizaciones
│   ├── run_sql_queries.py            Consultas SQL sobre SQLite
│   └── build_dashboard.py            Construcción del dashboard
├── tests/
│   └── test_pipeline.py              19 tests del pipeline y del build
└── .github/workflows/pages.yml       CI: tests, build y publicación
```

---

## El dashboard

Un solo archivo HTML de 152 KB, sin frameworks ni dependencias externas. Los
1.470 empleados viajan embebidos como JSON y los filtros recalculan en el
navegador, así que responde al instante y funciona sin conexión.

- **Cinco vistas**: Panorama, Compensación y carga, Clima interno, Trayectoria y Detalle
- **Filtros combinables** por departamento, rol, viajes, estado civil, género, formación y horas extra
- **Matriz de plantilla**: un cuadrado por empleado, que se achica al filtrar para que se vea cuándo la muestra deja de ser confiable
- **Avisos de muestra chica** cuando un corte queda por debajo del umbral
- Tema claro y oscuro, y funciona en pantalla de teléfono

---

## Tecnologías

| Área | Herramientas |
|---|---|
| Lenguaje | Python 3.12 |
| Análisis | pandas 3.0.5, NumPy 2.5.1 |
| Visualización | Matplotlib 3.11.1, Seaborn 0.13.2 |
| Base de datos | SQLite (módulo estándar) |
| Dashboard | HTML, CSS y JavaScript sin frameworks |
| Tests | pytest 9.1.1 |
| CI/CD | GitHub Actions y GitHub Pages |

Las versiones están fijadas en `requirements.txt`. El análisis se desarrolló
contra pandas 3.x, cuya API difiere de la 2.x.

---

## Metodología (CRISP-DM)

| Fase | Documento |
|---|---|
| 1. Business Understanding | [`docs/01_business_understanding.md`](docs/01_business_understanding.md) |
| 2. Project Plan | [`docs/02_project_plan.md`](docs/02_project_plan.md) |
| 3. Data Understanding | [`docs/03_data_understanding.md`](docs/03_data_understanding.md) |
| 4. Data Preparation | [`docs/04_data_preparation.md`](docs/04_data_preparation.md) |
| 5. EDA | [`docs/05_eda.md`](docs/05_eda.md) |
| 6. Conclusiones | [`docs/06_conclusions_recommendations.md`](docs/06_conclusions_recommendations.md) |

---

## Dataset

**IBM HR Analytics Employee Attrition & Performance.** 1.470 registros, 35
variables: demográficas, satisfacción, desempeño, salarios y rotación. Es un
conjunto sintético creado por científicos de datos de IBM para demostración.
Disponible también en
[Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).

Se versiona dentro del repo para que el análisis sea reproducible sin depender
de servicios externos, y su integridad se verifica por checksum en los tests.
Los detalles están en [`data/README.md`](data/README.md).

---

## Pendiente

- Dashboard en Power BI como entregable alternativo

---

## Licencia

MIT. Ver [`LICENSE`](LICENSE).

La licencia cubre el código y la documentación de este repositorio. El dataset
de `data/raw/` es el conjunto sintético de demostración publicado por IBM y no
está cubierto por ella; se incluye con fines educativos. Detalles en
[`data/README.md`](data/README.md).

---

## Autor

**Joel Dragonetti** — [@Joellwh](https://github.com/Joellwh)

Para preguntas sobre el proyecto, abrí un
[issue](https://github.com/Joellwh/rrhh-attrition-analysis/issues).
