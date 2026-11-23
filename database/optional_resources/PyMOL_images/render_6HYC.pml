load database/optional_resources/protein/6HYC.cif
hide everything
show cartoon
util.cbc                      # color por cadena
bg_color white
set ray_shadows, 0
set cartoon_fancy_helices, 1

# Ligando H4B como sticks, con carbonos en verde
show sticks, resn H4B
color green, resn H4B and elem C
set stick_radius, 0.25, resn H4B

orient
ray 1600, 1200
png database/optional_resources/PyMOL_images/6HYC_figura.png, dpi=300
quit
