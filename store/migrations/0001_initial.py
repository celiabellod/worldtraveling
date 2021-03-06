# Generated by Django 3.0.3 on 2020-03-20 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('reference', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date_travel', models.DateField()),
                ('available', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('picture', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Contact')),
                ('travel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Travel')),
            ],
        ),
    ]
