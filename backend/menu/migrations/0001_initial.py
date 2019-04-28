# Generated by Django 2.2 on 2019-04-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('VEG', 'Vegetarian'), ('SO', 'Special offer'), ('BABY', 'Baby menu'), ('REG', 'Regular'), ('HOT', 'Hot')], default='REG', max_length=4)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('weight', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
