from django.urls import path
from . import views

urlpatterns = [
    # --- Authentication Views --- #
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # --- Home Views --- #
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # --- Appointment Views --- #
    path('take_appointment/', views.take_appointment_view, name='take_appointment'),
    path('edit_appointment/<int:id>/', views.edit_appointment_view, name='edit_appointment'),
    path('delete_appointment/<int:id>/', views.delete_appointment_view, name='delete_appointment'),

    # --- Admin or Trainer Pages --- #
    path('trainer/appointments/', views.admin_appointments_view, name='admin_appointments'),
    path('trainer/appointments/history/', views.appointment_history_view, name='appointment_history'),

    # --- Profile Url --- #
    path('profile/', views.profile_view, name='profile'),

]
