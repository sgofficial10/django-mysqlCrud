from django.urls import path
from . import views



urlpatterns = [

    # dashboard URL
    path('logout', views.logout),
    path('dashboard', views.dashboard),

    # Class URL
    path('deleteClass', views.deleteClass,),
    path('viewClass/<int:class_id>', views.viewClass),  
    path('createClass', views.createClass, name="create_class"),
    path('classList', views.listClass, name="list_class"),
    path('listSection', views.listSection),


    # Section URL

    path('createSection', views.createSection),
    path('listSection', views.listSection),
]