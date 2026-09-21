"""
Script para ejecutar el Análisis Exploratorio de Datos (EDA) y generar visualizaciones.
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo (escribir archivos directamente
import matplotlib.pyplot as plt
import seaborn as sns

import paths


def run_eda():
    # Configurar estilo de gráficos
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = (12, 6)

    # Crear directorio de reports si no existe
    reports = paths.ensure_dir(paths.REPORTS_DIR)

    # Cargar datos limpios
    df = pd.read_csv(paths.require(paths.PROCESSED_CSV))

    print("=== Iniciando Análisis Exploratorio de Datos (EDA) ===")

    # 1. Análisis de la variable objetivo (Attrition)
    print("\n1. Análisis de Attrition:")
    attrition_counts = df["Attrition"].value_counts()
    attrition_percent = df["Attrition"].value_counts(normalize=True) * 100
    print(f"Total empleados: {len(df)}")
    print(f"No (permanece): {attrition_counts[0]} ({attrition_percent[0]:.1f}%)")
    print(f"Yes (se va): {attrition_counts[1]} ({attrition_percent[1]:.1f}%)")

    plt.figure(figsize=(8, 5))
    sns.countplot(x="Attrition", data=df, palette="Set2")
    plt.title("Distribución de Rotación de Empleados (Attrition)")
    plt.xlabel("Attrition (0 = No, 1 = Yes)")
    plt.ylabel("Número de Empleados")
    plt.savefig(reports / "attrition_distribution.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Gráfico guardado: reports/attrition_distribution.png")

    # 2. Función para graficar variables categóricas vs Attrition
    def plot_categorical_vs_attrition(col, title):
        plt.figure(figsize=(12, 6))
        ax = sns.countplot(x=col, hue="Attrition", data=df, palette="Set2")
        plt.title(title)
        plt.xlabel(col)
        plt.ylabel("Número de Empleados")
        plt.legend(title="Attrition", labels=["No", "Yes"])
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(reports / f"{col}_vs_attrition.png", dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Gráfico guardado: reports/{col}_vs_attrition.png")

    # Graficar variables categóricas clave
    plot_categorical_vs_attrition("Department", "Rotación por Departamento")
    plot_categorical_vs_attrition("JobRole", "Rotación por Rol de Trabajo")
    plot_categorical_vs_attrition("OverTime", "Rotación por Horas Extras")
    plot_categorical_vs_attrition("MaritalStatus", "Rotación por Estado Civil")

    # 3. Función para graficar variables numéricas vs Attrition
    def plot_numerical_vs_attrition(col, title):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="Attrition", y=col, data=df, palette="Set2")
        plt.title(title)
        plt.xlabel("Attrition (0 = No, 1 = Yes)")
        plt.ylabel(col)
        plt.tight_layout()
        plt.savefig(reports / f"{col}_vs_attrition.png", dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Gráfico guardado: reports/{col}_vs_attrition.png")

    # Graficar variables numéricas clave
    plot_numerical_vs_attrition("Age", "Distribución de Edad por Rotación")
    plot_numerical_vs_attrition("MonthlyIncome", "Ingreso Mensual por Rotación")
    plot_numerical_vs_attrition("DistanceFromHome", "Distancia del Hogar por Rotación")
    plot_numerical_vs_attrition("TotalWorkingYears", "Años Totales de Trabajo por Rotación")

    # 4. Matriz de correlación
    print("\n2. Generando matriz de correlación:")
    # Excluimos identificadores: son números pero no tienen significado estadístico.
    # EmployeeNumber es un ID secuencial; su correlación con Attrition es -0.01 (ruido puro)
    # y solo añade una fila/columna ilegible al heatmap.
    ID_COLUMNS = ["EmployeeNumber"]
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    numeric_df = numeric_df.drop(columns=ID_COLUMNS, errors="ignore")
    print(f"   Variables incluidas en la correlación: {numeric_df.shape[1]} "
          f"(excluidos identificadores: {ID_COLUMNS})")
    correlation_matrix = numeric_df.corr()
    plt.figure(figsize=(16, 12))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Matriz de Correlación de Variables Numéricas")
    plt.tight_layout()
    plt.savefig(reports / "correlation_matrix.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Gráfico guardado: reports/correlation_matrix.png")

    print("\n=== EDA completado! ===")


if __name__ == "__main__":
    run_eda()
