# Generated by Django 3.2.8 on 2021-12-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=150, null=True, upload_to='./static/images/')),
                ('constructions', models.TextField(blank=True, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Example@mail.com')),
            ],
        ),
    ]