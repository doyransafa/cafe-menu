# Generated by Django 5.0.1 on 2024-01-13 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.FloatField()),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='VariantGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.product')),
            ],
        ),
        migrations.CreateModel(
            name='VariantItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('extra_price', models.FloatField()),
                ('variant_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.variantgroup')),
            ],
        ),
    ]
