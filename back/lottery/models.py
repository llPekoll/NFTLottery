from django.db import models
from django.utils.timezone import now, timedelta


class Lottery(models.Model):
    lotery_nb = models.AutoField(primary_key=True)
    lotery_name = models.CharField(max_length=255, default="Lottery")
    lotery_wallet_address = models.CharField(max_length=255, default="0xfasdf")
    date_start = models.DateTimeField(default=now)
    date_end = models.DateTimeField(default=now)
    duration = models.IntegerField(default=7)
    ticket_price = models.IntegerField(default=10)

    def save(self, *args, **kwargs):
        self.date_end = self.date_start + timedelta(days=self.duration)
        super(Lottery, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.lotery_nb)


class Ticket(models.Model):
    ticket_holder_wallet_address = models.CharField(max_length=128)
    date = models.DateTimeField(default=now)
    lotery_nb = models.ForeignKey(
        Lottery, related_name="tickets", on_delete=models.CASCADE
    )
    transation_id = models.CharField(max_length=128)

    def __str__(self):
        return str(self.ticket_holder_wallet_address)


class Price(models.Model):
    place = models.IntegerField(default=1)
    lotery_nb = models.ForeignKey(
        Lottery, related_name="prices", on_delete=models.CASCADE
    )
    gain = models.CharField(max_length=255)

    def __str__(self):
        return str(self.place)


class Winner(models.Model):

    lotery_nb = models.ForeignKey(
        Lottery, related_name="winners", on_delete=models.CASCADE
    )
    ticket = models.ForeignKey(Ticket, related_name="winners", on_delete=models.CASCADE)
    price = models.ForeignKey(Price, related_name="winners", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.lotery_nb)


class Trad(models.Model):
    
    key = models.CharField(max_length=32, unique=True)
    content = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.key