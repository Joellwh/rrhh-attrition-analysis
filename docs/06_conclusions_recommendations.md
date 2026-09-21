# Conclusiones y Recomendaciones de Negocio

## 1. Conclusiones
A partir del análisis de datos del dataset IBM HR Analytics Employee Attrition & Performance, se identificaron los siguientes factores clave que influyen en la rotación de empleados:

1. **Horas Extras**: Los empleados que hacen horas extras tienen una probabilidad significativamente mayor de rotar (30.53% vs 10.44%).
2. **Ingreso Mensual**: Los empleados con menores ingresos tienden a abandonar la empresa con mayor frecuencia (promedio $4,787 vs $6,832).
3. **Distancia del Hogar**: Los empleados que viven más lejos del trabajo tienen mayor riesgo de rotación (promedio 10.63 km vs 8.92 km).
4. **Edad**: Los empleados más jóvenes (promedio 33.6 años vs 37.6 años) rotan más que los de mayor edad.
5. **Antigüedad en la Empresa**: Los empleados con menos de 2 años en la empresa tienen una tasa de rotación muy alta (34.88%).
6. **Equilibrio Vida-Trabajo**: Los empleados con nivel 1 de equilibrio vida-trabajo tienen la mayor tasa de rotación (31.25%).
7. **Satisfacción con el Ambiente**: Los empleados con nivel 1 de satisfacción con el ambiente tienen la mayor tasa de rotación (25.35%).
8. **Satisfacción Laboral**: Los empleados con nivel 1 de satisfacción laboral tienen una tasa de rotación de 22.84%.
9. **Relación con el Manager**: Los empleados con menos de 2 años con su manager actual tienen una tasa de rotación del 28.32%.
10. **Promociones**: Los empleados promovidos dentro del último año (`YearsSinceLastPromotion = 0`) presentan la mayor tasa de rotación del corte (18.93%), frente al 14.29% del resto. **Este resultado no debe leerse como que promover aumenta la rotación**: ese grupo tiene la mitad de antigüedad que el resto (4.4 vs 8.7 años promedio) y menos experiencia total (9.4 vs 12.5 años), por lo que el efecto está confundido con el de la conclusión 5 (los empleados nuevos rotan más). El dataset no permite identificar a los empleados que nunca fueron promovidos.
11. **Rol de Trabajo**: Sales Representative (39.76%) y Laboratory Technician (23.94%) son los roles con mayor rotación.
12. **Departamento**: El departamento de Ventas tiene la mayor tasa de rotación (20.63%).
13. **Involucramiento Laboral**: Los empleados que rotaron tienen un promedio menor de involucramiento (2.52 vs 2.77).

---

## 2. Recomendaciones de Negocio
Basadas en los hallazgos del análisis, se proponen las siguientes recomendaciones para reducir la rotación de empleados:

### 2.1 Reducir Horas Extras y Mejorar Equilibrio Vida-Trabajo
- Implementar políticas para limitar las horas extras obligatorias.
- Evaluar la carga de trabajo de los equipos y contratar personal adicional si es necesario.
- Ofrecer compensaciones adicionales o días de descanso compensatorios por horas extras trabajadas.
- Realizar encuestas periódicas para medir y mejorar el equilibrio vida-trabajo de los empleados.

### 2.2 Mejorar la Política Salarial y de Promociones
- Realizar un estudio de mercado para asegurar que los salarios sean competitivos.
- Implementar programas de bonos o incentivos por desempeño.
- Revisar los rangos salariales para los roles con mayor rotación (Sales Representative, Laboratory Technician).
- Establecer procesos claros de promoción y reconocimiento para mantener a los empleados motivados. *(Buena práctica general: los datos disponibles no permiten medir el efecto de la falta de promoción sobre la rotación — ver conclusión 10.)*

### 2.3 Ayudar con la Distancia del Hogar y Retener a Empleados Nuevos
- Ofrecer opciones de trabajo híbrido o remoto cuando sea posible.
- Proporcionar subsidios de transporte o estacionamiento.
- Considerar la ubicación de la empresa al contratar nuevos empleados.
- Implementar programas de mentoría y mejorar el onboarding para integrar rápidamente a los nuevos empleados.
- Focalizar en los primeros 2 años de los empleados, ya que es el período con mayor riesgo de rotación.

### 2.4 Mejorar la Satisfacción Laboral y el Ambiente de Trabajo
- Realizar encuestas periódicas de satisfacción laboral y de ambiente para identificar problemas.
- Implementar acciones correctivas basadas en los resultados de las encuestas.
- Fomentar una cultura de respeto y colaboración en todos los equipos.

### 2.5 Mejorar la Relación con los Managers
- Capacitar a los managers en liderazgo y gestión de equipos.
- Fomentar la comunicación regular entre managers y colaboradores.
- Establecer programas de seguimiento para los empleados con managers nuevos.

### 2.6 Focalizar en Roles y Departamentos con Mayor Rotación
- Realizar análisis específicos para el departamento de Ventas y los roles de Sales Representative y Laboratory Technician.
- Identificar problemas específicos en estos equipos y abordarlos.
- Ofrecer oportunidades de desarrollo y crecimiento en estos roles.

---

## 3. Próximos Pasos
1. Implementar las recomendaciones priorizadas (comenzar con reducir horas extras, mejorar salarios y equilibrio vida-trabajo).
2. Monitorear la tasa de rotación mensualmente para evaluar el impacto de las medidas.
3. Realizar encuestas periódicas de satisfacción laboral para medir el progreso.
4. Actualizar el dashboard de Power BI con datos nuevos para seguimiento continuo.
