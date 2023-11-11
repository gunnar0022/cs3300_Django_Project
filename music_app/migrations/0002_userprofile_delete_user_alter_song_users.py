# Generated by Django 4.2.6 on 2023-11-10 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, verbose_name='Bio')),
                ('learned_songs', models.ManyToManyField(blank=True, related_name='learned_by', to='music_app.song')),
                ('liked_songs', models.ManyToManyField(blank=True, related_name='liked_by', to='music_app.song')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='song',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='songs', to='music_app.userprofile'),
        ),
    ]