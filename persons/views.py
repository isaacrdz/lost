from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.template import loader
from django.shortcuts import (
    render, 
    get_object_or_404, 
    redirect
)

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Person

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    
)

# Create your views here.





class PersonList(ListView):
    model = Person

class PersonDetail(DetailView):
    model = Person

class PersonCreation(CreateView):
    model = Person
    success_url = reverse_lazy('persons:list')
    fields = ['name', 'age','description',]


class PersonUpdate(UpdateView):
    model = Person
    success_url = reverse_lazy('persons:list')
    fields = ['name', 'age','description',]

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons:list')



def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username,
                                            password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/persons')
    context = {}
    return render(request, 'login/login.html', context)


