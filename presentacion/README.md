# Presentación del proyecto PAH

Abrir **PAH_plantilla_general.pptx**: plantilla general de 17 diapositivas, con contenido real únicamente en las diapositivas **5–7**, correspondientes al Integrante 3. Los títulos y responsables organizan las otras secciones; sus cuerpos, tablas y espacios de figura quedan con lorem ipsum o guiones.

**PAH_plantilla_general.pdf** es el respaldo de lectura de la plantilla. La versión PowerPoint conserva la edición de texto, tablas, diagramas y el gráfico de anillo.

**PAH_plantilla_general.potx** es la versión de plantilla de PowerPoint: abrirla crea una presentación nueva con estos apartados. El tema incluye la paleta y las fuentes del diseño. Para añadir páginas, duplicar la diapositiva cuyo formato se quiera reutilizar.

| Diapositiva | Apartado | Responsable |
|---|---|---|
| 1 | CASO 1 | Equipo |
| 2 | Contexto y pregunta del proyecto | Integrante 1 |
| 3 | Mapa de la presentación | Equipo |
| 4 | Variantes y localización genómica | Integrante 2 |
| 5 | Del genoma al cambio de aminoácido | Integrante 3 |
| 6 | 15 variantes: siete producen un missense | Integrante 3 |
| 7 | VAR012: una deleción que conserva el marco | Integrante 3 |
| 8 | Ranking inicial y criterios | Integrante 1 |
| 9 | Evaluación con Evo2 | Integrante 4 |
| 10 | Comparación con el ranking inicial | Integrantes 1 y 4 |
| 11 | Modelado de proteína WT y mutantes | Integrante 5 |
| 12 | Comparación estructural | Integrante 6 |
| 13 | Integración de las capas de evidencia | Integrante 1 |
| 14 | Ranking final y justificación | Integrante 1 |
| 15 | Conclusión y límites | Integrante 1 |
| 16 | Referencias | Equipo |
| 17 | Elementos reutilizables | Equipo |

La última diapositiva contiene grupos de hélice, bloques, red y archivo, además de la paleta, etiquetas, flechas y tarjetas. Copiar y pegar conserva la edición; para modificar una pieza interna, usar **Agrupar → Desagrupar**. Las ilustraciones son esquemáticas. Los espacios de figura están vacíos y los guiones no representan resultados.

Las tres diapositivas originales del Integrante 3 permanecen en `integrante3_transcrito_proteina.pptx`; el guion está en `integrante3_guion.md`. La plantilla general incorpora una versión visual ampliada de esa sección y conserva sus notas del presentador.

Para regenerar el PPTX desde la tabla verificada: `python presentacion/generar_plantilla.py` (requiere python-pptx y pandas). La exportación a PDF se realiza en PowerPoint.
