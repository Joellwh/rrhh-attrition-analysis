"""
Script para ejecutar consultas SQL en el dataset IBM HR Analytics usando SQLite.
"""
import sqlite3
import sys

import pandas as pd

import paths


def run_sql_queries():
    # 1. Cargar datos limpios
    df = pd.read_csv(paths.require(paths.PROCESSED_CSV))

    # 2. Conectar a base de datos SQLite (en memoria)
    conn = sqlite3.connect(":memory:")

    try:
        # 3. Guardar DataFrame en la base de datos como tabla 'employees'
        df.to_sql("employees", conn, index=False, if_exists="replace")

        # 4. Leer consultas SQL desde el archivo
        sql_content = paths.require(paths.QUERIES_SQL).read_text(encoding="utf-8")

        # 5. Dividir consultas (separadas por ';') y ejecutar cada una
        queries = [q.strip() for q in sql_content.split(";") if q.strip()]

        print("=== Ejecutando Consultas SQL ===")
        fallidas = []
        for i, query in enumerate(queries, 1):
            print(f"\n--- Consulta {i} ---")
            print(query)
            try:
                result = pd.read_sql_query(query, conn)
            # Excepciones nombradas: un error de SQL es lo unico que esperamos
            # acá. Cualquier otra cosa (un bug nuestro) debe propagarse.
            except (sqlite3.Error, pd.errors.DatabaseError) as e:
                print(f"ERROR en la consulta {i}: {e}")
                fallidas.append(i)
            else:
                print("\nResultado:")
                print(result)
    finally:
        # 6. Cerrar conexión pase lo que pase
        conn.close()

    # 7. Si alguna consulta falló, terminar con error. Antes se imprimía el
    #    problema y el script salía en exito, asi que el CI nunca se enteraba.
    if fallidas:
        raise RuntimeError(
            f"{len(fallidas)} de {len(queries)} consultas fallaron: {fallidas}. "
            f"Revisá {paths.QUERIES_SQL.relative_to(paths.ROOT)}"
        )

    print(f"\n=== {len(queries)} consultas ejecutadas sin errores ===")


if __name__ == "__main__":
    try:
        run_sql_queries()
    except (FileNotFoundError, RuntimeError) as e:
        print(f"\n{e}", file=sys.stderr)
        sys.exit(1)
