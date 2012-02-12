from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=200, verbose_name='Gift')
    buyer = models.CharField(max_length=200, blank=True, null=True)
    notice = models.TextField(blank=True, null=True)
    buyer_declaration_date = models.DateTimeField(blank=True, null=True, default=None)

    def __unicode__(self):
        buyer = u" ({0})".format(self.buyer) if self.buyer else ''
        return self.name + buyer


class Link(models.Model):
    gift = models.ForeignKey(Gift, related_name="links")
    href = models.CharField(max_length=200, verbose_name='example link')

    def __unicode__(self):
        return self.gift.__unicode__() + u" {0}".format(self.href)
