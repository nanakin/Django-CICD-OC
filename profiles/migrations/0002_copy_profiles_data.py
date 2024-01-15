from django.apps import apps as global_apps
from django.db import migrations


def cp_profiles(apps, schema_editor):
    try:
        OldModel = apps.get_model("oc_lettings_site", "Profile")
    except LookupError:
        # The old app isn't installed.
        return

    NewModel = apps.get_model("profiles", "Profile")
    NewModel.objects.bulk_create(
        NewModel(user=old_object.user,
                 favorite_city=old_object.favorite_city)
        for old_object in OldModel.objects.all()
    )


class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(cp_profiles, migrations.RunPython.noop),
    ]
    dependencies = [
        ("oc_lettings_site", "0001_initial"),
        ("profiles", "0001_initial"),
    ]