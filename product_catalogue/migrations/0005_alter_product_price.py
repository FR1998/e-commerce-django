# Generated by Django 4.2.3 on 2023-07-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalogue', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
