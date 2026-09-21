# Diccionario de Datos - IBM HR Analytics Employee Attrition & Performance

## Información General
- **Fuente**: Dataset público de IBM
- **Filas**: 1470
- **Columnas**: 35

> Archivo generado automáticamente por `src/explore_data.py`.
> Las descripciones y escalas provienen del catálogo `VARIABLE_CATALOG`
> definido en ese script: **editá el catálogo, no este archivo**.

## Descripción de Variables

| Variable | Tipo de Dato | Valores Únicos | Descripción | Escala / Valores posibles |
|----------|--------------|----------------|-------------|---------------------------|
| Age | int64 | 43 | Edad del empleado. | Continua: 18 a 60 años |
| Attrition | str | 2 | Variable objetivo. Indica si el empleado dejó la empresa. | Yes = se fue / No = permanece |
| BusinessTravel | str | 3 | Frecuencia de viajes por trabajo. | Non-Travel / Travel_Rarely / Travel_Frequently |
| DailyRate | int64 | 886 | Tarifa diaria facturable asignada al empleado. Métrica interna de IBM, no es el salario. | Continua: 102 a 1499 |
| Department | str | 3 | Departamento al que pertenece. | Human Resources / Research & Development / Sales |
| DistanceFromHome | int64 | 29 | Distancia entre el domicilio y el lugar de trabajo. | Continua: 1 a 29 (unidad no especificada por IBM) |
| Education | int64 | 5 | Nivel educativo alcanzado. | Ordinal 1-5: 1=Below College, 2=College, 3=Bachelor, 4=Master, 5=Doctor |
| EducationField | str | 6 | Área de formación académica. | 6 categorías: Life Sciences, Medical, Marketing, Technical Degree, Human Resources, Other |
| EmployeeCount | int64 | 1 | Contador heredado del sistema de origen. Constante. | Siempre 1 — se elimina en data_preparation.py |
| EmployeeNumber | int64 | 1470 | Identificador único del empleado. | ID secuencial — excluir de todo análisis estadístico |
| EnvironmentSatisfaction | int64 | 4 | Satisfacción con el ambiente de trabajo. | Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High |
| Gender | str | 2 | Género del empleado. | Female / Male |
| HourlyRate | int64 | 71 | Tarifa horaria asignada. Métrica interna de IBM, no es el salario. | Continua: 30 a 100 |
| JobInvolvement | int64 | 4 | Nivel de involucramiento con el puesto. | Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High |
| JobLevel | int64 | 5 | Nivel jerárquico del puesto. | Ordinal 1-5 (1 = más bajo) |
| JobRole | str | 9 | Rol o puesto específico. | 9 categorías (ver tabla de frecuencias) |
| JobSatisfaction | int64 | 4 | Satisfacción con el puesto de trabajo. | Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High |
| MaritalStatus | str | 3 | Estado civil. | Single / Married / Divorced |
| MonthlyIncome | int64 | 1349 | Ingreso mensual real del empleado. Es la variable salarial válida para el análisis. | Continua: 1.009 a 19.999 |
| MonthlyRate | int64 | 1427 | Tarifa mensual del sistema de origen. Métrica interna de IBM, no es el salario. | Continua: 2.094 a 26.999 |
| NumCompaniesWorked | int64 | 10 | Cantidad de empresas en las que trabajó antes. | Continua: 0 a 9 |
| Over18 | str | 1 | Indica si el empleado es mayor de 18 años. Constante. | Siempre 'Y' — se elimina en data_preparation.py |
| OverTime | str | 2 | Indica si el empleado realiza horas extras. | Yes / No |
| PercentSalaryHike | int64 | 15 | Porcentaje del último aumento salarial. | Continua: 11% a 25% |
| PerformanceRating | int64 | 2 | Calificación de desempeño. | Ordinal 1-4 en teoría, pero en los datos SOLO aparecen 3=Excellent y 4=Outstanding |
| RelationshipSatisfaction | int64 | 4 | Satisfacción con las relaciones interpersonales en el trabajo. | Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High |
| StandardHours | int64 | 1 | Horas estándar de trabajo. Constante. | Siempre 80 — se elimina en data_preparation.py |
| StockOptionLevel | int64 | 4 | Nivel de opciones sobre acciones otorgadas. | Ordinal 0-3 (0 = sin opciones) |
| TotalWorkingYears | int64 | 40 | Años totales de experiencia laboral. | Continua: 0 a 40 |
| TrainingTimesLastYear | int64 | 7 | Cantidad de capacitaciones recibidas el año pasado. | Continua: 0 a 6 |
| WorkLifeBalance | int64 | 4 | Equilibrio entre vida personal y trabajo. | Ordinal 1-4: 1=Bad, 2=Good, 3=Better, 4=Best |
| YearsAtCompany | int64 | 37 | Años de antigüedad en la empresa. | Continua: 0 a 40 |
| YearsInCurrentRole | int64 | 19 | Años en el rol actual. | Continua: 0 a 18 |
| YearsSinceLastPromotion | int64 | 16 | Años transcurridos desde la última promoción. | Continua: 0 a 15. OJO: 0 = promovido en el último año, NO 'nunca promovido' |
| YearsWithCurrManager | int64 | 18 | Años trabajando con el manager actual. | Continua: 0 a 17 |

## Escalas Ordinales (Likert)

Estas variables son **texto codificado como número**. En cualquier gráfico o dashboard
hay que mostrar la etiqueta, no el entero: un eje que dice `1, 2, 3, 4` no comunica
si 1 es bueno o malo. En Power BI conviene crear una tabla de dimensión por escala.

### Education
- **Escala**: `1` = Below College · `2` = College · `3` = Bachelor · `4` = Master · `5` = Doctor
- **Valores presentes en los datos**: [1, 2, 3, 4, 5]

### EnvironmentSatisfaction
- **Escala**: `1` = Low · `2` = Medium · `3` = High · `4` = Very High
- **Valores presentes en los datos**: [1, 2, 3, 4]

### JobInvolvement
- **Escala**: `1` = Low · `2` = Medium · `3` = High · `4` = Very High
- **Valores presentes en los datos**: [1, 2, 3, 4]

### JobSatisfaction
- **Escala**: `1` = Low · `2` = Medium · `3` = High · `4` = Very High
- **Valores presentes en los datos**: [1, 2, 3, 4]

### PerformanceRating
- **Escala**: `1` = Low · `2` = Good · `3` = Excellent · `4` = Outstanding
- **Valores presentes en los datos**: [3, 4]
- ⚠️ **Niveles nunca observados**: `1` (Low), `2` (Good). No asumir que la escala está completa al construir filtros o ejes.

### RelationshipSatisfaction
- **Escala**: `1` = Low · `2` = Medium · `3` = High · `4` = Very High
- **Valores presentes en los datos**: [1, 2, 3, 4]

### WorkLifeBalance
- **Escala**: `1` = Bad · `2` = Good · `3` = Better · `4` = Best
- **Valores presentes en los datos**: [1, 2, 3, 4]

## Variables Constantes

Se eliminan en `src/data_preparation.py` porque no aportan información.

- **EmployeeCount**: Valor único = `1`
- **Over18**: Valor único = `Y`
- **StandardHours**: Valor único = `80`
