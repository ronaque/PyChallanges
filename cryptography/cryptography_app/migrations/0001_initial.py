# Generated by Django 5.0.2 on 2024-02-09 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userDocument', models.CharField(max_length=128)),
                ('creditCardToken', models.CharField(max_length=128)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
