from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import formularioF
from .models import GeneralData, FactIncidences, UserProfile, DimSection
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.dateparse import parse_date

# Create your views here.

def home (request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()  # Esta línea es redundante ya que create_user guarda el usuario.
                login(request,user)
                return redirect('formulario')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error' : 'Usuario existente'
                    }) 
            except Exception as e:
                # Considerar manejar o registrar el error específico para depuración.
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error' : 'Error al crear el usuario'
                })
                   
        else:
            return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error' : 'Password no existente'
                })
        
                   
@login_required
def formulario(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        is_admin = request.user.is_superuser
    except UserProfile.DoesNotExist:
        return HttpResponse("No hay un perfil de usuario asociado a este usuario.")

    main_sections = DimSection.objects.values_list('main_section', flat=True).distinct()
    inner_sections = DimSection.objects.none()
    locations = []  # Inicializa una lista vacía para las ubicaciones

    # Si el usuario es administrador, obtén la lista de ubicaciones
    if is_admin:
        locations = DimSection.objects.values_list('location_name', flat=True)  # Ajusta 'name' según tu modelo de Location

    if request.method == 'POST':
        form = formularioF(request.POST, request.FILES)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.user = request.user
            incidencia.save()
            return redirect('formulario')
        else:
            return render(request, 'formulario.html', {'form': form, 'error': 'Hubo un error con el formulario', 'main_sections': main_sections, 'inner_sections': inner_sections, 'is_admin': is_admin, 'locations': locations})
    else:
        form = formularioF()
        return render(request, 'formulario.html', {
            'form': form, 
            'main_sections': main_sections, 
            'inner_sections': inner_sections,
            'is_admin': is_admin,
            'locations': locations  # Asegúrate de pasar las ubicaciones al contexto
        })
    
def signout (request):
    logout(request)

    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario no encontrado'
            })
        else: 
            login(request,user)
            return redirect('formulario')
        
@login_required
def incidencias(request):
    user = request.user

    # Obtener los IDs de las incidencias asociadas al usuario autenticado
    incidencias_ids = FactIncidences.objects.filter(user=user).values_list('id_incidence', flat=True)

    # Filtrar los datos de GeneralData basándose en las incidencias asociadas al usuario autenticado
    general_data = GeneralData.objects.filter(incidence_id__in=incidencias_ids)

    main_sections = general_data.values_list('main_section', flat=True).distinct()
    inner_sections = general_data.values_list('inner_section', flat=True).distinct()

    # Filtros
    main_section_query = request.GET.get('main_section', '')
    inner_section_query = request.GET.get('inner_section', '')

    incidencias = general_data

    if main_section_query:
        incidencias = incidencias.filter(main_section__icontains=main_section_query)

    if inner_section_query:
        incidencias = incidencias.filter(inner_section__icontains=inner_section_query)
    
    incidencias_count = incidencias.values('main_section').annotate(total=Count('main_section')).order_by()

    return render(request, 'incidencias.html', {
        'incidencias': incidencias,
        'main_sections': main_sections,
        'inner_sections': inner_sections,
        'incidencias_count': incidencias_count
    })

from django.db.models import Count



@user_passes_test(lambda u: u.is_superuser)
def incidenciasOverview(request):
    locations = GeneralData.objects.values_list('location_name', flat=True).distinct()

    # Inicia el queryset general
    general_data = GeneralData.objects.all()

    # Recupera los valores de los filtros desde el request
    location_query = request.GET.get('location_name', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # Aplica el filtro de ubicación si se especifica
    if location_query:
        general_data = general_data.filter(location_name=location_query)

    # Aplica los filtros de fecha si se especifican
    if start_date:
        start_date_parsed = parse_date(start_date)
        general_data = general_data.filter(registro_fecha_hora__date__gte=start_date_parsed)
    if end_date:
        end_date_parsed = parse_date(end_date)
        general_data = general_data.filter(registro_fecha_hora__date__lte=end_date_parsed)

    # Datos para la primera tabla: Total de incidencias por ubicación
    location_summary = general_data.values('location_name').annotate(total=Count('incidence_id')).order_by('-total')

    # Datos para la segunda tabla: Resumen de incidencias por ubicación y sección principal
    summaries = general_data.values('location_name', 'main_section').annotate(num_incidencias=Count('incidence_id')).order_by('location_name', 'main_section')

    # Calcula el total general de incidencias basado en 'summaries'
    total_general_incidencias = sum(item['num_incidencias'] for item in summaries)

    return render(request, 'overview.html', {
        'locations': locations,
        'location_summary': location_summary,
        'summaries': summaries,
        'total_general_incidencias': total_general_incidencias,
        # Pasa los filtros al template para mantener los valores en los campos de filtro
        'filter': {
            'location_name': location_query,
            'start_date': start_date,
            'end_date': end_date,
        }
    })

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)


from django.http import JsonResponse
from .models import DimSection

def get_inner_sections(request):
    main_section = request.GET.get('main_section', '')
    inner_sections = DimSection.objects.filter(main_section=main_section).values('inner_section').distinct()
    inner_sections_list = [{'id': section['inner_section'], 'name': section['inner_section']} for section in inner_sections]
    return JsonResponse({'inner_sections': inner_sections_list})

