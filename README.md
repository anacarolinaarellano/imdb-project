# Diseño y Arquitectura de Software: Proyecto Final
### **Por: Ana Carolina Arellano y Pamela Lozano**

Documento con requerimientos y diagramas del proyecto: https://docs.google.com/document/d/1b01iOCu52O0maFAYQodnVeDaV2gEABjYwiEirU9Kq-0/edit?usp=sharing

## Running the project

Project can be build using the following command:

`docker-compose build`

Project can be run using the following command:

`docker-compose –-env-file config/dev.env up`

You can connect to the running container using the following command:

`docker-compose exec app bash`

You can connect to the database using the following command:

`docker-compose –-env-file config/dev.env exec postgres psql -h localhost -U movies movies`

You can recreate the database with the following command:

`docker-compose –-env-file config/dev.env rm -v postgres`

You can access the project using the following url:

http://localhost:5005/hello
