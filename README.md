My final project for Harvard's CS50 Web

https://github.com/me50/JuanGarrid0/tree/web50/projects/2020/x/capstone

Distinctiveness and Complexity: My final Project is a videoclub that loans movies to users, this movies can be films or series, my Project was progammed by using JavaScript, HTML, css and django(python), The database used is a default SQLite db, i have already used this in some uni projects so i decided to not go very crazy and use it. I have used several models, created a complete authentication system . This requires a strong understanding of Django as there are not indications unlike for the other projects, this one you had to create and code from 0 to hero. The superuser has Access to the admin panel and to the entire database.

Inside my movies app, you can find: static: CSS styles file that styles every HTML item specifically as there is no Bootstrap or Vue being used, JS file that is used to implement functionalities for my projects frontend, such as alert messages or security checkings on forms, and the images of movies and genres.

templates: layout (parent to all) where both the header and the footer are set, the footer contains irrelevant info and is there mainly for aesthetics, however the header contains the nav that redirects the web users to other pages that will be explained later. buscarDirector is where the Director instances that start with the string that is entered in the director page search bar detalles loads the personal movie page for each movie instance, regardless of the page where you might be coming from, director, lista or genero director lists all Director instances, each instance links to every movie directed by said Director formulario genero lists all genre instances, each instance links to every movie that is represented by said genre index is the main page, it loads one Movie instance of each genre lista lists Movies, from said instance you can go to the personal Movie info page login is the html template that contains the form that logs in your user or redirects you to the register page register this page registers a new page and saves it in the database so it can later be used update edits a Movie instance, it can change its tipo, genero or director, as long as they are existing

admin.py: Here I registered the models so they would appear in the admin panel, in order to edit ítems and check that they were added correctly, even though I prefered using the console.

models.py:

I used Reserva, to track the movies that we loan a user, its fields are (in english) usuario, correo, fecha, peliculas which is of the type "Movie" and comentarios The User is the predetermined abstract user that we inherit from django The model Movie's fields are tipo, if they are a film or a series, and they are restricted to only those two choices, then genero, nombre and director of the type "Director" Director, then has only two fields, nombre and apellido

views.py: In order to implement Authentication, I made use of Django's generic class-based views LoginView and LogoutView, these handle all authentication functionality interally meaning my code is compact and does not clutter up the views file. I also made a view that renders each film, genre or director, for registerin i made a view that checks that the user is nonexistant and then creates it, i also have views for displaying the personal page of each movie, called 'detalles', i also added the functionality of searching both movies and directors in buscar peliculas and buscar director, and i implemented some CRUD methods, by using 'delete' to delete movie objects and updatePage & update to update movie objects (as later mentioned, only for logged users), reserva then is the view that manages the loans of the movies (also for logged users), and i added some other views in order to avoid repetition throughout my views.py file, these views are getDirector, getMovie...

settings.py: In the projects settings.app, (Videclub>settings.py)jsut added AUTH_USER_MODEL = 'movie.User', add 'movie' to installed apps, add STATIC_URL = '/static/' and add 'movies' to the INSTALLED APPS

The other files, i have not touched and were created by the initial command or by migrating changes from models.py to the database Additional comments:

Styling is implemented exclusively via the CSS file in the Project called styles.css

The functionalities of loaning, deleting or editing a movie are limited to registered users, if the user is not logged in they wont appear.

Run code:

Run like a regular django application "python manage.py runserver" in your console, if you change code that affects the db, mirations Will be necessary, "Python manage.py makemigrations movies" "Python manage.py migrate"

There are many users created, but i mainly used the superuser "j", that i created in order to chech that everything works well from the admin page;

