"""
Script para exploración inicial del dataset y generación de diccionario de datos (Fase Data Understanding de CRISP-DM)
"""
import pandas as pd

import paths

# ---------------------------------------------------------------------------
# Catálogo de metadatos de las variables.
# Cada entrada es: nombre_columna -> (descripción, escala / valores posibles)
#
# Este catálogo se mantiene a mano y es la fuente de verdad de la semántica del
# dataset. El diccionario de datos se genera combinándolo con las estadísticas
# calculadas sobre el CSV, de modo que regenerar el archivo NO borra estas
# descripciones (antes el script las sobrescribía con simples valores de ejemplo).
# ---------------------------------------------------------------------------
VARIABLE_CATALOG = {
    "Age": ("Edad del empleado.", "Continua: 18 a 60 años"),
    "Attrition": ("Variable objetivo. Indica si el empleado dejó la empresa.", "Yes = se fue / No = permanece"),
    "BusinessTravel": ("Frecuencia de viajes por trabajo.", "Non-Travel / Travel_Rarely / Travel_Frequently"),
    "DailyRate": ("Tarifa diaria facturable asignada al empleado. Métrica interna de IBM, no es el salario.", "Continua: 102 a 1499"),
    "Department": ("Departamento al que pertenece.", "Human Resources / Research & Development / Sales"),
    "DistanceFromHome": ("Distancia entre el domicilio y el lugar de trabajo.", "Continua: 1 a 29 (unidad no especificada por IBM)"),
    "Education": ("Nivel educativo alcanzado.", "Ordinal 1-5: 1=Below College, 2=College, 3=Bachelor, 4=Master, 5=Doctor"),
    "EducationField": ("Área de formación académica.", "6 categorías: Life Sciences, Medical, Marketing, Technical Degree, Human Resources, Other"),
    "EmployeeCount": ("Contador heredado del sistema de origen. Constante.", "Siempre 1 — se elimina en data_preparation.py"),
    "EmployeeNumber": ("Identificador único del empleado.", "ID secuencial — excluir de todo análisis estadístico"),
    "EnvironmentSatisfaction": ("Satisfacción con el ambiente de trabajo.", "Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High"),
    "Gender": ("Género del empleado.", "Female / Male"),
    "HourlyRate": ("Tarifa horaria asignada. Métrica interna de IBM, no es el salario.", "Continua: 30 a 100"),
    "JobInvolvement": ("Nivel de involucramiento con el puesto.", "Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High"),
    "JobLevel": ("Nivel jerárquico del puesto.", "Ordinal 1-5 (1 = más bajo)"),
    "JobRole": ("Rol o puesto específico.", "9 categorías (ver tabla de frecuencias)"),
    "JobSatisfaction": ("Satisfacción con el puesto de trabajo.", "Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High"),
    "MaritalStatus": ("Estado civil.", "Single / Married / Divorced"),
    "MonthlyIncome": ("Ingreso mensual real del empleado. Es la variable salarial válida para el análisis.", "Continua: 1.009 a 19.999"),
    "MonthlyRate": ("Tarifa mensual del sistema de origen. Métrica interna de IBM, no es el salario.", "Continua: 2.094 a 26.999"),
    "NumCompaniesWorked": ("Cantidad de empresas en las que trabajó antes.", "Continua: 0 a 9"),
    "Over18": ("Indica si el empleado es mayor de 18 años. Constante.", "Siempre 'Y' — se elimina en data_preparation.py"),
    "OverTime": ("Indica si el empleado realiza horas extras.", "Yes / No"),
    "PercentSalaryHike": ("Porcentaje del último aumento salarial.", "Continua: 11% a 25%"),
    "PerformanceRating": ("Calificación de desempeño.", "Ordinal 1-4 en teoría, pero en los datos SOLO aparecen 3=Excellent y 4=Outstanding"),
    "RelationshipSatisfaction": ("Satisfacción con las relaciones interpersonales en el trabajo.", "Ordinal 1-4: 1=Low, 2=Medium, 3=High, 4=Very High"),
    "StandardHours": ("Horas estándar de trabajo. Constante.", "Siempre 80 — se elimina en data_preparation.py"),
    "StockOptionLevel": ("Nivel de opciones sobre acciones otorgadas.", "Ordinal 0-3 (0 = sin opciones)"),
    "TotalWorkingYears": ("Años totales de experiencia laboral.", "Continua: 0 a 40"),
    "TrainingTimesLastYear": ("Cantidad de capacitaciones recibidas el año pasado.", "Continua: 0 a 6"),
    "WorkLifeBalance": ("Equilibrio entre vida personal y trabajo.", "Ordinal 1-4: 1=Bad, 2=Good, 3=Better, 4=Best"),
    "YearsAtCompany": ("Años de antigüedad en la empresa.", "Continua: 0 a 40"),
    "YearsInCurrentRole": ("Años en el rol actual.", "Continua: 0 a 18"),
    "YearsSinceLastPromotion": ("Años transcurridos desde la última promoción.", "Continua: 0 a 15. OJO: 0 = promovido en el último año, NO 'nunca promovido'"),
    "YearsWithCurrManager": ("Años trabajando con el manager actual.", "Continua: 0 a 17"),
}

# Variables ordinales (escalas tipo Likert) codificadas como enteros.
# Se documentan aparte porque en un dashboard hay que mostrar la etiqueta, no el número.
LIKERT_SCALES = {
    "Education": {1: "Below College", 2: "College", 3: "Bachelor", 4: "Master", 5: "Doctor"},
    "EnvironmentSatisfaction": {1: "Low", 2: "Medium", 3: "High", 4: "Very High"},
    "JobInvolvement": {1: "Low", 2: "Medium", 3: "High", 4: "Very High"},
    "JobSatisfaction": {1: "Low", 2: "Medium", 3: "High", 4: "Very High"},
    "PerformanceRating": {1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"},
    "RelationshipSatisfaction": {1: "Low", 2: "Medium", 3: "High", 4: "Very High"},
    "WorkLifeBalance": {1: "Bad", 2: "Good", 3: "Better", 4: "Best"},
}


def explore_dataset():
    # -------------------------------
    # 1. Leer el dataset CSV
    # -------------------------------
    # La ruta sale de src/paths.py: no depende del directorio desde el que corras esto
    file_path = paths.require(paths.RAW_CSV)
    # Leemos el CSV con pandas
    df = pd.read_csv(file_path)
    
    # Imprimimos encabezado para organizar la salida
    print("=" * 100)
    print("FASE DE DATA UNDERSTANDING - EXPLORACIÓN INICIAL DEL DATASET")
    print("=" * 100)
    
    # -------------------------------
    # 2. Mostrar cantidad de filas y columnas
    # -------------------------------
    print("\n1. DIMENSIONES DEL DATASET:")
    print(f"   - Número de filas (empleados): {df.shape[0]}")
    print(f"   - Número de columnas (variables): {df.shape[1]}")
    
    # -------------------------------
    # 3. Mostrar tipos de datos por columna
    # -------------------------------
    print("\n2. TIPOS DE DATOS POR COLUMNA:")
    print(df.dtypes)
    
    # -------------------------------
    # 4. Mostrar valores nulos/faltantes por columna
    # -------------------------------
    print("\n3. VALORES NULOS POR COLUMNA:")
    null_counts = df.isnull().sum()
    # Mostramos solo columnas con valores nulos (si las hay), o todas si no
    if null_counts.sum() > 0:
        print(null_counts[null_counts > 0])
    else:
        print("   No hay valores nulos en el dataset")
    
    # -------------------------------
    # 5. Mostrar duplicados
    # -------------------------------
    print("\n4. REGISTROS DUPLICADOS:")
    duplicate_count = df.duplicated().sum()
    print(f"   - Número de filas duplicadas: {duplicate_count}")
    if duplicate_count > 0:
        print("\n   Filas duplicadas:")
        print(df[df.duplicated()])
    
    # -------------------------------
    # 6. Mostrar cantidad de valores únicos por columna
    # -------------------------------
    print("\n5. CANTIDAD DE VALORES ÚNICOS POR COLUMNA:")
    unique_counts = df.nunique().sort_values(ascending=True)
    print(unique_counts)
    
    # -------------------------------
    # 7. Generar estadísticas descriptivas
    # -------------------------------
    print("\n6. ESTADÍSTICAS DESCRIPTIVAS (VARIABLES NUMÉRICAS):")
    print(df.describe())
    
    # -------------------------------
    # 8. Identificar variables numéricas y categóricas
    # -------------------------------
    print("\n7. CLASIFICACIÓN DE VARIABLES:")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    print(f"   - Variables numéricas ({len(numeric_cols)}): {numeric_cols}")
    print(f"\n   - Variables categóricas ({len(categorical_cols)}): {categorical_cols}")
    
    # -------------------------------
    # 9. Detectar columnas constantes (mismo valor en todas las filas)
    # -------------------------------
    print("\n8. COLUMNAS CONSTANTES:")
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    if constant_cols:
        print(f"   - Columnas con un solo valor único: {constant_cols}")
        for col in constant_cols:
            print(f"     - {col}: {df[col].iloc[0]}")
    else:
        print("   ✅ No hay columnas constantes")
    
    # -------------------------------
    # 10. Guardar diccionario de datos inicial en docs/data_dictionary.md
    # -------------------------------
    print("\n9. GENERANDO DICCIONARIO DE DATOS...")
    # Creamos la carpeta docs si no existe
    paths.ensure_dir(paths.DOCS_DIR)
    
    # Construimos el contenido del diccionario
    data_dict_content = "# Diccionario de Datos - IBM HR Analytics Employee Attrition & Performance\n\n"
    data_dict_content += "## Información General\n"
    data_dict_content += f"- **Fuente**: Dataset público de IBM\n"
    data_dict_content += f"- **Filas**: {df.shape[0]}\n"
    data_dict_content += f"- **Columnas**: {df.shape[1]}\n\n"
    data_dict_content += "> Archivo generado automáticamente por `src/explore_data.py`.\n"
    data_dict_content += "> Las descripciones y escalas provienen del catálogo `VARIABLE_CATALOG`\n"
    data_dict_content += "> definido en ese script: **editá el catálogo, no este archivo**.\n\n"
    data_dict_content += "## Descripción de Variables\n\n"
    data_dict_content += "| Variable | Tipo de Dato | Valores Únicos | Descripción | Escala / Valores posibles |\n"
    data_dict_content += "|----------|--------------|----------------|-------------|---------------------------|\n"

    # Avisamos si el catálogo quedó desactualizado respecto del CSV
    sin_documentar = [c for c in df.columns if c not in VARIABLE_CATALOG]
    if sin_documentar:
        print(f"   ⚠️  Columnas sin entrada en VARIABLE_CATALOG: {sin_documentar}")

    for col in df.columns:
        dtype = str(df[col].dtype)
        n_unique = df[col].nunique()
        descripcion, escala = VARIABLE_CATALOG.get(
            col, ("_Sin documentar — agregar a VARIABLE_CATALOG_", "—")
        )
        data_dict_content += f"| {col} | {dtype} | {n_unique} | {descripcion} | {escala} |\n"

    # -------------------------------
    # Sección de escalas ordinales (clave para etiquetar ejes en Power BI)
    # -------------------------------
    data_dict_content += "\n## Escalas Ordinales (Likert)\n\n"
    data_dict_content += (
        "Estas variables son **texto codificado como número**. En cualquier gráfico o dashboard\n"
        "hay que mostrar la etiqueta, no el entero: un eje que dice `1, 2, 3, 4` no comunica\n"
        "si 1 es bueno o malo. En Power BI conviene crear una tabla de dimensión por escala.\n\n"
    )
    for col, escala in LIKERT_SCALES.items():
        if col not in df.columns:
            continue
        presentes = sorted(df[col].unique().tolist())
        etiquetas = " · ".join(f"`{k}` = {v}" for k, v in escala.items())
        data_dict_content += f"### {col}\n"
        data_dict_content += f"- **Escala**: {etiquetas}\n"
        data_dict_content += f"- **Valores presentes en los datos**: {presentes}\n"
        faltantes = [k for k in escala if k not in presentes]
        if faltantes:
            faltantes_txt = ", ".join(f"`{k}` ({escala[k]})" for k in faltantes)
            data_dict_content += (
                f"- ⚠️ **Niveles nunca observados**: {faltantes_txt}. "
                "No asumir que la escala está completa al construir filtros o ejes.\n"
            )
        data_dict_content += "\n"

    # Agregamos sección de variables constantes
    if constant_cols:
        data_dict_content += "## Variables Constantes\n\n"
        data_dict_content += "Se eliminan en `src/data_preparation.py` porque no aportan información.\n\n"
        for col in constant_cols:
            data_dict_content += f"- **{col}**: Valor único = `{df[col].iloc[0]}`\n"

    # Guardamos el diccionario en un archivo Markdown
    dict_path = paths.DATA_DICTIONARY_MD
    with open(dict_path, "w", encoding="utf-8") as f:
        f.write(data_dict_content)
    
    print(f"   ✅ Diccionario de datos guardado exitosamente en: {dict_path}")
    
    return df

if __name__ == "__main__":
    df = explore_dataset()
