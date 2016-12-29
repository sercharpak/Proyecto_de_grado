all: new_project.gv old_project.gv new_project.png old_project.png ../scripts/Proyecto_de_grado/docs/new_project.gv ../scripts/Proyecto_de_grado/docs/new_project.png ../scripts/Proyecto_de_grado/docs/old_project.gv ../scripts/Proyecto_de_grado/docs/old_project.png
#Compiling the dot languages into png images
new_project.png:new_project.gv
	dot -Tpng new_project.gv -o new_project.png
old_project.png:old_project.gv
	dot -Tpng old_project.gv -o old_project.png
#Copying into the repository folder
../scripts/Proyecto_de_grado/docs/new_project.gv:new_project.gv
	cp new_project.gv ../scripts/Proyecto_de_grado/docs/new_project.gv
../scripts/Proyecto_de_grado/docs/new_project.png:new_project.png
	cp new_project.png ../scripts/Proyecto_de_grado/docs/new_project.png
../scripts/Proyecto_de_grado/docs/old_project.gv:old_project.gv
	cp old_project.gv ../scripts/Proyecto_de_grado/docs/old_project.gv
../scripts/Proyecto_de_grado/docs/old_project.png:old_project.png
	cp old_project.png ../scripts/Proyecto_de_grado/docs/old_project.png
#Cleaning the images
clean:
	rm *.png
