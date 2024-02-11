from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view-project/<str:pk>", views.view_project, name="view-project"),
    path("create-large-project/", views.create_large_project, name="create-large-project"),

    
    path("view-dashboard/", views.view_dashboard, name="view-dashboard"),
    path("view-small-projects/<str:pk>/", views.view_dashboard, name="view-dashboard"),
    path("create-small-project/<str:pk>/", views.create_small_project, name="create-small-project"),

    path("view-documents/<str:pk>/", views.view_documents, name="view-documents"),
    path("document/<str:pk>/", views.document, name="document"),

    path("document/<str:pk>/bot", views.bot, name="bot"),

    path("view-ideation/<str:pk>/", views.view_ideation, name="view-ideation"),

    #  path("view-small-project/<str:pk1>/<str:pk2>/", views.view_dashboard, name="view-dashboard"),




    path("login/", views.login_page, name="login-page"),
    path("register/", views.register, name="register"), 

    # path("bot/", views.bot,name="bot"),

]