# Generated by Django 3.1.7 on 2021-04-05 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20210405_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciever', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.customer')),
            ],
        ),
    ]
