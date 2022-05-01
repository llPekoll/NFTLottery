from django.contrib import admin

from .models import Lottery, Ticket, Prices
# Register your models here.

@admin.register(Prices)
class PricesInline(admin.TabularInline):
    model = Prices

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    model = Ticket

@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    model = Lottery

    inlines = [
        PricesInline,
    ]
