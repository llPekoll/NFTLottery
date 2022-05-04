from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import get_history, get_lottery, get_trad, post_ticket

urlpatterns = [
    path("lottery/", get_lottery),
    path("ticket/", csrf_exempt(post_ticket)),
    path("history/", get_history),
    path("trad/", get_trad),
]
