# Generated by Django 4.2.6 on 2023-11-23 10:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("petsapp", "0003_customer_log_order_shippingaddress_orderitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="order",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="product",
        ),
        migrations.RemoveField(
            model_name="shippingaddress",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="shippingaddress",
            name="order",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderItem",
        ),
        migrations.DeleteModel(
            name="ShippingAddress",
        ),
    ]
