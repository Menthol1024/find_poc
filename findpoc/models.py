from django.db import models


# Create your models here.
class ExchangeCode(models.Model):
    code = models.CharField(unique=True, max_length=80, db_index=True, primary_key=True)
    effective = models.BooleanField(default=False)
    pocnumber = models.BigIntegerField(default=0)


class Audit(models.Model):
    another = models.CharField(max_length=50, default='深山隐者')
    email = models.EmailField()
    package = models.TextField()
    version = models.CharField(max_length=30)
    review = models.IntegerField(default=0)
    place = models.CharField(blank=True,max_length=50)
    bugtype = models.TextField()
    desc = models.TextField()
    time = models.TimeField(auto_now_add=True)


class Links(models.Model):
    title = models.CharField(max_length=225)
    free = models.BooleanField(default=True)
    keywords = models.TextField(blank=True)
    description = models.TextField()
    url = models.CharField(max_length=30)

class Poc(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    another = models.CharField(max_length=50, default='深山隐者')
    email = models.EmailField()
    place = models.CharField(blank=True,max_length=50)
    package = models.TextField()
    version = models.CharField(max_length=30)
    bugtype = models.TextField()
    desc = models.TextField()
    time = models.DateTimeField(auto_now=True)
    frequency = models.IntegerField(default=0)
    free = models.BooleanField(default=True)

    def get_url(self):
        return '/findpoc/poc/{code}'.format(code=self.code)
