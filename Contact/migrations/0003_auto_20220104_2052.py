# Generated by Django 3.1.13 on 2022-01-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_alter_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
