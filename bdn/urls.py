from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
  path("", views.home, name="home"),
  path("signup", views.signup, name="signup"),
  path("signin", views.signin, name="signin"),
  path("signout", views.signout, name="signout"),
  path("app/", include("app.urls")),
  path("admin/", admin.site.urls),
  path("modelo/", include("modelo.urls")),
]
