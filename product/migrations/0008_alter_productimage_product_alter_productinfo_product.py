# Generated by Django 5.1.1 on 2024-11-20 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_rename_image1_productimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='product.product'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='product.product'),
        ),
    ]
