# Generated by Django 3.1.6 on 2021-03-07 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0004_perfil_bloqueado'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
