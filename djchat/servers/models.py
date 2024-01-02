from collections.abc import Iterable

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)
    description = models.TextField(_("Category Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(_("Server Name"), max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Server Owner"),
        on_delete=models.CASCADE,
        related_name="server_owner",
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_("Server Category"),
        on_delete=models.CASCADE,
        related_name="server_category",
    )
    description = models.CharField(
        _("Server Description"), max_length=250, blank=True, null=True
    )
    member = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name=_("Server Members")
    )

    class Meta:
        verbose_name = _("Server")
        verbose_name_plural = _("Servers")

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(_("Channel Name"), max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Channel Owner"),
        on_delete=models.CASCADE,
        related_name="channel_owner",
    )
    topic = models.CharField(_("Channel Topic"), max_length=100)
    server = models.ForeignKey(
        Server,
        verbose_name=_("Channel Server"),
        on_delete=models.CASCADE,
        related_name="channel_server",
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")

    def __str__(self):
        return self.name
