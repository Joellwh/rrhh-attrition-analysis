"""
Script para la fase de Data Preparation (Preparación de los Datos).
Limpia y transforma el dataset IBM HR Analytics.
"""
import pandas as pd

import paths


def prepare_data():
    # 1. Cargar datos crudos
    raw_data_path = paths.require(paths.RAW_CSV)
    df = pd.read_csv(raw_data_path)

    print("=== Iniciando Data Preparation ===")
    print(f"Datos iniciales: {df.shape[0]} filas, {df.shape[1]} columnas")

    # 2. Eliminar variables constantes (no aportan información)
    constant_columns = ["EmployeeCount", "Over18", "StandardHours"]
    df = df.drop(columns=constant_columns)
    print(f"\nEliminadas variables constantes: {constant_columns}")
    print(f"Columnas restantes: {df.shape[1]}")

    # 3. Convertir variables categóricas a tipo 'category' (mejora rendimiento)
    categorical_columns = [
        "Attrition",
        "BusinessTravel",
        "Department",
        "EducationField",
        "Gender",
        "JobRole",
        "MaritalStatus",
        "OverTime",
    ]
    for col in categorical_columns:
        df[col] = df[col].astype("category")
    print(f"\nConvertidas variables categóricas a tipo 'category': {categorical_columns}")

    # 4. Codificar variable objetivo (Attrition: Yes=1, No=0)
    # Útil para análisis y modelado posteriores
    df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})
    print("\nVariable objetivo 'Attrition' codificada: Yes=1, No=0")

    # 5. Guardar datos limpios
    paths.ensure_dir(paths.PROCESSED_DIR)
    processed_data_path = paths.PROCESSED_CSV
    df.to_csv(processed_data_path, index=False)
    print(f"\nDatos limpios guardados en: {processed_data_path.relative_to(paths.ROOT)}")

    # 6. Mostrar resumen final
    print("\n=== Resumen Final de Data Preparation ===")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Variables numéricas: {len(df.select_dtypes(include=['int64', 'float64']).columns)}")
    print(f"Variables categóricas: {len(df.select_dtypes(include=['category']).columns)}")

    return df


if __name__ == "__main__":
    df_clean = prepare_data()
