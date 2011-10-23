from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200, blank=True, null=True)
    buyer_declaration_date = models.DateTimeField(blank=True, null=True, default=None)

    def __unicode__(self):
        return self.name


class Link(models.Model):
    gift = models.ForeignKey(Gift, related_name="links")
    href = models.CharField(max_length=200)
