# Generated by Django 2.1.2 on 2018-11-02 11:15

from django.db import migrations
from accounts.models import AccountUser


def create_default_user(apps, schema_editor):
    usr = AccountUser(username='admin',
                      is_staff=True,
                      is_superuser=True,)
    usr.set_password('admin')
    usr.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_default_user,
            lambda  x,y: (x,y)
        )
    ]
