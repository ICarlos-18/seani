# Generated by Django 5.0.2 on 2024-02-20 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_module_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text_image',
            new_name='question_image',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text_question',
            new_name='question_text',
        ),
    ]
