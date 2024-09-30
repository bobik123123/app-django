# Generated by Django 4.2.16 on 2024-09-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['ordering'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='item',
            name='ordering',
            field=models.PositiveIntegerField(default=0),
        ),
    ]