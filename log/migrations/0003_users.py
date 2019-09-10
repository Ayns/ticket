# Generated by Django 2.2.4 on 2019-09-10 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0002_department_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=20, unique=True)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(blank=True, max_length=70)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]