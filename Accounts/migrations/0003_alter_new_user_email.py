# Generated by Django 4.2.4 on 2023-08-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_new_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Email address '),
        ),
    ]
