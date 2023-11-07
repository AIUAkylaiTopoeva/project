# Generated by Django 4.2.7 on 2023-11-07 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=60)),
                ('slug', models.SlugField(blank=True, max_length=60, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='posts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uploated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='podtd', to='recipes.category')),
            ],
        ),
    ]