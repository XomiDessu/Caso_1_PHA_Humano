# Caso 1 · PAH Gene

## 

## 1\. Contexto biológico

La fenilalanina hidroxilasa humana, codificada por el gen **PAH**, participa en el metabolismo de la fenilalanina. Su función consiste en catalizar la conversión de fenilalanina a tirosina utilizando tetrahidrobiopterina como cofactor.

Cambios en la secuencia de **PAH** pueden modificar la expresión, estabilidad o actividad de la proteína. Sin embargo, detectar una variante no implica automáticamente que ésta tenga una consecuencia funcional.

En este proyecto se analizará un conjunto reducido de **variantes reales localizadas en PAH**.

El conjunto incluye variantes con diferentes:

* frecuencias poblacionales;
* posiciones dentro del gen;
* consecuencias sobre la secuencia codificante;
* cambios de aminoácidos;
* niveles conocidos de evidencia funcional.

El objetivo será construir una **priorización independiente** a partir de los datos disponibles y posteriormente integrar distintas capas de evidencia.

\---



# 2\. Pregunta central

> \*\*¿Qué variante del conjunto proporcionado presenta la evidencia más consistente de alterar la función de la fenilalanina hidroxilasa y cómo puede justificarse esa conclusión integrando información genómica, proteica y estructural?\*\*

La intención no es únicamente identificar una variante candidata.

El objetivo principal es construir una **cadena de evidencia reproducible** que permita distinguir entre:

**observación → anotación → inferencia → evidencia adicional → interpretación.**

\---



# 3\. Datos proporcionados

El paquete de trabajo contiene información genómica, transcriptómica y proteómica correspondiente a **PAH**.

## 3.1 Datos genómicos

### `PAH\_variants\_masked\_GRCh38.vcf`

Panel reducido de variantes reales localizadas en la región de **PAH**.

El archivo contiene:

* cromosoma;
* posición;
* identificador interno;
* alelo de referencia;
* alelo alternativo;
* información de frecuencia poblacional.

La información que pudiera revelar directamente la clasificación conocida de las variantes ha sido retirada.

\---

### `PAH\_NM\_000277.3\_GRCh38\_subset.gtf`

Anotación reducida del gen **PAH** correspondiente al transcrito de referencia utilizado en el proyecto.

Contiene, entre otros:

* gen;
* transcrito;
* exones;
* CDS;
* 5′ UTR;
* 3′ UTR.

La anotación permite determinar la posición de cada variante respecto a la arquitectura del gen.

\---

## 3.2 Datos transcriptómicos

### `PAH\_CDS\_NM\_000277.3.fasta`

Secuencia codificante correspondiente al transcrito de referencia utilizado.

Esta secuencia permitirá:

* relacionar coordenadas genómicas con posiciones dentro del CDS;
* identificar codones afectados;
* determinar posibles cambios de aminoácidos.

\---

## 3.3 Datos proteicos

### `PAH\_WT\_NP\_000268.1.fasta`

Secuencia de referencia de la proteína fenilalanina hidroxilasa humana.

Se utilizará para:

* verificar cambios de aminoácidos;
* generar variantes proteicas;
* preparar modelos estructurales;
* comparar proteína WT frente a proteínas mutantes.

\---

## 3.4 Información adicional

El paquete incluye tablas auxiliares con:

* frecuencia poblacional;
* identificadores internos;
* plantillas para ranking;
* referencias utilizadas para construir el caso.

\---



# 4\. Referencias utilizadas

El proyecto utiliza como sistema de referencia:

|Elemento|Referencia|
|-|-|
|Ensamblaje genómico|GRCh38|
|Gen|PAH|
|Transcrito|NM\_000277.3|
|Proteína|NP\_000268.1|
|Estructura experimental|PDB 6HYC|

PAH se encuentra en la **hebra negativa**.

Esto deberá considerarse al interpretar cambios entre:

**genoma → transcrito → proteína.**

Por ejemplo, una sustitución descrita como:

`G>A`

en la referencia genómica puede corresponder a:

`C>T`

en la orientación del transcrito.

\---



# 5\. Análisis esperados

El proyecto debe seguir una progresión de análisis.

No se espera que una sola herramienta determine la respuesta.

Cada etapa deberá aportar una capa diferente de evidencia.

\---

## 5.1 Exploración del VCF

Se deberá:

* cargar el archivo VCF;
* identificar las variantes disponibles;
* distinguir REF y ALT;
* clasificar el tipo de variante;
* revisar la frecuencia poblacional;
* reconocer que referencia y alelo mayoritario no son necesariamente equivalentes.

\---

## 5.2 Localización de variantes

Utilizando el GTF se deberá determinar la posición de cada variante respecto a:

* CDS;
* exón;
* intrón;
* UTR;
* otras regiones anotadas.

\---

## 5.3 Relación genoma → transcrito

Para las variantes codificantes se deberá:

* convertir la coordenada genómica en posición dentro del CDS;
* considerar la orientación de la hebra;
* identificar REF y ALT en orientación transcriptómica.

\---

## 5.4 Consecuencia sobre el codón y la proteína

Para las variantes codificantes se deberá determinar:

* codón de referencia;
* codón alternativo;
* aminoácido WT;
* aminoácido alternativo;
* tipo de consecuencia.

Las variantes podrán clasificarse, por ejemplo, como:

* sinónimas;
* missense;
* deleciones in-frame;
* otros tipos cuando corresponda.

\---

## 5.5 Frecuencia poblacional

Se deberá considerar la frecuencia poblacional como una línea de evidencia adicional.

Sin embargo:

> \*\*Una variante rara no es necesariamente funcionalmente dañina.\*\*

De la misma manera:

> \*\*Una variante frecuente no es automáticamente irrelevante.\*\*

La frecuencia deberá interpretarse junto con otras capas de información.

\---



# 6\. Ranking inicial de variantes

Antes de utilizar modelos fundacionales, se deberá construir un **ranking inicial de cinco variantes**.

La priorización deberá considerar, como mínimo:

* localización;
* consecuencia molecular;
* frecuencia poblacional;
* naturaleza del cambio proteico.

El ranking deberá incluir una justificación explícita.

Ejemplo:

|Rank|Variante|Región|Consecuencia|Evidencia|Justificación|
|-:|-|-|-|-|-|
|1||||||
|2||||||
|3||||||
|4||||||
|5||||||

Este ranking deberá conservarse.

\---



# 7\. Evaluación con Evo2

Las variantes priorizadas serán evaluadas mediante **Evo2** utilizando la API de NVIDIA.

Para las SNV se comparará:

`P(REF | contexto)`

frente a:

`P(ALT | contexto)`

y se calculará:

`ΔlogP = log P(ALT) - log P(REF)`

Una puntuación más negativa indica que el modelo favorece más fuertemente el alelo de referencia dentro del contexto analizado.



### Importante

El resultado de Evo2:

* no representa patogenicidad;
* no demuestra causalidad;
* no sustituye evidencia experimental.

Debe interpretarse como una **capa adicional de evidencia sobre la secuencia**.

\---



# 8\. Comparación antes y después de Evo2

Se deberá comparar:

**ranking inicial**

vs.

**evidencia Evo2**

y responder:

* ¿qué variantes fueron más penalizadas por Evo2?
* ¿coinciden con el ranking inicial?
* ¿qué variantes cambiaron de prioridad?
* ¿qué discrepancias aparecieron?

Las discrepancias deberán discutirse.

No deben tratarse automáticamente como errores del modelo ni como errores del análisis previo.

\---

# 9\. Selección de candidatos para análisis estructural

A partir de la integración del análisis genómico y Evo2 se seleccionarán candidatos para estudiar con **RF3**.

No es necesario modelar todas las variantes.

Se espera seleccionar aquellas que permitan responder una pregunta concreta.

Por ejemplo:

* una variante con fuerte evidencia Evo2;
* una variante con alta prioridad genómica;
* dos candidatos con evidencia contrastante.

\---



# 10\. Análisis estructural con RF3

Para los candidatos seleccionados se generarán modelos de:

* proteína WT;
* proteína mutante.

Se podrán comparar:

* posición del residuo;
* entorno local;
* contactos;
* diferencias estructurales;
* confianza del modelo;
* similitud con la estructura experimental disponible.

Cuando corresponda, se utilizará **PDB 6HYC** como referencia estructural experimental.

\---



# 11\. Integración de evidencia

Cada variante priorizada deberá evaluarse mediante una tabla integradora.

|Variante|Evidencia genómica|Frecuencia|Consecuencia proteica|Evo2|RF3|Interpretación|
|-|-|-|-|-|-|-|
||||||||

El análisis deberá identificar:

* evidencia convergente;
* evidencia contradictoria;
* evidencia insuficiente;
* incertidumbres.

\---



# 12\. Ranking final

Después de integrar todas las capas de evidencia, se construirá un ranking final.

El ranking inicial deberá permanecer visible para permitir comparar cómo cambió el razonamiento.

Se deberá explicar:

* qué variantes subieron;
* qué variantes bajaron;
* qué evidencia produjo esos cambios.

La posición final de una variante deberá justificarse mediante la evidencia reunida y no únicamente mediante un score automático.

\---



# 13\. Entregables

#### &#x09;- Notebook reproducible

#### &#x09;- Tabla de variantes anotadas

#### &#x09;- Ranking inicial

&#x09;		Top 5 previo a Evo2.

&#x09;		Debe conservarse como evidencia del primer nivel de razonamiento.

#### &#x20;     	- Resultados Evo2

#### &#x09;- Análisis estructural

#### &#x09;- Ranking final

&#x09;		Top 5 final integrando toda la evidencia.

#### &#x09;- Conclusión

\---



# 14\. Criterios generales de evaluación

Se evaluará principalmente:

* reproducibilidad;
* calidad del análisis;
* integración de evidencia;
* razonamiento;
* interpretación;
* reconocimiento de limitaciones;
* claridad de la conclusión.

No se evaluará únicamente si el ranking coincide exactamente con la solución correcta.

Una propuesta diferente podrá considerarse válida si está correctamente argumentada y respaldada por evidencia.

\---

# 

