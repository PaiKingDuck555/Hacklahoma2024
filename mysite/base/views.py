from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
import datetime as dt



def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        p1 = request.POST.get("password1")
        p2 = request.POST.get("password2")

        if first_name != None and last_name != None  and email != None and p1 != None and p2 != None and p1==p2 and username != None:
            user = User.objects.create(first_name=first_name,last_name=first_name,email=email,password=p1, username=username)
            user.save()
            login(request, user)
            return redirect("home")
        else:
            print("An error has occured during registration")

    context = {"page":"register"}
    return render(request, "base/login_register.html", context)

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            print("User no exist with that email")

        if user is not None:
            login(request, user)
            return redirect("home") 
        else:
            print(user)
            print("Wrong Info")
    context = {"page":"login"}
    return render(request, "base/login_register.html", context)

def home(request):
    for p in request.user.projects.all():
        print(p.name)
    context = {}
    return render(request, "base/home.html", context)

def view_project(request, pk):  # displays all small projects
    user = request.user
    project = LargeProject.objects.get(id=int(pk))
    large_project = LargeProject.objects.get(id=int(pk))
    sub_projects = large_project.sub_projects.all()

    context = {"sub_projects":sub_projects, "project":project}
    return render(request, "base/view_project.html", context)

def view_dashboard(request):
    user = request.user
    if request.method == "POST":
        pass
    context = {"projects":user.projects.all()}
    return render(request, "base/dashboard.html", context)


def create_large_project(request):
    user = request.user
    if request.method == "POST":
        name = request.POST.get("projectName")
        description = request.POST.get("projectDescription")
        due_date = request.POST.get("dueDate")
        Lproject = LargeProject.objects.create(name=name, description=description, date_created=str(dt.datetime.now()), due_date=due_date)
        user.projects.add(Lproject)
        Lproject.save()
        user.save()

        context = {"projects":user.projects.all()}
        return render(request, "base/dashboard.html", context)

    
    context = {}
    return render(request, "base/create_large_project.html" , context)

def create_small_project(request, pk):
    print(pk)
    large_project = LargeProject.objects.get(id=int(pk))
    print(large_project.name)
    if request.method == "POST":
        
        name = request.POST.get("projectName")
        description = request.POST.get("projectDescription")
        Sproject = SubProject.objects.create(name=name, description=description)
        large_project.sub_projects.add(Sproject)

        large_project.save()
        Sproject.save()
        return redirect("view-project", large_project.id)
        

    context = {"large_project":large_project}
    return render(request, "base/create_small_project.html", context)

def view_documents(request, pk):
    small_project = SubProject.objects.get(pk=int(pk))
    small_project.save()
    if request.method == "POST":
        document_name = request.POST.get("document_name")
        due_date = request.POST.get("due_date")
        doc_type = request.POST.get("type")
        document_number = request.POST.get("document_number")
        prompt = request.POST.get("prompt")
        doc = None
        if doc_type == "document":
            doc = Document(name=document_name,due_date=due_date, prompt=prompt, doc_type=doc_type, number=document_number)
            doc.save()
            small_project.documents.add(doc)
            doc.save()
            small_project.save()
        if doc_type == "ideation":
            ideation = Ideation(name=document_name, prompt=prompt)
            ideation.save()
            small_project.ideations.add(ideation)
            ideation.save()
            small_project.save()


    
    context = {"small_project":small_project, "documents":small_project.documents.all(), "ideations":small_project.ideations.all()}
    return render(request, "base/view_documents.html", context)

def document(request, pk):
    doc = Document.objects.get(id=int(pk))
    if request.method == "POST":
        updated_text = request.POST.get("update")
        doc.content = updated_text
        doc.save()
        for sp in SubProject.objects.all():
            if doc in list(sp.documents.all()):
                return redirect("view-documents", sp.id)
    context = {"document":doc}
    return render(request, "base/document.html", context)

def view_ideation(request, pk):
    ideation = Ideation.objects.get(id=int(pk))

    context = {"ideation":ideation}
    return render(request, "base/GoJSInput.html", context) 
def bot(request, pk):
    context = {}
    return render(request, "base/Bot2.html", context)