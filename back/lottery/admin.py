from django.contrib import admin

from .models import Lottery, Ticket, Price, Winner

# Register your models here.


@admin.register(Winner)
class WinnerInline(admin.ModelAdmin):
    model = Winner


@admin.register(Price)
class PriceInline(admin.ModelAdmin):
    model = Price


class PriceInline(admin.TabularInline):
    model = Price


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    model = Ticket


@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    model = Lottery

    inlines = [
        PriceInline,
    ]
