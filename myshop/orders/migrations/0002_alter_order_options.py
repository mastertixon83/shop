# Generated by Django 3.2.5 on 2021-08-05 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]