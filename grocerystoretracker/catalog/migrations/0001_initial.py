# Generated by Django 2.2.14 on 2020-07-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consumers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter your first name', max_length=100)),
                ('last_name', models.CharField(help_text='Enter your last name', max_length=100)),
                ('budget', models.IntegerField(help_text='Enter your max budget')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('F', 'FRUIT'), ('V', 'VEGETABLES'), ('D', 'DAIRY'), ('M', 'MEAT'), ('C', 'CARBS'), ('JF', 'JUNK FOOD')], max_length=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='stores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your first name', max_length=20)),
            ],
        ),
    ]
