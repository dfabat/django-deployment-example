from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # autenticação do usuário
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone attempted to login and failed!")
            print("Username: {a} and password: {b}".format(a=username, b=password))
    else:
        return render(request, 'basic_app/login.html', context={})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    # checagem de registro
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():  # se ambos antendem os critérios dos bancos

            user = user_form.save()  # salve as informações no banco
            user.set_password(user.password)  # pegue o password e faça o hash
            user.save()  # salve por cima da versão antiga

            profile = profile_form.save(commit=False)
            profile.user = user  # que é o user_form que é igual ao UserForm

            if 'profile_pic' in request.FILES:  # request.FILES serve para todo tipo de arquivo, imagens, textos, planilhas, etc...
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:  # HTTP request without a thing
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'basic_app/registration.html', context={
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    })