
from django.urls import path
# from shop import views
# from shop.views import current_page
from .views import *

#without below statment it works
# from shop.views import home_page

urlpatterns = [
    path('home/',home_page,name='home'),
    path('current/',current_page,name='current'),
    path('current/add',add,name='add'),
]