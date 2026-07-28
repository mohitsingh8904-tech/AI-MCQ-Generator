from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("upload/", views.upload_notes, name="upload"),

    path("quiz/", views.quiz_view, name="quiz"),

    path("result/", views.result_view, name="result"),

    path("my-tests/", views.my_tests, name="my_tests"),

    path(
        "result/<int:result_id>/pdf/",
        views.download_result_pdf,
        name="result_pdf",
    ),

    path("about/", views.about_view, name="about"),

    path("blog/", views.blog_view, name="blog"),
]