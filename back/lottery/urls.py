from django.urls import path
from .views import get_lottery, post_ticket, get_history, get_trad
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("lottery/", get_lottery),
    path("ticket/", csrf_exempt(post_ticket)),
    path("history/", get_history),
    path("trad/", get_trad),
]
