all: new_project.gv old_project_AortaWall.gv old_project_SegCall.gv new_project.png old_project_AortaWall.png old_project_SegCall.png ../scripts/Proyecto_de_grado/docs/new_project.gv ../scripts/Proyecto_de_grado/docs/new_project.png ../scripts/Proyecto_de_grado/docs/old_project_AortaWall.gv ../scripts/Proyecto_de_grado/docs/old_project_SegCall.gv ../scripts/Proyecto_de_grado/docs/old_project_AortaWall.png ../scripts/Proyecto_de_grado/docs/old_project_SegCall.png
#Compiling the dot languages into png images
new_project.png:new_project.gv
	dot -Tpng new_project.gv -o new_project.png
old_project_AortaWall.png:old_project_AortaWall.gv
	dot -Tpng old_project_AortaWall.gv -o old_project_AortaWall.png
old_project_SegCall.png:old_project_SegCall.gv
	dot -Tpng old_project_SegCall.gv -o old_project_SegCall.png
#Copying into the repository folder
../scripts/Proyecto_de_grado/docs/new_project.gv:new_project.gv
	cp new_project.gv ../scripts/Proyecto_de_grado/docs/new_project.gv
../scripts/Proyecto_de_grado/docs/new_project.png:new_project.png
	cp new_project.png ../scripts/Proyecto_de_grado/docs/new_project.png
../scripts/Proyecto_de_grado/docs/old_project_AortaWall.gv:old_project_AortaWall.gv
	cp old_project_AortaWall.gv ../scripts/Proyecto_de_grado/docs/old_project_AortaWall.gv
../scripts/Proyecto_de_grado/docs/old_project_AortaWall.png:old_project_AortaWall.png
	cp old_project_AortaWall.png ../scripts/Proyecto_de_grado/docs/old_project_AortaWall.png
../scripts/Proyecto_de_grado/docs/old_project_SegCall.gv:old_project_SegCall.gv
	cp old_project_SegCall.gv ../scripts/Proyecto_de_grado/docs/old_project_SegCall.gv
../scripts/Proyecto_de_grado/docs/old_project_SegCall.png:old_project_SegCall.png
		cp old_project_SegCall.png ../scripts/Proyecto_de_grado/docs/old_project_SegCall.png
#Cleaning the images
clean:
	rm *.png
