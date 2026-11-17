# Reporte general del proyecto PAH

Abrir **PAH_reporte_general.docx**. Incluye portada en una página independiente, índice de capítulos, listas de figuras y tablas, y diez capítulos que comienzan en una página nueva. Está completado el aporte del **Integrante 3**: su capítulo de transcrito y proteína y sus apartados de conclusiones y referencias. Los demás aportes tienen únicamente la nota del integrante responsable.

**Conclusiones y límites por integrante** y **Referencias por integrante** contienen seis apartados, uno por persona. Cada integrante debe completar únicamente sus conclusiones y sus fuentes; el apartado del Integrante 3 ya está escrito. Las fuentes de su análisis se concentran en Referencias.

El texto normal usa **Arial 12**, alineación a la izquierda e interlineado **1.15**. Los títulos de capítulo usan el estilo **Título 1** con salto de página anterior; al añadir un capítulo con ese estilo se conservan la numeración y el índice.

La sección del Integrante 3 incluye dos diagramas nativos de Word, la anotación de las 15 variantes, los controles manuales y la lista de siete FASTA. Los diagramas son lienzos con formas, flechas y cuadros de texto editables: hacer clic en un elemento dentro del lienzo para cambiarlo. Sus componentes se guardan dentro del DOCX y no requieren archivos externos.

## Figuras, tablas e índice automáticos

Los títulos contienen campos **SEQ Figura** y **SEQ Tabla**. Las menciones dentro del texto usan campos **REF**, y los índices usan campos **TOC**; sus números no están escritos como texto fijo.

Para agregar una figura o tabla antes o después de las existentes:

1. Insertar la figura o tabla en el lugar deseado.
2. Usar **Referencias → Insertar título** y elegir **Figura** o **Tabla**. Si el rótulo Figura no aparece, crearlo con **Nuevo rótulo**. También se puede copiar un título existente; editar solo su descripción, conservando el campo numérico.
3. Después de agregar, mover o eliminar elementos, usar **Ctrl+A, F9** y seleccionar **Actualizar toda la tabla** para los índices. En algunas computadoras se requiere **Fn+F9**. El documento no solicita recalcular los campos al abrirlo.

Word mantiene la secuencia mediante sus campos; la actualización después de editar se realiza con ese comando, sin macros. No sustituir el campo de número por un número escrito manualmente.

## Archivos

- `PAH_reporte_general.docx`: documento general editable con los campos ya actualizados en Word.
- `PAH_reporte_general_vista_previa.pdf`: vista previa de las páginas renderizadas desde Word; los campos editables se conservan en el DOCX.
- `recursos/diagrama_VAR003_nativo.xml` y `diagrama_VAR012_nativo.xml`: componentes de Word utilizados por el generador; quedan incorporados dentro del DOCX. Los PNG/SVG anteriores se conservan como recursos de respaldo.
- `diagramas_nativos.ps1`: construye los dos lienzos con las herramientas de dibujo de Word.
- `generar_reporte.py`: generador del DOCX a partir de la tabla verificada y los lienzos nativos; requiere python-docx y pandas. Después de regenerarlo, actualizar los campos desde Word. Para crear una copia sin reemplazar el reporte actual: `python reporte/generar_reporte.py --salida copia.docx`.

Se comprobó la renumeración en una copia temporal al insertar un título de figura y uno de tabla antes de los existentes: las secuencias y la referencia cruzada se actualizaron correctamente. La portada y el índice ocupan una página cada uno, y las 15 variantes caben juntas en una tabla.

La versión con diagramas nativos se verificó al reabrirla en Word: contiene dos lienzos y 53 elementos editables, ninguna imagen dentro del DOCX y ninguna relación con archivos externos. El generador también conserva los lienzos al crear una copia nueva.
