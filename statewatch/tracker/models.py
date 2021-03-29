from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.state} ({self.abbreviation})"

class Body(models.Model):
    body = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.body}"

class Legislature(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    body = models.ForeignKey(Body, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.state} {self.body}"

class Bills(models.Model):
    legBody = models.ForeignKey(Legislature, on_delete=models.PROTECT)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    sponsor = models.CharField(max_length=64)
    text = models.URLField(max_length=200)
    date = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.code} {self.name} Last updated: {self.date}"