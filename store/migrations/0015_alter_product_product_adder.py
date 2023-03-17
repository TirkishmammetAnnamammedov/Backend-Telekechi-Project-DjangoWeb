# Generated by Django 4.0.5 on 2023-03-08 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_product_adder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_products', to='store.userclient', to_field='phone_number'),
        ),
    ]