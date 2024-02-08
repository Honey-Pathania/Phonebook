from django.shortcuts import render, redirect
from django.views import View
from newcontact.models import Phonebook


class Updatecontact(View):
    def get(self, request):
        return redirect("home")
    
    def post(self, request):

        if request.POST.get('meth')=='get':
            U_id = request.POST.get('update')

            contact = Phonebook.objects.get(id=U_id)
            return render(request, "update.html", {"contact":contact})
        
        if request.POST.get('meth')=='post':
            error_message = None
            UU_id = request.POST.get('up_id')
            Name = request.POST.get('name')
            new_contact = request.POST.get('phone')
            Name = Name.lower()

            contact = Phonebook.objects.get(id=UU_id)

            if ((new_contact==contact.Contact) and (Name==contact.Name)):
                return redirect('home')
            else:
                try:
                    if (Phonebook.objects.get(Contact=new_contact).exclude(Contact=contact.Contact)):
                        error_message = "Phone Number Already Exist!"

                except:
                    pass

            if len(new_contact)>10:
                error_message="Please enter valid Contact number."

            if error_message:
                return render(request, "update.html", {"error":error_message})
            else:
                contact.Name = Name
                contact.Contact = new_contact
                contact.save()
                return redirect("home")
