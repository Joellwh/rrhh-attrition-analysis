# Análisis Exploratorio de Datos (EDA)

## 1. Objetivo de la Fase
Explorar el dataset para identificar patrones, relaciones y factores que influyen en la rotación de empleados.

---

## 2. Archivos Generados
- **Notebook**: [notebooks/01_eda.ipynb](file:///d:\RRHH\notebooks\01_eda.ipynb)
- **Script de ejecución**: [src/run_eda.py](file:///d:\RRHH\src\run_eda.py)
- **Visualizaciones**: Carpeta `reports/` (10 gráficos PNG)
- **Consultas SQL**: [sql/queries.sql](file:///d:\RRHH\sql\queries.sql)
- **Script SQL**: [src/run_sql_queries.py](file:///d:\RRHH\src\run_sql_queries.py)

---

## 3. Hallazgos Clave del EDA
### 3.1 Variable Objetivo (Attrition)
- Tasa de rotación general: **16.1%** (237 empleados se fueron, 1233 se quedaron).
- Dataset desbalanceado (muchos más empleados que no rotaron).

### 3.2 Variables Categóricas vs Attrition
1. **Departamento**:
   - Ventas tiene la mayor tasa de rotación.
   - Research & Development tiene la menor.
2. **Rol de Trabajo**:
   - Sales Representative y Laboratory Technician tienen las tasas más altas.
   - Manager tiene la tasa más baja.
3. **Horas Extras (OverTime)**:
   - Los empleados que hacen horas extras tienen **mucha mayor probabilidad de rotar**.
4. **Estado Civil**:
   - Solteros tienen mayor tasa de rotación que casados o divorciados.

### 3.3 Variables Numéricas vs Attrition
1. **Edad**:
   - Los empleados más jóvenes (menores de 35) tienden a rotar más.
2. **Ingreso Mensual**:
   - Los empleados con menor ingreso mensual tienen mayor rotación.
3. **Distancia del Hogar**:
   - Los empleados que viven más lejos tienen mayor probabilidad de rotar.
4. **Años Totales de Trabajo**:
   - Los empleados con menos experiencia total tienen mayor rotación.

### 3.4 Correlaciones
- Correlaciones importantes con `Attrition`:
  - Positiva (mayor valor → más rotación): `DistanceFromHome`, `NumCompaniesWorked`.
  - Negativa (mayor valor → menos rotación): `Age`, `MonthlyIncome`, `TotalWorkingYears`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsWithCurrManager`.

---

## 4. Visualizaciones Generadas
1. `reports/attrition_distribution.png`: Distribución de Attrition.
2. `reports/Department_vs_attrition.png`: Rotación por Departamento.
3. `reports/JobRole_vs_attrition.png`: Rotación por Rol de Trabajo.
4. `reports/OverTime_vs_attrition.png`: Rotación por Horas Extras.
5. `reports/MaritalStatus_vs_attrition.png`: Rotación por Estado Civil.
6. `reports/Age_vs_attrition.png`: Edad vs Rotación.
7. `reports/MonthlyIncome_vs_attrition.png`: Ingreso vs Rotación.
8. `reports/DistanceFromHome_vs_attrition.png`: Distancia vs Rotación.
9. `reports/TotalWorkingYears_vs_attrition.png`: Años de Trabajo vs Rotación.
10. `reports/correlation_matrix.png`: Matriz de Correlación.
