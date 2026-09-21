# Data Understanding (Comprensión de los Datos)

## 1. Resumen del Dataset
- **Nombre**: IBM HR Analytics Employee Attrition & Performance
- **Registros (filas)**: 1470 empleados
- **Variables (columnas)**: 35
- **Tipo de datos**: Mixto (numéricos y categóricos)
- **Valores faltantes**: Ninguno (dataset limpio inicial)
- **Duplicados**: Ninguno

---

## 2. Variables Constantes
Se identificaron 3 variables con un solo valor único (constantes). Estas variables no aportan información para el análisis y podrían ser eliminadas en la fase de preparación de datos:
1. `EmployeeCount`: Siempre 1
2. `Over18`: Siempre 'Y'
3. `StandardHours`: Siempre 80

---

## 3. Clasificación de Variables
### Variables Numéricas (26):
`Age`, `DailyRate`, `DistanceFromHome`, `Education`, `EmployeeCount`, `EmployeeNumber`, `EnvironmentSatisfaction`, `HourlyRate`, `JobInvolvement`, `JobLevel`, `JobSatisfaction`, `MonthlyIncome`, `MonthlyRate`, `NumCompaniesWorked`, `PercentSalaryHike`, `PerformanceRating`, `RelationshipSatisfaction`, `StandardHours`, `StockOptionLevel`, `TotalWorkingYears`, `TrainingTimesLastYear`, `WorkLifeBalance`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsSinceLastPromotion`, `YearsWithCurrManager`

### Variables Categóricas (9):
`Attrition` (variable objetivo), `BusinessTravel`, `Department`, `EducationField`, `Gender`, `JobRole`, `MaritalStatus`, `Over18`, `OverTime`

---

## 4. Variable Objetivo
- **`Attrition`**: Indica si un empleado abandonó la empresa (Yes) o permaneció (No)
- **Distribución inicial**:
  - No: ~83.9% (1233 empleados)
  - Yes: ~16.1% (237 empleados)
  - El dataset está desbalanceado (más empleados que se quedaron que se fueron)

---

## 5. Hallazgos Iniciales
- El dataset está completo (sin valores faltantes ni duplicados)
- Hay variables de satisfacción (JobSatisfaction, EnvironmentSatisfaction, RelationshipSatisfaction, WorkLifeBalance) que probablemente están correlacionadas con la rotación
- Variables de permanencia y progreso (YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager)
- Variables de ingreso (DailyRate, HourlyRate, MonthlyIncome, MonthlyRate, PercentSalaryHike)
- Variables demográficas (Age, Gender, MaritalStatus, Education, EducationField)

---

## 6. Diccionario de Datos Completo
Para una descripción detallada de cada variable, ver el archivo [docs/data_dictionary.md](file:///d:\RRHH\docs\data_dictionary.md).
