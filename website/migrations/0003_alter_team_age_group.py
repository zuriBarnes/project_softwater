# Generated by Django 4.1.7 on 2023-03-24 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_manager_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='age_group',
            field=models.CharField(choices=[('REC', 'REC'), ('U18', 'U18'), ('U17', 'U17'), ('U16', 'U16'), ('U15', 'U15'), ('U14', 'U14'), ('U14', 'U13'), ('U12', 'U12'), ('U11', 'U11'), ('U10', 'U10'), ('U9', 'U9'), ('U8', 'U8')], max_length=3),
        ),
    ]
