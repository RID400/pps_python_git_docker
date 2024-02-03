# pps_python_git_docker
Que es esto??

Esto es una increible, remenda, fantastica, alucinante, estrepidamte, escalofriante, maravillosa, califragilisticoespialidosa aplicacion

Tienes fortuna??
Descubrelo en LA BAYETA DE LA FORTUNA (solo te dirá frases inutiles acerca de cierta serie japonesa de animación)


## REQUISITOS
Es necesario tener instalado docker, más información en https://docs.docker.com/

## GUIA DE USO
1. Desplazarse a carpeta de proyecto.
2. Inicia un contenedor de mongodb con el comando: docker run -d -p 27017:27017 --name mongo mongo:4.4.18
3. Construir la imagen con Dockerfile: docker build -t bayeta .
4. Construir docker en base a la imagen: docker run -d -p 5000:5000 --name bayeta bayeta

## Contribución:
Robert Mitache (Strimer de éxito, gran amigo mejor persona) 0 spam pero https://www.twitch.tv/sxprimo
Dato importante (Es el experto python pero eso nadie lo sabe, todo el credito para mi por favor)
