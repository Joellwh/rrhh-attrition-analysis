# Data Preparation (Preparación de los Datos)

## 1. Objetivo de la Fase
Limpiar y transformar el dataset para que esté listo para el análisis exploratorio y modelado.

---

## 2. Pasos Realizados
### 2.1 Carga de Datos
- Se cargó el dataset original desde `data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv` (1470 filas, 35 columnas).

### 2.2 Eliminación de Variables Constantes
Se identificaron y eliminaron 3 variables que tienen un solo valor único y no aportan información para el análisis:
- `EmployeeCount`: Siempre 1
- `Over18`: Siempre 'Y'
- `StandardHours`: Siempre 80

### 2.3 Conversión de Tipos de Datos
Se convirtieron las variables categóricas a tipo `category` para mejorar el rendimiento y la semántica:
- `Attrition`
- `BusinessTravel`
- `Department`
- `EducationField`
- `Gender`
- `JobRole`
- `MaritalStatus`
- `OverTime`

### 2.4 Codificación de Variable Objetivo
Se codificó la variable objetivo `Attrition` a valores numéricos para facilitar análisis y modelado:
- `Yes` → 1 (rotación)
- `No` → 0 (no rotación)

### 2.5 Guardado de Datos Limpios
El dataset limpio se guardó en `data/processed/clean_data.csv`.

---

## 3. Resultado Final
- **Filas**: 1470 (mismo número que original, no se eliminaron registros)
- **Columnas**: 32 (se eliminaron 3 variables constantes)
- **Variables numéricas**: 24
- **Variables categóricas**: 8 (incluyendo la variable objetivo codificada `Attrition`)

---

## 4. Script Utilizado
El script de preparación de datos se encuentra en: [src/data_preparation.py](file:///d:\RRHH\src\data_preparation.py)
