from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.template import context
from django.shortcuts import render
from .models import Detail


# Create your views here.
def home(request):
    return render(request, "home/index.html")


def services(request):
    if request.method == "POST":
        post = Detail()
        post.firstname = request.POST['firstname']
        post.surname = request.POST['surname']
        post.lastname = request.POST['lastname']
        post.skill1 = request.POST['skill1']
        post.skill2 = request.POST['skill2']
        post.skill3 = request.POST['skill3']
        post.profile_img = request.POST['profile_img']
        post.background_img = request.POST['background_img']
        post.profession = request.POST['profession']
        post.overview = request.POST['overview']
        post.contact_number = request.POST['contact_number']
        post.email = request.POST['email']
        post.address = request.POST['address']
        post.portfolio = request.POST['portfolio']
        post.role1 = request.POST['role1']
        post.role1_info = request.POST['role1_info']
        post.role2 = request.POST['role2']
        post.role2_info = request.POST['role2_info']
        post.role3 = request.POST['role3']
        post.role3_info = request.POST['role3_info']
        post.save()

        return render(request, 'services/dashboard.html')
    else:
        return render(request, 'services/index.html')




def my_portfolio(request):

    context = {}
    context["dataset"] = Detail.objects.all()

    return  render(request, "resources/lavish/index.html", context)
def dashboard(request):

    context = {}
    context["links"] = Detail.objects.all()

    return  render(request, "services/dashboard.html", context)

def service1(request):
    return render(request, "resources/lavish/index.html")


def preview1(request):
    return render(request, "resources/lavish/preview.html")
def dashboard(request):
    return render(request, "services/dashboard.html")
