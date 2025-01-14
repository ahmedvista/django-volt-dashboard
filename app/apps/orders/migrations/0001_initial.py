# Generated by Django 4.2.3 on 2023-07-15 05:28

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='First Name')),
                ('surname', models.CharField(blank=True, max_length=75, null=True, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=75, null=True, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=140, null=True, verbose_name='Address')),
                ('company', models.CharField(blank=True, max_length=140, null=True, verbose_name='Company')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table': 'Customers',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Order Title')),
                ('status', models.IntegerField(choices=[(0, 'PENDING'), (1, 'IN SHIPPING'), (2, 'SHIPPED'), (3, 'RETURNED'), (4, 'PARTIALLY RETURNED')], default=0, verbose_name='Order Status')),
                ('delivery_date', models.CharField(blank=True, max_length=150, null=True, verbose_name='Delivery Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('data', models.JSONField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Price')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.client', verbose_name='Customer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'Orders',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='First Name')),
                ('surname', models.CharField(blank=True, max_length=75, null=True, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=75, null=True, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=140, null=True, verbose_name='Address')),
                ('company', models.CharField(blank=True, max_length=140, null=True, verbose_name='Company')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
                'db_table': 'Suppliers',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='SupplyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Order Title')),
                ('status', models.IntegerField(choices=[(0, 'PENDING'), (1, 'IN SHIPPING'), (2, 'SHIPPED'), (3, 'RETURNED'), (4, 'PARTIALLY RETURNED')], default=0, verbose_name='Order Status')),
                ('delivery_date', models.CharField(blank=True, max_length=150, null=True, verbose_name='Delivery Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated Data')),
                ('data', models.JSONField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Price')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.supplier', verbose_name='Supplier')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Supply Order',
                'verbose_name_plural': 'Supply Orders',
                'db_table': 'Supply_Orders',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='SupplyOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('1'), max_digits=10, null=True, verbose_name='Order Quantity')),
                ('actual_quantity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=10, null=True, verbose_name='Fulfilled Order Quantity')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Cost Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated Data')),
                ('raw_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.rawstock', verbose_name='Raw Stock')),
                ('supply_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.supplyorder', verbose_name='Supply Order')),
            ],
            options={
                'verbose_name': 'Supply Order Item',
                'verbose_name_plural': 'Supply Order Items',
                'db_table': 'Supply_Order_Items',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='RawOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('1'), max_digits=10, null=True, verbose_name='Order Quantity')),
                ('actual_quantity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=10, null=True, verbose_name='Fulfilled Order Quantity')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Cost Price')),
                ('total_sale', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Sale Price')),
                ('total_profit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Profit')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated Data')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
                ('raw_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.rawstock', verbose_name='Raw Stock')),
            ],
            options={
                'verbose_name': 'Raw Order Item',
                'verbose_name_plural': 'Raw Order Items',
                'db_table': 'Raw_Order_Items',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('1'), max_digits=10, null=True, verbose_name='Order Quantity')),
                ('actual_quantity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=10, null=True, verbose_name='Fulfilled Order Quantity')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Cost Price')),
                ('total_sale', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Sale Price')),
                ('total_profit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Profit')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Data')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated Data')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
                ('product_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.productstock', verbose_name='Product Stock')),
            ],
            options={
                'verbose_name': 'Product Order Item',
                'verbose_name_plural': 'Product Order Items',
                'db_table': 'Product_Order_Items',
                'ordering': ('-created_at',),
            },
        ),
    ]
