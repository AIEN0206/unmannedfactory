from django.urls import path
from . import views

app_name = "lumino"

urlpatterns = [
    path('', views.index, name="index"),
    path('charts/', views.charts, name="charts"),
    path('elements/', views.elements, name="elements"),
    path('panels/', views.panels, name="panels"),
    path('widgets/', views.widgets, name="widgets"),
    path('login/', views.login, name="login"),
    # path('api/v1/drivelesscar/', views.getjson, name="getjson"),
]
