# Generated by Django 3.0.3 on 2022-02-20 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220220_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.Ticket'),
        ),
    ]