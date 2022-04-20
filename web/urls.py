from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.IndexView, name='home'),
    path('login/', LoginView.as_view(next_page='dashboard'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.RegisterView, name='register_url'),
    path('register_tipo/', views.Register_TipoView, name='register_tipo_url'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('update_profile/', views.profile, name='change_profile'),
    path('new_inmueble', views.New_Inmueble, name='new_inmueble'),
    path('update_inmueble/', views.Inmueble_Update, name= 'update_inmueble_url'),
    path('delete_inmueble/', views.Inmueble_Delete, name='delete_inmueble_url' )
]