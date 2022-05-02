from .views import get_lottery, post_ticket, get_history

urlpatterns = [
    path("lottery/", get_lottery),
    path("ticket/", post_ticket),
    path("history/", get_history),
]
