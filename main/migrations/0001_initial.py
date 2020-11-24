# Generated by Django 2.2 on 2020-11-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateTimeField(auto_now_add=True)),
                ('usd', models.DecimalField(decimal_places=3, max_digits=10)),
                ('eur', models.DecimalField(decimal_places=3, max_digits=10)),
                ('rur', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'verbose_name': 'Курсы валют',
                'ordering': ['date_today'],
            },
        ),
    ]