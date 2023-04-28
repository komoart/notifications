# Generated by Django 3.2.12 on 2023-04-28 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('code', models.CharField(choices=[('common', 'Обычное письмо'), ('monthly_personal_statistic', 'Ежемесячная персональная статистика')], max_length=50)),
                ('template', models.TextField()),
                ('subject', models.TextField(blank=True, null=True)),
                ('transport', models.CharField(choices=[('sms', 'Sms'), ('email', 'Email')], default='email', max_length=50)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'notification_templates',
            },
        ),
        migrations.CreateModel(
            name='MailingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'В очередь на отправку'), ('done', 'Отправлено'), ('cancelled', 'Отменено')], default='pending', max_length=250)),
                ('is_promo', models.BooleanField(default=True)),
                ('priority', models.CharField(choices=[('high', 'Высокий приоритет'), ('medium', 'Средний приоритет'), ('low', 'Низкий приоритет')], default='low', max_length=250)),
                ('context', models.JSONField(default={})),
                ('scheduled_datetime', models.DateTimeField(blank=True, null=True)),
                ('execution_datetime', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.template')),
            ],
            options={
                'db_table': 'mailing_tasks',
            },
        ),
    ]
