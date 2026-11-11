# Caso 1 · PAH

Análisis de 15 variantes del gen PAH para identificar cuál tiene la evidencia más consistente de alterar la función de la fenilalanina hidroxilasa, integrando información genómica, de transcrito, Evo2 y estructura (RF3 y PDB 6HYC).

Entrega: lunes 23 de noviembre de 2026.

## Carpetas

| Carpeta | Contenido |
|-|-|
| `database/` | Datos originales del caso. No se modifican. |
| `notebooks/` | Un notebook por capa y, al final, `PAH_caso1.ipynb`. |
| `resultados/` | Tablas `.tsv`, `fasta/` de mutantes, `rf3/` con modelos y `figuras/`. |
| `reporte/` | Borradores y PDF final del reporte (4 páginas máximo). |
| `presentacion/` | Diapositivas. |

## Notebooks y responsables

| Notebook | Responsable | Contenido |
|-|-|-|
| `01_genomica.ipynb` | Integrante 2 | VCF, tipo de variante, frecuencia, ubicación en el gen |
| `02_transcrito_proteina.ipynb` | Integrante 3 | Posición en el CDS, codones, aminoácidos, FASTA mutantes |
| `03_ranking_inicial.ipynb` | Integrante 1 | Criterios y Top 5 inicial |
| `04_evo2.ipynb` | Integrante 4 | ΔlogP con la API de NVIDIA y comparación |
| `05_estructura.ipynb` | Integrantes 5 y 6 | Modelos RF3 y comparación con 6HYC |
| `06_integracion.ipynb` | Integrante 1 | Tabla integradora, ranking final, conclusión y límites |

## Cómo trabajar

1. Abrir el notebook en Colab: File > Open notebook > GitHub, y buscar `XomiDessu/Caso_1_PHA_Humano`.
2. Correr primero la celda de configuración (clona el repositorio).
3. Trabajar en tu propia rama y guardar con File > Save a copy in GitHub.
4. Abrir un pull request hacia `main`; lo aprueba tu revisor.
5. La API key de NVIDIA se pide con `getpass()` y nunca se sube al repositorio.
