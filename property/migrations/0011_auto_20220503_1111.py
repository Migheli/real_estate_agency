# Generated by Django 2.2.24 on 2022-05-03 08:11

from django.db import migrations

def owner_objects_autocreator(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner_name=flat.owner,
                                    owners_phonenumber=flat.owners_phonenumber,
                                    owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220503_1105'),
    ]

    operations = [
        migrations.RunPython(owner_objects_autocreator)
    ]
