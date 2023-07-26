# Generated by Django 4.2.3 on 2023-07-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("showcase_app", "0008_answer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.AddField(
            model_name="product",
            name="images",
            field=models.FileField(blank=True, null=True, upload_to="photos/%Y/%m/%d"),
        ),
    ]
