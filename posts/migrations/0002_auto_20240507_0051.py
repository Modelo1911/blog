# Generated by Django 5.0.4 on 2024-05-07 00:51

from django.db import migrations, models

def populate_status(apps, schemaeditor):
    entries = {
        "draft": "A post that is not ready to be published", 
        "published": "A post avalible for all to see", 
        "archived": "An older post avalible in the archive only"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
