# Generated by Django 5.0.3 on 2024-04-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_text_en_product_text_ru_product_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Для фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
