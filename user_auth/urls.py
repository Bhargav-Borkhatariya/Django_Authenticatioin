from user_auth import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("signin", views.signin, name='signin'),
    path("signup", views.signup, name='signup'),
    path("signout", views.signout, name='signout'),
    path("changepassword", views.changepass, name='changepass'),
    path("addbook", views.add_book, name='add_book'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("editbook/<int:id>", views.edit_book, name='editbook'),
    path("deletebook/<int:id>", views.delete_book, name='deletebook'),
]
