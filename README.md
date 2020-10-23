# project-dq
Follow below instructions to run the application

1. Install Docker on machine
2. clone this project
3. cd to project-dq directory
4. run "docker-compose up -d" command to build and run the containers
5. once the containers are up, go to localhost:8000 to check if the app is working fine.
6. run command "docker ps" to find the container_id for dq-app or iamges dataquality_ap. copy the container id
7. run command "docker exec -it container id python manage.py createsuperuser"
8. give user name, email and password for superuser (by pass the security settings if password is too small for now) 
9. You can log in to the app on localhost:8000 using this super user

To Access the online adminer tool for db access, log on to localhost:8080
select mysql
server = db
user : dq
password: vqd2020
database: dataquality


if you have a mysql database running on local host where this application also running, and if you want to connect to the mysql db on
localhost, then in the hostname field enter "host.docker.internal" instead of localhost.
