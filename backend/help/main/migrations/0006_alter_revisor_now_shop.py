# Generated by Django 4.2.14 on 2024-07-24 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_revisor_now_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisor',
            name='now_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shop'),
        ),
    ]
