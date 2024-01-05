from collections.abc import Iterable

from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from .validators import validate_icon_image_size, validate_image_extension


def category_icon_file_path(instance, filename):
    return f"category/{instance.id}/category_icon/{filename}"


def channel_icon_file_path(instance, filename):
    return f"channel/{instance.id}/channel_icon/{filename}"


def channel_banner_file_path(instance, filename):
    return f"channel/{instance.id}/channel_banner/{filename}"


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)
    description = models.TextField(_("Category Description"), blank=True, null=True)
    icon = models.FileField(
        _("Category Icon"), upload_to=category_icon_file_path, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id:
            existing_category = get_object_or_404(Category, id=self.id)
            if existing_category.icon != self.icon:
                existing_category.icon.delete(save=False)
        super(Category, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="servers.Category")
    def category_file_pre_delete(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)


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
    banner = models.ImageField(
        _("Banner"),
        upload_to=channel_banner_file_path,
        blank=True,
        null=True,
        validators=[validate_image_extension],
    )
    icon = models.ImageField(
        _("Icon"),
        upload_to=channel_icon_file_path,
        blank=True,
        null=True,
        validators=[validate_icon_image_size, validate_image_extension],
    )

    def save(self, *args, **kwargs):
        if self.id:
            existing_channel = get_object_or_404(Channel, id=self.id)
            if existing_channel.icon != self.icon:
                existing_channel.icon.delete(save=False)
            if existing_channel.banner != self.banner:
                existing_channel.banner.delete(save=False)
        super(Channel, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="servers.Channel")
    def channel_file_pre_delete(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon" or field.name == "banner":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")

    def __str__(self):
        return self.name
