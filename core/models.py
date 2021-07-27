from django.db import models
from django.utils.translation import gettext_lazy as _


class Core(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class App(models.Model):
    label = models.CharField(_("label"), max_length=100)
    core = models.ForeignKey(
        Core, verbose_name=_("core"), related_name="apps", on_delete=models.CASCADE
    )
