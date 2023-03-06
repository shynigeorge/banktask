from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from bankapp.form import AccountForm
from bankapp.models import Register, District, Branch


def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":

        username= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']

        user=User.objects.create_user(username=username,password=password1)
        user.save()
        return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a user!!")
            else:
                return redirect('/demo')
        else:
            alert = True
            return render(request, "login.html", {'alert': alert})
    return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')



def registration(request):

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted.')
            return render(request, 'registration.html', {'form': AccountForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)


    else:
        form = AccountForm()
    obj = District.objects.all()
    br=Branch.objects.all()
    return render(request, 'registration.html', {'form': form,'obj':obj,'br':br})

def person_update_view(request, pk):
    person = get_object_or_404(Register, pk=pk)
    form = AccountForm(instance=person)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'registration.html', {'form': form})

def load_branch(request):
    district_id = request.GET.get('district_id')
    b = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'registration.html', {'b': b})

def demo(request):
    return render(request,'newpage.html')
