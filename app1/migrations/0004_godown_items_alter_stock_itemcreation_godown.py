# Generated by Django 4.0.2 on 2023-02-13 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_stock_itemcreation_godown'),
    ]

    operations = [
        migrations.CreateModel(
            name='Godown_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('per', models.CharField(max_length=100, null=True)),
                ('value', models.CharField(max_length=100, null=True)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
        migrations.AlterField(
            model_name='stock_itemcreation',
            name='godown',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.godown_items'),
        ),
    ]
