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
    votes =Votes.objects.all()
    comments = Comment.objects.all()
    
    return render(request, "index.html", {"projects":projects,"details":details,"comments":comments,"votes":votes})


def search_results(request):
    
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"message":message,"projects":searched_projects,})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect ('index')

    else:
        form = ProjectForm()
    return render(request, 'new_projects.html', {"form":form})
def vote_project(request):
    project = get_object_or_404(Project, id=request.POST.get('project_id'))
    Project.votes.add(request.user)
    return redirect('index')


def detail(request, user_id):
    title = "Profile"
    project = Project.get_post_by_id(id= user_id).order_by('pub_date')
    details = User.objects.get(id=user_id)
    users = User.objects.get(id=user_id)

    return render(request, 'detail/detail.html',{'title':title,"images":images,"details":details,})

def edit_detail(request):
    current_user = request.user
    detail = Detail.objects.get(user= request.user)
    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.save()
        return redirect('index')
    else:
        form = DetailForm()
    return render(request, 'detail/edit-detail.html', {"form": form,})

def add_comment(request, image_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.project = project
            comment.save()
    return redirect('index')

def vote(request, project_id):
    current_user = request.user
    voted_project = Project.objects.get(id=project_id)
    new_vote, created = Votes.objects.get_or_create(user_vote=current_user, voted_project=voted_project)
    new_vote.save()

    return redirect('index')