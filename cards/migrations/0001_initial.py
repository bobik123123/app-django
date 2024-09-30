# Generated by Django 4.2.16 on 2024-09-20 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
                ('icon', models.ImageField(upload_to='category/icon', verbose_name='Иконка')),
                ('icon_mobile', models.ImageField(upload_to='category/icon_mobile', verbose_name='Иконка')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item', verbose_name='изображение товара')),
                ('price', models.CharField(max_length=20, verbose_name='цена')),
                ('like', models.BooleanField(default=False, verbose_name='Нравится')),
                ('description', models.TextField(verbose_name='Описание')),
                ('create_at', models.DateTimeField(verbose_name='вРЕМЯ создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item', to='cards.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['create_at'],
            },
        ),
    ]
