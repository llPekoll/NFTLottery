from django.contrib import admin

from .models import Lottery, Ticket, Price, Winner, Trad

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

@admin.register(Trad)
class TradAdmin(admin.ModelAdmin):
    model = Trad


@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    model = Lottery
    list_per_page = 10
    list_display = [
        "__str__",
        "lotery_name",
        "lotery_wallet_address",
        "date_start",
        "ticket_price",
    ]
    ordering = ["ticket_price"]
    search_fields = ["lotery_name", "lotery_address"]
    readonly_fields = ["date_end"]
    inlines = [
        PriceInline,
    ]
