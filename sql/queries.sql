-- Consultas SQL para analizar el dataset IBM HR Analytics Employee Attrition & Performance
-- Estas consultas se pueden ejecutar en una base de datos SQLite (o compatible)

-- 1. Tasa de rotación general
SELECT
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees;

-- 2. Tasa de rotación por departamento
SELECT
    Department,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY Department
ORDER BY tasa_rotacion_porcentaje DESC;

-- 3. Tasa de rotación por rol de trabajo
SELECT
    JobRole,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY JobRole
ORDER BY tasa_rotacion_porcentaje DESC;

-- 4. Tasa de rotación por horas extras
SELECT
    OverTime,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY OverTime;

-- 5. Promedio de ingreso mensual por estado de rotación
SELECT
    CASE WHEN Attrition = 1 THEN 'Sí' ELSE 'No' END AS rotacion,
    COUNT(*) AS total_empleados,
    ROUND(AVG(MonthlyIncome), 2) AS promedio_ingreso_mensual
FROM employees
GROUP BY Attrition;

-- 6. Promedio de edad por estado de rotación
SELECT
    CASE WHEN Attrition = 1 THEN 'Sí' ELSE 'No' END AS rotacion,
    COUNT(*) AS total_empleados,
    ROUND(AVG(Age), 2) AS promedio_edad
FROM employees
GROUP BY Attrition;

-- 7. Promedio de distancia del hogar por estado de rotación
SELECT
    CASE WHEN Attrition = 1 THEN 'Sí' ELSE 'No' END AS rotacion,
    COUNT(*) AS total_empleados,
    ROUND(AVG(DistanceFromHome), 2) AS promedio_distancia_hogar
FROM employees
GROUP BY Attrition;

-- 8. Tasa de rotación por nivel de satisfacción laboral (JobSatisfaction)
SELECT
    JobSatisfaction,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY JobSatisfaction
ORDER BY tasa_rotacion_porcentaje DESC;

-- 9. Tasa de rotación por nivel de satisfacción con el ambiente (EnvironmentSatisfaction)
SELECT
    EnvironmentSatisfaction,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY EnvironmentSatisfaction
ORDER BY tasa_rotacion_porcentaje DESC;

-- 10. Tasa de rotación por nivel de equilibrio vida-trabajo (WorkLifeBalance)
SELECT
    WorkLifeBalance,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY WorkLifeBalance
ORDER BY tasa_rotacion_porcentaje DESC;

-- 11. Tasa de rotación por años en la empresa (YearsAtCompany)
SELECT
    CASE
        WHEN YearsAtCompany < 2 THEN 'Menos de 2 años'
        WHEN YearsAtCompany BETWEEN 2 AND 5 THEN '2 a 5 años'
        WHEN YearsAtCompany BETWEEN 6 AND 10 THEN '6 a 10 años'
        ELSE 'Más de 10 años'
    END AS antiguedad_rango,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY antiguedad_rango
ORDER BY tasa_rotacion_porcentaje DESC;

-- 12. Tasa de rotación por años desde la última promoción (YearsSinceLastPromotion)
-- NOTA: el valor 0 significa "promovido dentro del último año" (581 empleados, 39.5%),
-- NO "nunca promovido". El dataset no contiene ninguna variable que permita saber
-- si un empleado nunca recibió una promoción.
SELECT
    CASE
        WHEN YearsSinceLastPromotion = 0 THEN 'Promovido en el último año'
        WHEN YearsSinceLastPromotion BETWEEN 1 AND 3 THEN '1 a 3 años'
        WHEN YearsSinceLastPromotion BETWEEN 4 AND 7 THEN '4 a 7 años'
        ELSE 'Más de 7 años'
    END AS ultima_promocion_rango,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY ultima_promocion_rango
ORDER BY tasa_rotacion_porcentaje DESC;

-- 13. Tasa de rotación por años con el manager actual (YearsWithCurrManager)
SELECT
    CASE
        WHEN YearsWithCurrManager < 2 THEN 'Menos de 2 años'
        WHEN YearsWithCurrManager BETWEEN 2 AND 5 THEN '2 a 5 años'
        ELSE 'Más de 5 años'
    END AS años_manager_rango,
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) AS empleados_rotados,
    ROUND((SUM(CASE WHEN Attrition = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS tasa_rotacion_porcentaje
FROM employees
GROUP BY años_manager_rango
ORDER BY tasa_rotacion_porcentaje DESC;

-- 14. Promedio de JobInvolvement por estado de rotación
SELECT
    CASE WHEN Attrition = 1 THEN 'Sí' ELSE 'No' END AS rotacion,
    COUNT(*) AS total_empleados,
    ROUND(AVG(JobInvolvement), 2) AS promedio_involucramiento_laboral
FROM employees
GROUP BY Attrition;
