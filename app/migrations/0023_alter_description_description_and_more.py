# Generated by Django 5.0.3 on 2024-03-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_description_description_en_description_title_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.TextField(default='النص باللغه باللغه العربية'),
        ),
        migrations.AlterField(
            model_name='description',
            name='description_en',
            field=models.TextField(default='النص باللغه الانجليزية'),
        ),
        migrations.AlterField(
            model_name='description',
            name='title',
            field=models.CharField(default='العنوان باللغة العربية', max_length=100),
        ),
        migrations.AlterField(
            model_name='description',
            name='title_en',
            field=models.CharField(default='النص باللغه الانجليزية', max_length=100),
        ),
        migrations.AlterField(
            model_name='lociation',
            name='text',
            field=models.CharField(default=' اسم الفرع باللغة العربية', max_length=100),
        ),
        migrations.AlterField(
            model_name='lociation',
            name='text_en',
            field=models.CharField(default=' اسم الفرع بالغه الانجليزية', max_length=100),
        ),
    ]
