# Generated by Django 5.0.3 on 2024-03-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Раздел'),
        ),
    ]
