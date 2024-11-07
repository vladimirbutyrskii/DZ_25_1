# Generated by Django 5.1.2 on 2024-11-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_payment_user_payment_payer_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={
                "ordering": ("payer", "payment_date"),
                "verbose_name": "оплата",
                "verbose_name_plural": "оплаты",
            },
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateField(auto_now=True, verbose_name="Дата оплаты"),
        ),
    ]