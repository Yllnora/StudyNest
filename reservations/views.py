from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_datetime
from django.contrib.admin.views.decorators import staff_member_required
from .models import Reservation
from .utils import is_reservation_available 


def home(request):
    """
    Startseite der Anwendung.
    """
    return render(request, 'reservations/home.html')


def login_view(request):
    """
    Benutzer-Login-View.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.is_staff:
                return redirect('admin_reservations')  
            return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'reservations/login.html', {'form': form})


def register(request):
    """
    Benutzer-Registrierungs-View.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'reservations/register.html', {'form': form})


@login_required
def dashboard(request):
    """
    Benutzer-Dashboard: Zeigt unterschiedliche Inhalte für Admins und normale Benutzer.
    """
    if request.user.is_staff:
      
        return redirect('admin_reservations')

    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/dashboard.html', {'reservations': reservations})


@login_required
def configure(request):
    """
    View zum Erstellen oder Konfigurieren einer neuen Reservierung.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        start_date = parse_datetime(request.POST.get('start_date'))
        end_date = parse_datetime(request.POST.get('end_date'))
        number_of_people = int(request.POST.get('number_of_people', 1))
        table_height = int(request.POST.get('table_height', 75))
        light_intensity = int(request.POST.get('light_intensity', 50))

        if is_reservation_available(start_date, end_date):
          
            Reservation.objects.create(
                user=request.user,
                name=name,
                email=email,
                start_date=start_date,
                end_date=end_date,
                number_of_people=number_of_people,
                table_height=table_height,
                light_intensity=light_intensity,
            )
            return redirect('reservation_success')
        else:

            return render(request, 'reservations/configure.html', {
                'error': 'The selected time slot is not available. Please choose a different time.',
                'name': name,
                'email': email,
                'start_date': request.POST.get('start_date'),
                'end_date': request.POST.get('end_date'),
                'number_of_people': number_of_people,
                'table_height': table_height,
                'light_intensity': light_intensity,
            })

    return render(request, 'reservations/configure.html')


def logout_view(request):
    """
    Benutzer-Logout-View.
    """
    logout(request)
    return redirect('home')


def reservation_success(request):
    """
    Erfolgsseite nach einer erfolgreichen Reservierung.
    """
    return render(request, 'reservations/reservation_success.html')


@login_required
def user_reservations(request):
    """
    Zeigt alle Reservierungen des eingeloggten Benutzers.
    """
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/user_reservations.html', {'reservations': reservations})


@staff_member_required
def admin_reservations(request):
    """
    Zeigt alle Reservierungen aller Benutzer an. Nur für Admins zugänglich.
    """
    reservations = Reservation.objects.all().order_by('start_date')
    return render(request, 'reservations/admin_reservations.html', {'reservations': reservations})
