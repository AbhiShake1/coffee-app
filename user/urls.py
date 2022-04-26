from django.urls import path

from .views import signup_user, login_user

urlpatterns = [
    # path(
    #     "login/",
    #     auth_views.LoginView.as_view(template_name="user/login.html", ),
    #     name="login",
    # ),
    path("login/", login_user, name="login"),
    path("signup/", signup_user, name="signup"),
]
