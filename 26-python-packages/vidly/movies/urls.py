from django.urls import path
from . import views

# movies/
# movies/1/details

urlpatterns = [ # url configuration
    path('', views.index, name="movies_index"), # root path
    path('<int:movie_id>/', views.detail, name='movies_detail') # url parameter
]