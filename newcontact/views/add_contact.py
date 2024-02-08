from django.shortcuts import render, redirect
from django.views import View
from newcontact.models import Phonebook


class Addcontact(View):
    def get(self, request):
        return render(request, "add.html")
    
    def post(self, request):
        error_message = None
        Name = request.POST.get('name')
        Contact = request.POST.get('phone')
        Name = Name.lower()
        contact = Phonebook(Name=Name, Contact=Contact)

        try:

            if Phonebook.objects.get(Contact=Contact):
                error_message = "Phone Number Already Exist!"

        except:
            pass

        if len(Contact)>10:
            error_message="Please enter valid Contact number."

        if error_message:
            return render(request, "add.html", {"error":error_message})
        else:
            contact.save()
            return redirect("home")
