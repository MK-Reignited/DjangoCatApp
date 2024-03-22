# Generated by Django 2.1.5 on 2024-03-22 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128, unique=True)),
                ('number_of_cats', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat_app.Student'),
        ),
    ]
