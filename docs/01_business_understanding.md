# Business Understanding (Comprensión del Negocio)

## 1. Contexto del Problema
**Empresa (Simulada)**: TechCorp Solutions  
**Sector**: Tecnología y Servicios Profesionales  

TechCorp Solutions ha experimentado un aumento significativo en la tasa de rotación voluntaria de empleados durante los últimos 18 meses. Este fenómeno genera impactos negativos en el negocio:
- Costos elevados en procesos de reclutamiento, selección y capacitación de nuevo personal
- Pérdida de conocimiento institucional y experiencia crítica
- Disminución en la productividad de los equipos durante los periodos de transición
- Impacto negativo en la moral y la cultura laboral del personal restante

Para abordar este problema, el equipo de RRHH requiere un análisis basado en datos para entender los factores que influyen en la rotación y tomar decisiones estratégicas.

---

## 2. Objetivos del Negocio
1. Reducir la tasa de rotación voluntaria de empleados en un plazo de 12 meses
2. Mejorar la retención de talento clave en la organización
3. Optimizar los recursos invertidos en procesos de contratación y capacitación
4. Fortalecer la cultura laboral y la satisfacción de los empleados

---

## 3. Objetivos del Análisis
1. Identificar los factores clave (demográficos, laborales, de satisfacción, etc.) que se correlacionan con la rotación de empleados
2. Cuantificar el impacto de cada factor en la probabilidad de rotación
3. Proporcionar recomendaciones de negocio accionables basadas en evidencia
4. Crear un dashboard interactivo para el monitoreo continuo de métricas de RRHH relacionadas con la rotación

---

## 4. Stakeholders
| Rol | Responsabilidad | Interés en el Proyecto |
|-----|-----------------|-------------------------|
| Director de RRHH | Líder del proyecto, toma de decisiones estratégicas | Alta |
| Gerentes de Área | Implementación de recomendaciones en sus equipos | Alta |
| Analistas de RRHH | Uso del dashboard y análisis para decisiones operativas | Alta |
| Director Financiero | Evaluación del impacto económico de las recomendaciones | Media |
| CEO | Revisión de resultados y aprobación de iniciativas | Media |

---

## 5. Preguntas de Negocio
1. ¿Cuál es la tasa de rotación general de la empresa?
2. ¿Qué departamentos, roles o niveles laborales tienen la mayor tasa de rotación?
3. ¿Existe una relación entre la satisfacción laboral/environmental y la probabilidad de rotación?
4. ¿Cómo impactan variables como salario, distancia al trabajo, horas extras en la rotación?
5. ¿Los empleados con ciertas características demográficas (edad, estado civil, educación) tienen mayor tendencia a rotar?
6. ¿Qué factores de desempeño y permanencia en la empresa se asocian con una mayor retención?

---

## 6. KPIs a Medir
| KPI | Definición | Frecuencia de Medición |
|-----|------------|-------------------------|
| Tasa de Rotación General | (Número de empleados que se fueron / Total de empleados) * 100 | Mensual |
| Tasa de Rotación por Departamento | Tasa de rotación desagregada por área | Mensual |
| Tiempo Medio de Permanencia | Promedio de meses que los empleados permanecen en la empresa | Trimestral |
| Costo por Contratación | Costo promedio de reclutar y capacitar un nuevo empleado | Trimestral |
| Índice de Satisfacción Laboral | Promedio de encuestas de satisfacción (si estuviera disponible, en este proyecto se usa la variable `JobSatisfaction` del dataset) | Trimestral |

---

## 7. Alcance del Proyecto
### Incluye:
- Análisis exploratorio de datos (EDA) completo del dataset IBM HR Analytics
- Identificación de factores de riesgo de rotación
- Consultas SQL para análisis agregados
- Visualizaciones de datos para comunicar hallazgos
- Dashboard interactivo en Power BI para monitoreo
- Recomendaciones de negocio basadas en datos

### No Incluye:
- Implementación de cambios operativos en la empresa TechCorp Solutions
- Integración con sistemas de RRHH en producción
- Despliegue de modelos predictivos en producción (solo desarrollo y validación de prototipos)
- Recolección de nuevos datos (solo se usa el dataset público proporcionado)

---

## 8. Supuestos
1. El dataset IBM HR Analytics Employee Attrition & Performance es representativo del contexto de TechCorp Solutions
2. La variable `Attrition` del dataset indica correctamente si un empleado abandonó la empresa voluntariamente
3. No hay errores significativos en la recolección de datos del dataset original
4. Los factores medidos en el dataset son relevantes para explicar la rotación en TechCorp Solutions

---

## 9. Riesgos
| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| El dataset no captura factores clave de rotación específicos de TechCorp | Alto | Media | Documentar claramente las limitaciones del dataset; recomendar recolección de datos adicionales |
| Las recomendaciones no son implementables por restricciones presupuestarias | Medio | Media | Priorizar recomendaciones por impacto y costo; involucrar stakeholders financieros tempranamente |
| Baja adopción del dashboard por parte del equipo de RRHH | Medio | Baja | Involucrar a RRHH en el diseño del dashboard; proporcionar capacitación |

---

## 10. Criterios de Éxito
1. **Negocio**: Reducción de la tasa de rotación en al menos un 15% en 12 meses (si las recomendaciones se implementan)
2. **Análisis**: Identificación de al menos 3 factores estadísticamente significativos asociados a la rotación
3. **Producto**: Dashboard adoptado y utilizado regularmente por el equipo de RRHH
4. **Documentación**: Proyecto completamente documentado y listo para ser compartido como caso de estudio profesional

---

## 11. Dataset Utilizado
**Nombre**: IBM HR Analytics Employee Attrition & Performance  
**Origen**: [Kaggle - IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
**Tipo**: Dataset público, anónimo y ficticio creado por IBM  
**Descripción**: Contiene 1470 registros de empleados con 35 variables, incluyendo información demográfica, satisfacción laboral, desempeño, salario y rotación (`Attrition`).
