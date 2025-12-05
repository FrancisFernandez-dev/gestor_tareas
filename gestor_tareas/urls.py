from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tareas import views as tareas_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # rutas de autenticación
    path('login/',  auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', tareas_views.signup, name='signup'),

    # solución → agregar esta línea
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # rutas de tareas
    path('', include('tareas.urls')),
]
