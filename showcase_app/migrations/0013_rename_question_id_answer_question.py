# Generated by Django 4.2.3 on 2023-07-29 10:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("showcase_app", "0012_rename_question_answer_question_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer",
            old_name="question_id",
            new_name="question",
        ),
    ]