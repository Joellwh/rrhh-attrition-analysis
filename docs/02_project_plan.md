# Project Plan (Plan del Proyecto)

## 1. Metodología: CRISP-DM
Se utilizará la metodología **CRISP-DM (Cross-Industry Standard Process for Data Mining)**, que consta de 6 fases iterativas:

1. **Business Understanding (Comprensión del Negocio)**: Definir objetivos y requisitos del negocio
2. **Data Understanding (Comprensión de los Datos)**: Explorar y familiarizarse con el dataset
3. **Data Preparation (Preparación de los Datos)**: Limpiar y transformar datos para análisis
4. **Modeling (Modelado)**: Aplicar técnicas de análisis o modelos predictivos
5. **Evaluation (Evaluación)**: Validar resultados y medir cumplimiento de objetivos
6. **Deployment (Despliegue)**: Documentar y compartir resultados (dashboard, reportes, recomendaciones)

---

## 2. Cronograma por Fases
| Fase | Duración Estimada | Actividades Principales |
|------|-------------------|-------------------------|
| 1. Business Understanding | 1-2 días | Definir contexto, objetivos, preguntas de negocio y KPIs |
| 2. Data Understanding | 2-3 días | Explorar datos, crear diccionario de datos, identificar problemas iniciales |
| 3. Data Preparation | 2-3 días | Limpiar datos, manejar valores faltantes/duplicados, transformar variables |
| 4. Modeling & Analysis | 3-4 días | EDA avanzado, consultas SQL, visualizaciones, análisis de correlación |
| 5. Evaluation | 1-2 días | Validar hallazgos, definir recomendaciones |
| 6. Deployment | 2-3 días | Crear dashboard, documentar proyecto, preparar para publicación |
| **Total** | **~12-17 días** | |

---

## 3. Entregables de Cada Fase
| Fase | Entregables |
|------|-------------|
| 1. Business Understanding | `docs/01_business_understanding.md` |
| 2. Data Understanding | `docs/02_data_understanding.md`, `docs/data_dictionary.md`, notebook de EDA inicial |
| 3. Data Preparation | `src/data_preparation.py`, `data/processed/clean_data.csv`, `docs/03_data_preparation.md` |
| 4. Modeling & Analysis | Notebooks de EDA avanzado, `sql/queries.sql`, visualizaciones en `reports/` |
| 5. Evaluation | `docs/04_evaluation.md`, `docs/05_conclusions_recommendations.md` |
| 6. Deployment | Dashboard en Power BI (`dashboards/`), `README.md` profesional, repositorio GitHub |

---

## 4. Tecnologías Utilizadas
| Categoría | Tecnologías |
|-----------|-------------|
| Control de Versiones | Git, GitHub |
| Lenguaje de Programación | Python 3.x |
| Librerías de Análisis | Pandas, NumPy |
| Visualización | Matplotlib, Seaborn, Power BI |
| Bases de Datos | SQLite (para consultas SQL) |
| Documentación | Markdown |

---

## 5. Estructura del Proyecto
```
RRHH/
├── data/
│   ├── raw/                # Datos originales (no modificados)
│   │   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   └── processed/          # Datos limpios y transformados
├── notebooks/              # Jupyter Notebooks para EDA y análisis
├── src/                    # Scripts de Python (descarga, limpieza, análisis)
│   ├── download_data.py
│   ├── explore_data.py
│   └── data_preparation.py
├── sql/                    # Consultas SQL
├── reports/                # Visualizaciones y reportes
├── dashboards/             # Archivos de Power BI
├── docs/                   # Documentación del proyecto
│   ├── 01_business_understanding.md
│   ├── 02_project_plan.md
│   ├── 03_data_understanding.md
│   ├── 04_evaluation.md
│   ├── 05_conclusions_recommendations.md
│   └── data_dictionary.md
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 6. Convenciones
- **Nombre de archivos**: Uso de `snake_case` para scripts y notebooks
- **Nombre de variables**: Uso de `snake_case` en código Python
- **Commits de Git**: Mensajes claros y descriptivos en inglés o español (ej: "feat: agregar script de exploración de datos")
- **Documentación**: Todo cambio importante debe estar documentado en la carpeta `docs/`
