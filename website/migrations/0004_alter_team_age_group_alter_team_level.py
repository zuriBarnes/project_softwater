# Generated by Django 4.1.7 on 2023-03-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_team_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='age_group',
            field=models.CharField(choices=[('U18', 'U18'), ('U17', 'U17'), ('U16', 'U16'), ('U15', 'U15'), ('U14', 'U14'), ('U14', 'U13'), ('U12', 'U12'), ('U11', 'U11'), ('U10', 'U10'), ('U9', 'U9'), ('U8', 'U8')], max_length=3),
        ),
        migrations.AlterField(
            model_name='team',
            name='level',
            field=models.CharField(choices=[('BLK', 'BLK'), ('YLW', 'YLW'), ('SLVR', 'SLVR'), ('REC', 'REC')], max_length=4),
        ),
    ]