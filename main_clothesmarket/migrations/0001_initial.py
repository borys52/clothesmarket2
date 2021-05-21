# Generated by Django 3.2.2 on 2021-05-07 16:35

from django.db import migrations, models
import django.db.models.deletion
import main_clothesmarket.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, unique=True)),
                ('photo', models.ImageField(upload_to=main_clothesmarket.models.Category.get_file_name)),
                ('category_order', models.IntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('photo', models.ImageField(upload_to=main_clothesmarket.models.Kind.get_file_name)),
                ('kind_order', models.IntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('des', models.CharField(max_length=150, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_clothesmarket.category')),
            ],
        ),
    ]
