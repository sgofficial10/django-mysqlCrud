from django.urls import path
from . import views



urlpatterns = [
    path('deleteClass', views.deleteClass),
    path('logout', views.logout),
    path('viewClass/<int:class_id>', views.viewClass),
    path('dashboard', views.dashboard),
    path('createClass', views.createClass),
    path('classList', views.listClass)
]