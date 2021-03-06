# Generated by Django 4.0.4 on 2022-05-02 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pet', models.CharField(default='dog', max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100)),
                ('brief_description', models.TextField(blank=True)),
                ('detail_description', models.TextField(blank=True)),
                ('large_category', models.CharField(blank=True, max_length=100)),
                ('medium_category', models.CharField(blank=True, max_length=100)),
                ('small_category1', models.CharField(blank=True, max_length=100)),
                ('small_category2', models.CharField(blank=True, max_length=100)),
                ('small_category3', models.CharField(blank=True, max_length=100)),
                ('small_category4', models.CharField(blank=True, max_length=100)),
                ('small_category5', models.CharField(blank=True, max_length=100)),
                ('small_category6', models.CharField(blank=True, max_length=100)),
                ('small_category7', models.CharField(blank=True, max_length=100)),
                ('small_category8', models.CharField(blank=True, max_length=100)),
                ('retail_price', models.IntegerField(blank=True)),
                ('wholesale_price', models.IntegerField(blank=True)),
                ('product_count', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_content', models.TextField()),
                ('r_date', models.DateField(auto_now_add=True)),
                ('r_help', models.IntegerField(default=0)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('q_title', models.CharField(max_length=100)),
                ('q_content', models.TextField()),
                ('q_date', models.DateField(auto_now_add=True)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]
