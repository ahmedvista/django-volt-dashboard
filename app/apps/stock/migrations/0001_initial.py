# Generated by Django 4.2.3 on 2023-07-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Name')),
                ('count', models.PositiveIntegerField(default=0)),
                ('serial_number', models.CharField(blank=True, max_length=150, null=True, verbose_name='Serial Number')),
                ('status', models.IntegerField(choices=[(0, 'IN SUPPLY ORDER'), (1, 'IN STOCK'), (2, 'IN FABRICATION'), (3, 'OUT ORDER'), (4, 'SOLD'), (5, 'RETURNED'), (6, 'IN MAINTENANCE'), (7, 'DAMAGED')], default=0, verbose_name='Stock Item Status')),
                ('cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Cost Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('raw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.raw', verbose_name='Raw')),
            ],
            options={
                'verbose_name': 'Raw Material Stock',
                'verbose_name_plural': 'Raw Materials Stock',
                'db_table': 'Raw_Materials_Stock',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Name')),
                ('count', models.PositiveIntegerField(default=0)),
                ('serial_number', models.CharField(blank=True, max_length=150, null=True, verbose_name='Serial Number')),
                ('status', models.IntegerField(choices=[(0, 'IN SUPPLY ORDER'), (1, 'IN STOCK'), (2, 'IN FABRICATION'), (3, 'OUT ORDER'), (4, 'SOLD'), (5, 'RETURNED'), (6, 'IN MAINTENANCE'), (7, 'DAMAGED')], default=0, verbose_name='Stock Item Status')),
                ('cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Cost Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Raw')),
            ],
            options={
                'verbose_name': 'Product Stock',
                'verbose_name_plural': 'Products Stock',
                'db_table': 'Products_Stock',
                'ordering': ('-created_at',),
            },
        ),
    ]
