`pipenv install django==2.1`
`pipenv shell` to start virtual environment


### django admin to create a new django project
`django-admin startproject vidly` . (creates admin project in current directory w/ boilerplate code)

### Creating an app
`python3 manage.py startapp movies`


### Creating Views and route /movies
* added a route in urlpatterns to include movies.urls
* movie.urls has an index route



### starting server with `python3 manage.py runserver`
#### Check before starting server
* Make sure you have the venv started
* The correct python interpreter pointing to python in venv


# Register models 
admin.site.register(Genre)
admin.site.register(Movie)