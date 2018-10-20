from django.shortcuts import render,redirect,get_object_or_404
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http  import HttpResponse,Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from .models import Detail,Project,Comment,Votes
from .forms import SignupForm,DetailForm,CommentsForm,ProjectForm

@login_required(login_url='accounts/login/')
def index(request):
    projects = Project.get_projects().order_by('-pub_date')
    details = User.objects.all()
    
    

    return render(request, "index.html", {"projects":projects,"details":details,})

def search_results(request):
    
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_detail = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        details = User.objects.all()
        print(details)

        return render(request, 'search.html',{"message":message,"usernames":searched_detail,"details":details})

def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect ('post')

    else:
        form = ProjectForm()
    return render(request, 'new_projects.html', {"form":form})
def vote_post(request):
    project = get_object_or_404(id= user_id).order_by('pub_date')
    project  .add(request.user)
    return redirect('post')