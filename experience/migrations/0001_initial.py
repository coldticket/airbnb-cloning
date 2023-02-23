# Generated by Django 4.1.7 on 2023-02-23 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('detail', models.CharField(blank=True, max_length=250, null=True)),
                ('explanation', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('country', models.CharField(default='south korea', max_length=50)),
                ('city', models.CharField(default='seoul', max_length=80)),
                ('name', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=20)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
