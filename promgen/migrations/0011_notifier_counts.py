# Generated by Django 2.2.4 on 2019-11-28 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0010_app_label_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='error_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alert',
            name='sent_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='AlertError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promgen.Alert')),
            ],
        ),
    ]
