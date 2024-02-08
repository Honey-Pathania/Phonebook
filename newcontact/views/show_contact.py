from django.shortcuts import render
from django.views import View
from newcontact.models import Phonebook


class Showcontact(View):
    def get(self, request):
        search = request.GET.get('search')

        if search:
            search = search.lower()
            contacts = Phonebook.objects.filter(Name=search)
        else:
            contacts = Phonebook.objects.all()


        return render(request, "index.html", {'contact':contacts})