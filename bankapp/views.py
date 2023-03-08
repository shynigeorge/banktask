from django.contrib import messages, auth



from django.contrib.auth.models import User


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  login
from bankapp.forms import AccountForm
from bankapp.models import Register, District, City


def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already exist")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username,  password=password)
                user.set_password(password)
                user.save()
                print("success")
                return redirect('login')
    else:
        print("this is not post method")
        return render(request,'signup.html')

        alert = True
        return render(request, "signup.html", {'alert': alert})
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(demo)
        else:
            messages.info(request,'Invalid username or password')
            return redirect(login)
    else:
         return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')



def registration(request):

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted.')
            return render(request, 'account.html', {'form': AccountForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)


    else:
        form = AccountForm()
    obj = District.objects.all()
    br=City.objects.all()
    return render(request, 'account.html', {'form': form,'obj':obj,'br':br})

def person_update_view(request, pk):
    person = get_object_or_404(Register, id=pk)
    form = AccountForm(instance=person)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', id=pk)
    return render(request, 'account.html', {'form': form})


def load_branch(request):
    district_id = request.GET.get('district_id')
    b = City.objects.filter(district_id=district_id).all()
    #return render(request, 'demo.html', {'b': b})
    return render(request, 'dropdownlist.html', {'b': b})
   # return JsonResponse(list(b.values('id', 'name')), safe=False)

def demo(request):
    return render(request,'newpage.html')

