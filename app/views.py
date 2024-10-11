from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context, loader
from django.shortcuts import render

from accounts.views import login
from .forms import UserForm

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

    return render(request, "resources/lavish/index.html", context)


@login_required(login_url='/login')
def dashboard(request):
    context = {}
    context["links"] = Detail.objects.all()

    return render(request, "services/dashboard.html", context)


def service1(request):
    return render(request, "resources/lavish/index.html")


def preview1(request):
    return render(request, "resources/lavish/preview.html")


@login_required(login_url='/login')
def user_list(request):
    users = Detail.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@login_required(login_url='/login')
def user_create(request):
    if request.method == 'POST':
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
        return redirect('user_list')
    else:
        form = Detail()
    return render(request, 'users/user_form.html', {'form': form})

@login_required(login_url='/login')
def user_read(request, pk):
    user = get_object_or_404(Detail, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

@login_required(login_url='/login')
def user_update(request, pk):
    user = get_object_or_404(Detail, pk=pk)

    if request.method == 'POST':
        # Handle form submission
        user.firstname = request.POST['firstname']
        user.surname = request.POST['surname']
        user.lastname = request.POST['lastname']
        user.skill1 = request.POST['skill1']
        user.skill2 = request.POST['skill2']
        user.skill3 = request.POST['skill3']
        user.profile_img = request.POST['profile_img']
        user.background_img = request.POST['background_img']
        user.profession = request.POST['profession']
        user.overview = request.POST['overview']
        user.contact_number = request.POST['contact_number']
        user.email = request.POST['email']
        user.address = request.POST['address']
        user.portfolio = request.POST['portfolio']
        user.role1 = request.POST['role1']
        user.role1_info = request.POST['role1_info']
        user.role2 = request.POST['role2']
        user.role2_info = request.POST['role2_info']
        user.role3 = request.POST['role3']
        user.role3_info = request.POST['role3_info']
        user.save()
        return redirect('user_list')

    # Render the form for updating user details
    return render(request, 'users/update_form.html', {'user': user})

@login_required(login_url='/login')
def user_delete(request, pk):
    user = get_object_or_404(Detail, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
