from django.urls import path
from . import views



urlpatterns = [

    # dashboard URL
    path('logout', views.logout),
    path('dashboard', views.dashboard),

    # Class URL
    path('deleteClass', views.deleteClass),
    path('viewClass/<int:class_id>', views.viewClass),  
    path('createClass', views.createClass),
    path('classList', views.listClass),


    # Section URL

    path('createSection', views.createSection)
]