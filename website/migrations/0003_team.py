# Generated by Django 4.1.4 on 2023-03-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_coach_bio_alter_leader_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(choices=[('U18', 'U18'), ('U17', 'U17'), ('U16', 'U16'), ('U15', 'U15'), ('U14', 'U14'), ('U14', 'U13'), ('U12', 'U12'), ('U11', 'U11'), ('U10', 'U10'), ('U9', 'U9'), ('U8', 'U8')], max_length=3)),
                ('side', models.CharField(choices=[('B', 'Boys'), ('G', 'Girls')], max_length=2)),
                ('level', models.CharField(choices=[('BLK', 'BLK'), ('YLW', 'YLW'), ('SLVR', 'SLVR')], max_length=4)),
            ],
        ),
    ]
