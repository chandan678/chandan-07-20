# chandan-07-20
**_Todo App with django-vue.js_**

**Installation**

First install Docker, and start the Docker 

Next, clone this repo:
```
git clone https://github.com/chandan678/chandan-07-20.git
cd chandan-07-20
```
To Run project with django
```
docker-compose run web python manage.py migrate
docker-compose up
```
To Run project with vue
```
cd vueapp
docker build -t vuejs-cookbook/dockerize-vuejs-app .
docker run -it -p 8080:8080 --rm --name dockerize-vuejs-app-1 vuejs-cookbook/dockerize-vuejs-app   
```
Access django run app at : http://0.0.0.0:8000/

Access the Vue-tod0 app at:  http://localhost:8080/static/src/vue/dist/ 

