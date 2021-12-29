# Generated by Django 3.2.8 on 2021-12-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='profile',
            name='image2',
            field=models.ImageField(max_length=150, null=True, upload_to='./static/images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='image3',
            field=models.ImageField(max_length=150, null=True, upload_to='./static/images/'),
        ),
    ]
