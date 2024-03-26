from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('say_hello', views.say_hello),
    path('display_time', views.display_time),
    path('menu',views.menu),
    # add a parameter dishes name in url
    path('dishes/<str:dish>', views.menuitems),
    path('form', views.form_view),
    path('about/', views.about),
    path('logger', views.Logger_by_name),
    path('home_menu', views.home_menu),
    path('about_menu', views.about_menu),
    path('menu_page', views.menu_page),

]