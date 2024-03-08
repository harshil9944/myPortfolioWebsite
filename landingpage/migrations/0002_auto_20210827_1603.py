# Generated by Django 3.0.4 on 2021-08-27 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_link_name'),
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.AddField(
            model_name='project',
            name='details_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='details_link', to='timeline.Link'),
        ),
        migrations.AddField(
            model_name='project',
            name='image_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_link', to='timeline.Link'),
        ),
        migrations.AddField(
            model_name='project',
            name='live_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='live_link', to='timeline.Link'),
        ),
    ]