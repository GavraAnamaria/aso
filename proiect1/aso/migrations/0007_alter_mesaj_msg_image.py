# Generated by Django 4.1.2 on 2023-01-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso', '0006_alter_mesaj_msg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesaj',
            name='msg_image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
