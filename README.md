# Sistema de Evaluación

## Reto
Crea un módulo para un sistema de evaluación educativo que muestre una estructura de preguntas con respuesta de selección múltiple y al final muestre el resultado de cantidad de respuestas correctas y cantidad de respuestas equivocadas, teniendo en cuenta las siguientes condiciones:
* Cada pregunta tiene 4 opciones de respuesta en la cual una es correcta y tres son erradas.
* A medida que pasa entre las preguntas se van acumulando los resultados correctos.
* Cada evaluación debe tener mínimo 5 preguntas.
* Para cargar las preguntas y opciones de respuesta de las evaluaciones se debe contar con una API local para realizar su lectura y visualización.

## Entregable

[API publicado en SwaggerHub](https://app.swaggerhub.com/apis-docs/davidcuy6/EvaluationSystemAPI)

Se desarollo una API utilizando serverless framework y se publicó en AWS utilizando los siguientes servicios:
* AWS Lambda
* AWS API Gateway
* AWS RDS con base de datos de MySQL

La aplicación se puede testear utilizando el enlace de SwaggerHub, y se encontrarán múltiples endpoints para CRUDS de modelos de datos, además de un endpoint extra para mostrar los resultados de las respuesta de la persona que resuelva el cuestionario. El diagrama de flujo de cómo se utilizaría esta API (para implementación de frontend tal vez) se muestra acontinuación.

![Diagrama de Flujo](documentation/api/Diagrama-de-flujo.png)

Para más información de cómo ejecutar localmente el repositorio da click [aquí](code/evaluation-system-be/README.md).

## Modelo entidad relación
De igual manera los modelos de datos basados para la constracción de la solución se muestran acontinuación:
![ERD](documentation/database/ERD.png)


```
sls plugin install -n serverless-python-requirements
npm i -D serverless-dotenv-plugin
npm install serverless-offline --save-dev
```