# Generated by Django 4.0.4 on 2022-05-02 10:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('u_id', models.CharField(max_length=20)),
                ('u_pw', models.CharField(max_length=20)),
                ('u_name', models.CharField(default='', max_length=20)),
                ('u_phone', models.CharField(blank=True, max_length=20)),
                ('u_post', models.CharField(blank=True, max_length=20)),
                ('u_date', models.DateField(auto_now_add=True)),
                ('u_drop', models.BooleanField(default=False)),
                ('u_shopping_cart', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
            ],
        ),
    ]
