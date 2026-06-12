from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Appointment

# Home Page
def home(request):
    return render(request, 'clients/home.html')

# Register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard' if not user.is_superuser else 'admin_appointments')
    else:
        form = RegisterForm()
    return render(request, 'clients/register.html', {'form': form})


# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect based on role
            if user.is_superuser:
                return redirect('admin_appointments')
            else:
                return redirect('dashboard')
    return render(request, 'clients/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard
@login_required
def dashboard_view(request):
    if request.user.is_superuser:
        appointments = Appointment.objects.all().order_by('-timestamp')
    else:
        active_appointments = Appointment.objects.filter(student=request.user, completed=False).order_by('-timestamp')
        completed_appointments = Appointment.objects.filter(student=request.user, completed=True).order_by('-timestamp')
        return render(request, 'clients/dashboard.html', {
            'active_appointments': active_appointments,
            'completed_appointments': completed_appointments
        })

# Appointment taking
from .forms import AppointmentForm
@login_required
def take_appointment_view(request):
    if request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.student = request.user
            appointment.save()
            return redirect('dashboard')
    else:
        form = AppointmentForm()

    return render(request, 'clients/take_appointment.html', {'form': form})
# Edit appointment
@login_required
def edit_appointment_view(request, id):
    appointment = get_object_or_404(Appointment, id=id, student=request.user, completed=False)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'clients/edit_appointment.html', {'form': form})


@login_required
def delete_appointment_view(request, id):
    appointment = get_object_or_404(Appointment, id=id, student=request.user, completed=False)
    appointment.delete()
    return redirect('dashboard')



# Admin Panel for Viewing & Deleting All Appointments
@login_required
def admin_appointments_view(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    appointments = Appointment.objects.filter(completed=False)

    if request.method == 'POST':
        # If delete requested
        if 'delete_id' in request.POST:
            Appointment.objects.filter(id=request.POST.get('delete_id')).delete()

        # If mark as complete requested
        elif 'complete_id' in request.POST:
            Appointment.objects.filter(id=request.POST.get('complete_id')).update(completed=True)

    return render(request, 'clients/admin_appointments.html', {'appointments': appointments})

@login_required
def appointment_history_view(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    completed_appointments = Appointment.objects.filter(completed=True).order_by('-timestamp')
    return render(request, 'clients/appointment_history.html', {'appointments': completed_appointments})


# User Profiles
from .forms import UserUpdateForm, ProfileUpdateForm
@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'clients/profile.html', {'u_form': u_form, 'p_form': p_form})

