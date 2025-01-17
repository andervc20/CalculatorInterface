
# Calculadora con Graficación

Esta es una calculadora interactiva construida con Python utilizando la biblioteca `tkinter` para la interfaz gráfica y `matplotlib` para la graficación de datos. La calculadora es capaz de realizar operaciones matemáticas básicas (suma, resta, multiplicación, división), eliminar caracteres, limpiar la pantalla y graficar puntos en un gráfico.

## Características

- **Operaciones Básicas**: La calculadora permite realizar operaciones aritméticas estándar como suma, resta, multiplicación, y división.
- **Botón de "Eliminar" (DEL)**: Permite borrar el último carácter ingresado.
- **Botón de "Limpiar" (C)**: Permite limpiar la pantalla de la calculadora.
- **Graficar Datos**: Permite ingresar pares de valores para los ejes X y Y, y luego muestra un gráfico de los puntos ingresados.
- **Tabla de Valores**: Después de graficar, se muestra una tabla con los valores de X y Y ingresados.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `tkinter` (para la interfaz gráfica)
- `matplotlib` (para la graficación de datos)

Puedes instalar `matplotlib` usando el siguiente comando:


pip install matplotlib


`tkinter` generalmente está incluido en las distribuciones estándar de Python, por lo que no debería ser necesario instalarlo por separado.

## Uso

1. **Abrir la Calculadora**: Al ejecutar el archivo, se abrirá una ventana con la interfaz de la calculadora.
2. **Realizar Operaciones**: Haz clic en los botones numéricos y de operaciones para realizar cálculos.
3. **Graficar Datos**: Haz clic en el botón "Graficar", y se te pedirá que ingreses los valores para los ejes X y Y en formato `X1,Y1,X2,Y2,...`. Asegúrate de ingresar un número par de valores.
4. **Ver Tabla de Valores**: Después de graficar, se mostrará una tabla con los valores de X y Y ingresados.
5. **Eliminar y Limpiar**: Usa los botones "DEL" para borrar el último carácter ingresado y "C" para limpiar toda la pantalla.

## Captura de Pantalla

![Calculadora](calculadora_screenshot.png)

## Estructura del Código

- **Interfaz gráfica**: Creada con `tkinter`, tiene un diseño con colores oscuros y botones con texto rojo.
- **Lógica de la calculadora**: Usando la función `eval()`, se evalúan las expresiones matemáticas ingresadas por el usuario.
- **Graficación**: Utiliza `matplotlib` para graficar los valores ingresados en los ejes X y Y, con una visualización clara y etiquetada.
- **Tabla de valores**: Al graficar los puntos, se genera una ventana adicional con una tabla que muestra los valores ingresados para X y Y.

## Cómo Ejecutar

1. Clona o descarga el repositorio en tu computadora.
2. Asegúrate de tener Python 3.x instalado.
3. Ejecuta el archivo Python:

```bash
python calculadora.py
```

La calculadora se abrirá y estará lista para usar.

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacer un *fork* del repositorio y enviar un *pull request* con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

```

### Descripción de los componentes:

- **Interfaz gráfica**: Utiliza `tkinter` para la interfaz de usuario, con un diseño oscuro y botones con texto rojo.
- **Operaciones matemáticas**: Se implementan utilizando la función `eval()` para evaluar expresiones aritméticas.
- **Graficación**: Al hacer clic en el botón "Graficar", se utilizan los datos ingresados para graficar los puntos usando `matplotlib`.
- **Tabla de valores**: Después de graficar, se crea una ventana secundaria que muestra una tabla con los valores de X y Y ingresados, utilizando `ttk.Treeview`.

Este README proporciona una visión general clara de cómo funciona la calculadora, cómo usarla, y cómo configurar el entorno para ejecutarla.
