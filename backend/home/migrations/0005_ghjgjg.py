# Generated by Django 2.2.13 on 2020-06-10 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20200610_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ghjgjg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgkjg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ghjgjg_hgkjg', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
