from django.contrib import admin

from .models import Lottery, Price, Ticket, Trad, Winner

# Register your models here.


@admin.register(Winner)
class WinnerInline(admin.ModelAdmin):
    model = Winner
    list_display = [
        "lotery_nb",
        "ticket",
        "price",
    ]


# @admin.register(Price)
# class PriceInline(admin.ModelAdmin):
#     model = Price


class PriceInline(admin.TabularInline):
    model = Price


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = [
        "ticket_holder_wallet_address",
        "lotery_nb",
        "date",
    ]
    search_fields = ["lotery_nb__lotery_nb"]


@admin.register(Trad)
class TradAdmin(admin.ModelAdmin):
    model = Trad
    search_fields = ["key", "content"]


@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    model = Lottery
    list_per_page = 10
    list_display = [
        "lotery_name",
        "lotery_wallet_address",
        "date_start",
        "ticket_price",
        "__str__",
    ]
    ordering = ["ticket_price"]
    search_fields = ["lotery_name", "lotery_address"]
    readonly_fields = ["date_end"]
    inlines = [
        PriceInline,
    ]
