from django.contrib import admin
from django.urls import path
from newcontact.views import show_contact, add_contact, update_contact, delete_contact

urlpatterns = [
    path('', show_contact.Showcontact.as_view(), name="home"),
    path('add/', add_contact.Addcontact.as_view(), name="add"),
    path('update/', update_contact.Updatecontact.as_view(), name="update"),
    path('delete/', delete_contact.Deletecontact.as_view(), name="delete"),
    
]