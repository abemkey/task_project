from django.urls import path

from study_management_app import views

urlpatterns = [
    path("",views.studies_list,name='studies_list'),
    path("add_study", views.add_study, name='add_study'),
    path("Add_sponsor", views.Add_sponsor, name='Add_sponsor'),
    path("view_study/<int:id>", views.view_study, name='view_study'),
    path("edit_study/<int:id>", views.edit_study, name='edit_study'),
    path("delete_study", views.delete_study, name='delete_study'),



]
