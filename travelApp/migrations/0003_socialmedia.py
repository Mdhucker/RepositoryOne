# Generated by Django 4.2.11 on 2024-10-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0002_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('LinkedIn', 'LinkedIn'), ('YouTube', 'YouTube'), ('TikTok', 'TikTok'), ('Other', 'Other')], max_length=50)),
                ('link', models.URLField()),
            ],
        ),
    ]