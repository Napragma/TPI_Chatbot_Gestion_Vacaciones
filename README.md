# CHATBOT DE GESTIÓN DE VACACIONES - ÓPTICA

Este repositorio contiene el Trabajo Integrador desarrollado para la materia **Organización Empresarial** de la Tecnicatura Universitaria en Programación (TUP). El proyecto consiste en la conceptualización, modelado y simulación automatizada de un proceso administrativo crítico aplicando la metodología BPMN 2.0 y el lenguaje de programación Python.

## Diagnóstico y Caso de Negocio
El sistema fue diseñado específicamente para la PYME local **"Óptica Vivian Petcoff"**, la cual cuenta con una nómina de 9 empleados activos. El relevamiento inicial detectó la ausencia de un sistema centralizado y formal para la **Gestión de Vacaciones**, manejándose históricamente mediante anotaciones manuscritas y mensajes informales. Esto generaba problemas operativos como superposición de turnos en el local, errores de cálculo en los días de vacaciones pendientes.

La solución propuesta implementa un Asistente Virtual (Chatbot) que automatiza las validaciones de identidad, control de calendarios y auditoría de días disponibles en tiempo real, optimizando la comunicación interna y centralizando las decisiones en una consola comercial.

## Modelado del Proceso (BPMN 2.0)
El flujo del proceso administrativo está estructurado bajo dos andariveles de responsabilidad (Lanes) bien definidos:
*   **Andarivel del Empleado:** Maneja la interfaz de cara al usuario, la selección de opciones del menú y la carga de datos del formulario conversacional.
*   **Andarivel del Sistema / Bot:** Ejecuta las tareas de servicio automáticas (verificación de legajos, validación sintáctica de fechas y cálculo de disponibilidad) y las compuertas de control lógico.

*(Nota: El diagrama de procesos exportado en alta resolución se encuentra adjunto en la raíz del repositorio con el nombre `diagrama_bpmn_gestion_vacaciones.png`)*.

## Perspectiva Técnica y Arquitectura
El script fue programado de manera íntegra en **Python**, respetando el alcance académico actual del plan de estudios y aplicando las siguientes estructuras nativas:
*   **Persistencia de Datos:** Simulada de forma dinámica mediante una plantilla de diccionario de diccionarios corporativo (`empleados`) que lee y modifica la cantidad de días de vacaciones pendientes en tiempo real.
*   **Gestión de Estados (Máquina de Estados):** Implementada a través de un diccionario independiente (`estados_usuarios`) que registra secuencialmente en qué paso del proceso BPMN se encuentra el operario activo (ej: `"poniendo fecha de inicio"`, `"esperando autorizacion"`). Se descartó la sugerencia de ChatGPT de utilizar estructuras complejas como `Enum` para mantener la legibilidad y el alcance de la cursada.
*   **Estructura Procedimental:** Se unificó toda la lógica en un único script optimizado mediante funciones independientes para simular los carriles de Draw.io, simplificando la recomendación de Google AI Studio de separar el desarrollo en múltiples archivos independientes (.py).
*   **Robustez (Camino Infeliz):** Captura proactiva de excepciones de casteo y errores sintácticos mediante bloques estructurados `try/except ValueError` y métodos de cadena nativos (`.split()`, `.strip()`, `.lower()`), evitando interrupciones críticas en la terminal ante entradas de datos erróneas.

## Instrucciones de Ejecución
1. Descargue el archivo de código en su computadora.
2. Abra el archivo con Visual Studio Code (o el entorno de desarrollo que use).
3. Haga clic en el botón "Run" (Ejecutar/Play)
4. El chatbot se desplegará de forma automática en la terminal interna para iniciar la simulación.

### Datos de Prueba Precargados (Nómina de la Óptica)
Para auditar las validaciones dinámicas del sistema, puede utilizar los siguientes legajos de prueba configurados en la base de datos simulada:
*   **Legajo 1001:** Natalia Cócers (15 días de vacaciones pendientes)
*   **Legajo 1002:** Diego Perez (7 días de vacaciones pendientes)
*   **Legajo 1003:** Sofía Lucero (20 días de vacaciones pendientes)
