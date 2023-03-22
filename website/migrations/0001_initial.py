# Generated by Django 3.2.18 on 2023-03-22 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=40)),
                ('bio', models.TextField(default='bio needed')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('team', models.CharField(choices=[('U18', 'U18'), ('U17', 'U17'), ('U16', 'U16'), ('U15', 'U15'), ('U14', 'U14'), ('U14', 'U13'), ('U12', 'U12'), ('U11', 'U11'), ('U10', 'U10'), ('U9', 'U9'), ('U8', 'U8')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(choices=[('U18', 'U18'), ('U17', 'U17'), ('U16', 'U16'), ('U15', 'U15'), ('U14', 'U14'), ('U14', 'U13'), ('U12', 'U12'), ('U11', 'U11'), ('U10', 'U10'), ('U9', 'U9'), ('U8', 'U8')], max_length=3)),
                ('side', models.CharField(choices=[('Boys', 'Boys'), ('Girls', 'Girls')], max_length=5)),
                ('level', models.CharField(choices=[('BLK', 'BLK'), ('YLW', 'YLW'), ('SLVR', 'SLVR')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=40)),
                ('bio', models.TextField(default='bio needed')),
                ('team', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.team')),
            ],
        ),
    ]
