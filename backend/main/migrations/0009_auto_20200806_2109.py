# Generated by Django 2.2.11 on 2020-08-06 21:09

from django.db import migrations

from main.text import pages


def forwards_func(apps, _schema_editor):
    User = apps.get_model("main", "User")
    for user in User.objects.all():
        progress = {}
        for page_slug, page in pages.items():
            if page_slug == user.page_slug:
                step_name = user.step_name
            else:
                step_name = page.step_names[-1]
            progress[page_slug] = {"step_name": step_name}
            if page_slug == user.page_slug:
                break
        user.json = {"pages_progress": progress}
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0008_user_json'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
