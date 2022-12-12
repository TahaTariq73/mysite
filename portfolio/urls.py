from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about/", views.about, name="About"),
    path("signup/", views.signup, name="SignUp"),
    path("login/", views.login, name="Login"),
    path("logout/", views.logout, name="Logout"),
    path("blog/", views.blog, name="Blog"),
    path("blog/post/<int:id>/", views.post, name="Post"),
    path("comment/<int:id>/", views.comment, name="Comment")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
