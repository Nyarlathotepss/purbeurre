from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user_account/', views.user_account, name='user_page')

]