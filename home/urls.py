from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
     path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)