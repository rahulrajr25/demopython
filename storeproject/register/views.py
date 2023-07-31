from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


from register.forms import CVForm
from register.models import CV, Course


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('newpage')

        else:
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect("login")
        else:
            return redirect("register")
        return redirect("/")
    return render (request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


def fill(request):
    form=CVForm()
    if request.method =='POST':
        form=CVForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form Submitted Successfully')
            return redirect('fill')
    return render(request,'fill.html',{'form':form})

def fillupdate(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    form = CVForm(instance=cv)
    if request.method == 'POST':
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('fill', pk=pk)
    return render(request, 'fill.html', {'form': form})



def course(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.filter(department_id=department_id).all()
    return render(request, 'fill2.html', {'course': course})


def newpage(request):
    return render(request,'new page.html')