from datetime import datetime
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from .models import Lottery, Ticket, Price, Winner
fomr datetime import datetime

def get_lottery():
    try:
        lottery = Lottery.objects.get(date_end<datetime.now())
    except Lottery.DoesNotExist:
        return JsonResponse({"error":{"message":"no lottery in process"}},status=404)
    lottery_dict = model_to_dict(lottery)
    lottery_dict["prices"] = [model_to_dict(price) for price in lottery.prices.all()]
    return JsonResponse(lottery_dict)

def post_ticket():
    pass
    
def get_history():
    pass