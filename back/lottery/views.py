import json
from datetime import datetime
from operator import itemgetter

from django.db.models import Sum
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from .models import Lottery, Ticket, Trad, Winner


def get_lottery(request):
    """Returns the current lottery"""
    if not request.method == "GET":
        return JsonResponse({"error": {"message": "method not allowed"}}, status=405)
    lottery = Lottery.objects.last()
    if lottery.date_end.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
        return JsonResponse(
            {"error": {"message": "currently no lottery in the process"}}
        )

    lottery_dict = model_to_dict(lottery)
    sum = 0
    if lottery.cashin_display:
        tickets = lottery.tickets.all()
        for ticket in tickets:
            print("ticket.ticket_nb")
            print(ticket.ticket_nb)
            print("lottery.ticket_price")
            print(lottery.ticket_price)
            sum += ticket.ticket_nb * lottery.ticket_price
        lottery_dict["cash_in"] = sum
    lottery_dict["prices"] = [model_to_dict(price) for price in lottery.prices.all()]
    lottery_dict["prices"] = sorted(lottery_dict["prices"], key=itemgetter("place"))
    return JsonResponse(lottery_dict)


def post_ticket(request):
    """Inser new ticket in the database"""
    if not request.method == "POST":
        return JsonResponse({"error": {"message": "method not allowed"}}, status=405)
    body_unicode = request.body.decode("utf-8")
    body_data = json.loads(body_unicode)
    print(body_data)
    lottery = Lottery.objects.get(lotery_nb=body_data.get("lotery_nb"))
    Ticket.objects.create(
        ticket_holder_wallet_address=body_data.get("ticket_holder_wallet_address"),
        ticket_nb=body_data.get("ticket_nb"),
        lotery_nb=lottery,
        transation_id=body_data.get("transation_id"),
    )
    return JsonResponse({"success": True})


def get_history(request):
    """Returns tbe previous lottery with the winners"""
    last = Lottery.objects.last()
    winners = Winner.objects.filter(lotery_nb=last.lotery_nb - 1)
    winners_list = []
    for winner in winners:
        print("winner")
        print(winner)
        winner_dict = {}
        winner_dict["place"] = winner.price.place
        winner_dict["price"] = winner.price.gain
        winner_dict["address"] = winner.ticket.ticket_holder_wallet_address
        winners_list.append(winner_dict)
    winners_list = sorted(winners_list, key=itemgetter("place"))

    return JsonResponse({"winners": winners_list})


def get_trad(request):
    trads = Trad.objects.all()
    trads_dict = {trad.key: trad.content for trad in trads}
    return JsonResponse(trads_dict)
