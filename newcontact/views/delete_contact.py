from django.shortcuts import render, redirect
from django.views import View
from newcontact.models import Phonebook


class Deletecontact(View):

    def get(self, request):
        return redirect("home")

    def post(self, request):
        del_id = request.POST.get('del_id')
        try:
            contact = Phonebook.objects.get(id=del_id)
            contact.delete()
        except:
            return redirect("home")

        return redirect("home")