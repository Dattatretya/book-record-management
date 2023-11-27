from django.urls import path
from .views import  helloview, addbook, addbookview,editbook,edit, deletebook

urlpatterns = [
    path("", helloview),
    path("addbook/", addbook),
    path("addbookdata", addbookview),
    path("editbook",editbook),
    path("editbook/edit", edit),
    path("deletebook", deletebook)
]