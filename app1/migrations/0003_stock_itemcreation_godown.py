# Generated by Django 4.0.2 on 2023-02-13 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_ledger_chequebook_ledger_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_itemcreation',
            name='godown',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.creategodown'),
        ),
    ]
