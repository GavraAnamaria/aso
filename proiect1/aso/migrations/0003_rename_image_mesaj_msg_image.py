# Generated by Django 4.1.2 on 2022-12-07 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aso', '0002_rename_question_text_mesaj_msg_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mesaj',
            old_name='image',
            new_name='msg_image',
        ),
    ]