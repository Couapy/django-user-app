from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/avatar/user_<id>/<filename>
    return 'avatar/user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    biography = models.TextField(
        verbose_name="Biographie",
        help_text="300 caractères maximum.",
        max_length=300,
        blank=True,
        null=True,
    )
    website = models.URLField(
        verbose_name="Site web",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        verbose_name="Photo de profil",
        upload_to=user_directory_path,
        null=True,
        blank=True,
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
