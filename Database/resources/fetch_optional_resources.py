#!/usr/bin/env python3
"""Descarga recursos públicos opcionales para el caso PAH. Requiere internet."""
from pathlib import Path
from urllib.request import urlretrieve

base = Path(__file__).resolve().parents[1]
items = {
    base/'transcript'/'NM_000277.3_full_mRNA.fasta': 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=NM_000277.3&db=nuccore&report=fasta&retmode=text',
    base/'genomic'/'NG_008690.2_RefSeqGene.fasta': 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=NG_008690.2&db=nuccore&report=fasta&retmode=text',
    base/'protein'/'6HYC.cif': 'https://files.rcsb.org/download/6HYC.cif',
}
for path,url in items.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    print(f'Descargando {url}')
    urlretrieve(url,path)
    print(f'  -> {path} ({path.stat().st_size} bytes)')
