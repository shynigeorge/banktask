# Generated by Django 3.2.18 on 2023-03-05 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('material', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.branch')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.district')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district'),
        ),
    ]
