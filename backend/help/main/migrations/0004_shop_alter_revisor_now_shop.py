# Generated by Django 4.2.14 on 2024-07-24 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_revisor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='revisor',
            name='now_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shop'),
        ),
    ]
