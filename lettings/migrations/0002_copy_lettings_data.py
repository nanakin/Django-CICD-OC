from django.apps import apps as global_apps
from django.db import migrations
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
#logger = logging.getLogger(__name__)

def cp_lettings(apps, schema_editor):
    try:
        OldAddress = apps.get_model("oc_lettings_site", "Address")
        OldLettings = apps.get_model("oc_lettings_site", "Letting")
    except LookupError:
        # The old app isn't installed.
        return

    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    for old_letting_object in OldLettings.objects.all():
        old_address_object = old_letting_object.address
        new_address_object = NewAddress.objects.create(
            number=old_address_object.number,
            street=old_address_object.street,
            city=old_address_object.city,
            state=old_address_object.state,
            zip_code=old_address_object.zip_code,
            country_iso_code=old_address_object.country_iso_code
        )
        new_letting_object = NewLetting.objects.create(
            title=old_letting_object.title,
            address=new_address_object)


class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(cp_lettings, migrations.RunPython.noop),
    ]
    dependencies = [
        ("oc_lettings_site", "0001_initial"),
        ("lettings", "0001_initial"),
    ]