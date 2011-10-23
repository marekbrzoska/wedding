from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200, blank=True, null=True)
    buyer_declaration_date = models.DateTimeField(null=True, default=None)


class Link(models.Model):
    gift = models.ForeignKey(Gift)
    href = models.CharField(max_length=200)
