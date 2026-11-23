load database/optional_resources/protein/6HYC.cif
hide everything
show cartoon
bg_color white
color marine, resi 22-117          # regulatorio (resuelto parcialmente)
color forest, resi 118-410         # catalítico
color salmon, resi 411-450         # tetramerización
show sticks, resn H4B
color yellow, resn H4B and elem C
orient
png database/optional_resources/PyMOL_images/6HYC_dominios.png, dpi=300
quit
