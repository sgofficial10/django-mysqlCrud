from django.urls import path
from . import views



urlpatterns = [

    # dashboard URL
    path('logout', views.logout),
    path('dashboard', views.dashboard),

    # Class URL
    path('deleteClass', views.deleteClass,),
    path('viewClass/<int:class_id>', views.viewClass, name="view_class"),  
    path('createClass', views.createClass, name="create_class"),
    path('classList', views.listClass, name="list_class"),
    path('listSection', views.listSection),


    # Section URL

    path('createSection', views.createSection, name="create_section"),
    path('listSections', views.listSections, name="list_section"),
    path('viewSection/<int:section_id>', views.viewSections, name="view_section"),
]