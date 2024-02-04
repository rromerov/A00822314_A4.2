# Actividad 4.2. Ejercicio de programación 1

## 1. [Compute statistics](compute_statistics.py)

Para ejecutar el script, se debe correr el siguiente comando en la terminal desde la ruta donde se encuentra el archivo `compute_statistics.py`:

```
python compute_statistics.py fileWithData.txt
```

Donde `fileWithData.txt` es el archivo con los datos a analizar.

El requerimento 4 pedía que el archivo se nombrará `computeStatistics.py`, pero para seguir la convención de nombrar los archivos con minúsculas y separar las palabras con guiones bajos, se nombró como `compute_statistics.py`, de acuerdo con el requerimiento 8 de que cumpla con PEP8, donde se menciona que se usará CamelCase si el proyecto en primera instancia fue creado con ese estilo de escritura en un principio, de lo contrario se debe usar Snake case.

El script hace el cálculo de la media, mediana, moda (si existe más de una moda se muestra "N/A"), varianza y desviación estándar de los datos contenidos en el archivo `fileWithData.txt`, adicionalmente se muestra el tiempo de ejecución del programa. Los resultados se imprimen en la terminal y en un archivo llamado `StatisticsResults.txt`.

## 2. [Converter](convert_numbers.py)

Para ejecutar el script, se debe correr el siguiente comando en la terminal desde la ruta donde se encuentra el archivo `convert_numbers.py`:

```
python convert_numbers.py fileWithData.txt
```

Donde `fileWithData.txt` es el archivo con los datos a analizar.

El requerimento 4 pedía que el archivo se nombrará `convertNumbers.py`, pero para seguir la convención de nombrar los archivos con minúsculas y separar las palabras con guiones bajos, se nombró como `convert_numbers.py`, de acuerdo con el requerimiento 8 de que cumpla con PEP8, donde se menciona que se usará CamelCase si el proyecto en primera instancia fue creado con ese estilo de escritura en un principio, de lo contrario se debe usar Snake case.

El script convierte los números en decimal contenidos en el archivo `fileWithData.txt` a binario y hexadecimal. Los resultados se imprimen en la terminal y en un archivo llamado `ConvertionResults.txt`.

## 3. [Count Words](word_count.py)

Para ejecutar el script, se debe correr el siguiente comando en la terminal desde la ruta donde se encuentra el archivo `word_count.py`:

```
python word_count.py fileWithData.txt
```

Donde `fileWithData.txt` es el archivo con los datos a analizar.

El requerimento 4 pedía que el archivo se nombrará `wordCount.py`, pero para seguir la convención de nombrar los archivos con minúsculas y separar las palabras con guiones bajos, se nombró como `word_count.py`, de acuerdo con el requerimiento 8 de que cumpla con PEP8, donde se menciona que se usará CamelCase si el proyecto en primera instancia fue creado con ese estilo de escritura en un principio, de lo contrario se debe usar Snake case.

[!IMPORTANT]
Se creó un subdirectorio llamado **utilities** donde se encuentran archivos usados por los scripts principales. Tal es el caso de `data_loader.py` que se encarga de cargar los datos de un archivo **.txt**, así como `statistics.py` usado para calcular las estadísticas descriptivas de los datos, además de `converter.py`para convertir los números en formato decimal dentro de una lista a binarios y hexadecimales, y por último `word_counter.py` que cuenta el número de veces que una palabra se repite en una lista.

[!NOTE]
El repositorio cuenta con un pipeline de CI/CD que se encarga de asegurar que tanto pylint como flake8 pasen exitosamente.

