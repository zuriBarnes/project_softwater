# Generated by Django 4.1.4 on 2023-03-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='side',
            field=models.CharField(choices=[('Boys', 'Boys'), ('Girls', 'Girls')], max_length=5),
        ),
    ]