from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Travel, Contact, Booking
from .form import ContactForm, BookingForm
from django.db import transaction, IntegrityError

def index(request):
    travels_in_searchbar = Travel.objects.all()
    query = request.GET.get('query')
    if not query :
        travels = Travel.objects.all()
    else:
        travels = Travel.objects.filter(destination__icontains=query)
        if not travels.exists():
            travels = Travel.objects.filter(date_start__contains=query)
            if not travels.exists():
                travels = Travel.objects.filter(nb_people__contains=query)
            else:
                travels = "Nous n'avons trouvé aucun voyage correspondant à votre demande!"
    context = {
        'travels': travels,
        'travels_in_searchbar': travels_in_searchbar
    }
    return render(request,'store/index.html', context)


class Detail(DetailView):
    context_object_name = "travel"
    model = Travel
    template_name = "store/detail.html"


@transaction.atomic
def booking(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id)
    form = BookingForm()
    context = {
        'travel': travel,
        'form': form
    }
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        contact = Contact.objects.create(
                            email = email,
                            name = name
                        )
                    else:
                        contact = contact.first()
                    
                    travel = get_object_or_404(Travel, id=travel_id)
                    booking = Booking.objects.create(
                        travel = travel,
                        contact = contact
                    )
            except IntegrityError:
                    form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre demande de réservation."

            message = "Merci, votre réservation nous à bien été parvenue, vous recevrez un e-mail de confirmation dans quelques jours !"
            context = {
                'message': message,
                'travel': travel
            }
            return render(request, 'store/booking.html', context )
        else:
            form = ReservationForm()
        context = {
            'form': form,
            'errors': form.errors.items(),
            'travel': travel
        }
    return render(request, 'store/booking.html', context)
           

def contact(request, travel_id=0):
    if travel_id == 0 :
        travel = Travel.objects.all()
    else:
        travel = Travel.objects.get(pk=travel_id)

    form = ContactForm()
    context = {
        'form': form,
        'travel' : travel
        
    }

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        contact = Contact.objects.create(
                            email = email,
                            name = name,
                            message = message
                        )
                    else:
                        contact = contact.first()
                        contact.message = message
        
            except IntegrityError:
                    form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre demande de réservation."

            message = "Merci, votre message à bien été envoyé, nous vous repondrons au plus vite !"
            context = {
                'message': message,
                
            }
            return render(request, 'store/contact.html', context )

        else:
            form = ContactForm()
            context = {
                'form' : form,
                'errors' : form.errors.items()
            }
    return render(request, 'store/contact.html', context)
