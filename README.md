# djangonautic

This is Djanog test project. The app djangonautic is to create the blog posts.

## Prerequisite
- Python3 - If you plan on running application locally.
- Docker - If you plan on running application in container.

---

## Instructions to run project
The code repository includes 
1. Base code for application
2. Dockerfile - Includes docker file to deploy application in container
3. requirements.txt - Inlcudes the list of packages or libraries needed to work on a project that can all be installed with the file.

The application can be run in two ways. You can run it directly on the system/server (MAC/Windows/Linux) or on docker container

### Run application in on local system
1. Clone repository - `git clone https://github.com/dipaksingbhukwal/djangonautic.git`
2. Change directory to djangonautic - `cd djangonautic`
3. Apply database model changes with - `python manage.py makemigrations && python manage.py migrate`
4. Start django server - `python manage.py runserver`
5. Access application using url http://127.0.0.1:8000/ on browser

### Run application in container
1. Clone repository `git clone https://github.com/dipaksingbhukwal/djangonautic.git`
2. Change directory to djangonautic - `cd djangonautic`
3. Built the docker image - `docker build -t my_django_app .`
4. Run docker container - `docker run -p 8000:8000 my_django_app`
5. Access application using url http://127.0.0.1:8000/ on browser

---
### Notes
- The Docker file is not complete. The database used in applciation is not persistant. The database will be reset when the container is restarted.
- Feel free to play around docker file to make it 
