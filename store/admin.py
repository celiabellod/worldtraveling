from django.contrib import admin

from .models import Booking, Contact, Travel





class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    readonly_fields = ["travel", "contact", "contacted"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,]
    search_fields = ['email', 'name']

    def has_add_permission(self, request):
        return False


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    search_fields = ['destination', 'reference']
    list_filter = ['available']
    inlines = [BookingInline,]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['contacted']
    readonly_fields = ["travel", "contact"]
    search_fields = ['email', 'name']

    def has_add_permission(self, request):
        return False
    






    


