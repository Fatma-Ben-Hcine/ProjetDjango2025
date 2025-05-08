from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.views import View 
from django.contrib.auth import logout
 
class RegisterView(View): 
    def get(self, request): 
        form = UserCreationForm() 
        return render(request, 'registration/register.html', {'form': form}) 
 
    def post(self, request): 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('/')  
        return render(request, 'registration/register.html', {'form': form}) 
def Logout_view(request): 
    logout(request) 
    return redirect('/')