from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm   #important please note
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):      #django has already buitlt in  (html)form and register is just afunction
    if request.method == 'POST':  #has nothing to do with the actual post but it indicates that we are posting data
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #
            messages.success(request, f'Acoount created for {username}!')
            return redirect('login') #to send the user back to home
    else:
        form = UserRegisterForm()   #blank form if anything else is provided
    return render(request,'users/register.html',{'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

#optyions we have
#message.debug
#message.warning
#messges.info
#message.error
#message.success
