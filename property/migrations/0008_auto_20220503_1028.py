# Generated by Django 2.2.24 on 2022-05-03 07:28

from django.db import migrations
import phonenumbers


def owner_pure_phone_auto_filler(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        owner_parsed_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(owner_parsed_phone):
            flat.owner_pure_phone = phonenumbers.format_number(owner_parsed_phone,
                                                               phonenumbers.PhoneNumberFormat.E164)
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(owner_pure_phone_auto_filler)
        ]
