# Generated by Django 3.2.4 on 2021-09-04 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poller.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poller.question')),
            ],
        ),
    ]