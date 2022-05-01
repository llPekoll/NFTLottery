from django.db import models
from django.utils.timezone import now


class Lottery(models.Model):
    lotery_nb = models.AutoField(primary_key=True)
    lotery_name = stripe_kyc = models.CharField(max_length=255, default="Lottery")
    date_start = models.DateTimeField(default=now)
    date_end = models.DateTimeField()
    ticket_price = models.IntegerField(default=10)
    
    def __str__(self):
        return str(self.lotery_nb)


class Ticket(models.Model):
    ticket_holder_wallet_address = models.CharField(max_length=128)
    date_start = models.DateTimeField(default=now)
    lotery_nb = models.ForeignKey(Lottery, related_name="tickets", on_delete=models.CASCADE)
    transation_id = models.CharField(max_length=128)

    def __str__(self):
        return str(self.ticket_holder_wallet_address)

class Price(models.Model):
    place = models.IntegerField(default=1)
    lotery_nb = models.ForeignKey(Lottery, related_name="prices", on_delete=models.CASCADE)
    gain = models.CharField(max_length=255)

    def __str__(self):
        return str(self.place)


class Winner(models.Model):
    
    lotery_nb = models.ForeignKey(Lottery, related_name="winner", on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name="winner", on_delete=models.CASCADE)
    price = models.ForeignKey(Price, related_name="winner", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.lotery_nb)
