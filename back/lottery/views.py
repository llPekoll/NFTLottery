from datetime import datetime

import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from .models import Lottery, Ticket, Trad
from datetime import datetime


def get_lottery(request):
    """ Returns the current lottery """
    if not request.method == "GET":
        return JsonResponse({"error": {"message": "method not allowed"}}, status=405)
    lottery = Lottery.objects.last()
    if lottery.date_end.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
        return JsonResponse(
            {"error": {"message": "currently no lottery in the process"}}
        )

    lottery_dict = model_to_dict(lottery)
    lottery_dict["prices"] = [model_to_dict(price) for price in lottery.prices.all()]
    return JsonResponse(lottery_dict)


def post_ticket(request):
    """ Inser new ticket in the database """
    if not request.method == "POST":
        return JsonResponse({"error": {"message": "method not allowed"}}, status=405)
    body_unicode = request.body.decode("utf-8")
    body_data = json.loads(body_unicode)
    lottery = Lottery.objects.get(pk=body_data.get("lotery_nb"))
    Ticket.objects.create(
        ticket_holder_wallet_address=body_data.get("wallet"),
        lotery_nb=lottery,
        transation_id=body_data.get("lotery_nb"),
    )
    return JsonResponse({"success": True})


def get_history(request):
    """ Returns tbe previous lottery with the winners """
    lotteries = Lottery.objects.all().order_by("lotery_nb")

    # lotteries_dict = [model_to_dict(lottery)for lottery in lotteries][-2:]
    lotteries_dict = []
    for lottery in lotteries[-3:]:
        lottery_dict = model_to_dict(lottery)
        lottery_dict["winners"] = [
            model_to_dict(winner) for winner in lottery.winners.all()
        ]
        lottery_dict["prices"] = [
            model_to_dict(price) for price in lottery.prices.all()
        ]
        lotteries_dict.append(lottery_dict)
    print(lotteries_dict)
    return JsonResponse({"lotteries": lotteries_dict})


def get_trad(request):
    trads = Trad.objects.all()
    trads_dict = {trad["key"]: trad["content"] for trad in trads}
    return JsonResponse(trads_dict)
    