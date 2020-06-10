from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    sads = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_sads",
    )
    edfqwef = models.OneToOneField(
        "home.HomePage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_edfqwef",
    )
    fdcwefq = models.ManyToManyField(
        "users.User", blank=True, related_name="customtext_fdcwefq",
    )
    ewdwqe = models.ManyToManyField(
        "home.HomePage", blank=True, related_name="customtext_ewdwqe",
    )
    eed = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_eed",
    )
    edwqdwed = models.OneToOneField(
        "home.HomePage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_edwqdwed",
    )
    eweew = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
