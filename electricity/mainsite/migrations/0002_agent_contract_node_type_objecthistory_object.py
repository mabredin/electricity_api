# Generated by Django 4.1 on 2023-10-06 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(help_text='Введите фамилию исполнителя', max_length=100, verbose_name='Фамилия исполнителя')),
                ('name', models.CharField(help_text='Введите имя исполнителя', max_length=100, verbose_name='Имя исполнителя')),
                ('patronymic', models.CharField(blank=True, help_text='Введите отчество исполнителя', max_length=100, null=True, verbose_name='Отчество исполнителя')),
                ('phone', models.CharField(help_text='Введите номер телефона исполнителя', max_length=20, unique=True, verbose_name='Номер телефона исполнителя')),
            ],
            options={
                'verbose_name': 'Исполнители',
                'verbose_name_plural': 'Исполнители',
                'db_table': 'agent',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Введите номер договора', max_length=100, unique=True, verbose_name='Номер договора')),
                ('date_of_issue', models.DateField(help_text='Введите дату оформления договора', verbose_name='Дата оформления договора')),
                ('status', models.BooleanField(default=True, help_text='Выберите статус договора', verbose_name='Статус договора')),
                ('slug', models.SlugField(default=None, max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Договоры',
                'verbose_name_plural': 'Договоры',
                'db_table': 'contract',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите имя объекта', max_length=100, unique=True, verbose_name='Имя объекта')),
                ('address', models.CharField(help_text='Введите адрес объекта', max_length=200, unique=True, verbose_name='Адрес объекта')),
                ('status', models.BooleanField(default=True, help_text='Выберите статус объекта', verbose_name='Статус объекта')),
                ('slug', models.SlugField(default=None, max_length=255, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Узлы',
                'verbose_name_plural': 'Узлы',
                'db_table': 'node',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите тип объекта', max_length=100, unique=True, verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'Типы объектов',
                'verbose_name_plural': 'Типы объектов',
                'db_table': 'type',
            },
        ),
        migrations.CreateModel(
            name='ObjectHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Введите код объекта', max_length=100, unique=True, verbose_name='Код объекта')),
                ('address', models.CharField(help_text='Введите адрес объекта', max_length=200, verbose_name='Адрес объекта')),
                ('start_value', models.IntegerField(help_text='Введите начальное показание счетчика', verbose_name='Начальное показание счетчика')),
                ('final_value', models.IntegerField(help_text='Введите конечное показание счетчика', verbose_name='Конечное показание счетчика')),
                ('info', models.TextField(blank=True, help_text='Введите дополнительную информацию', null=True, verbose_name='Дополнительная информация')),
                ('status', models.BooleanField(default=True, help_text='Выберите статус объекта', verbose_name='Статус объекта')),
                ('log', models.TextField(blank=True, help_text='Заполните журнал событий', null=True, verbose_name='Журнал событий')),
                ('month', models.IntegerField(help_text='Введите месяц показания', verbose_name='Месяц показания')),
                ('year', models.IntegerField(help_text='Введите год показания', verbose_name='Год показания')),
                ('agent', models.ForeignKey(blank=True, help_text='Выберите исполнителя', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='agent_objecthistory', to='mainsite.agent', verbose_name='Исполнитель')),
                ('contract', models.ForeignKey(help_text='Выберите договор объекта', on_delete=django.db.models.deletion.PROTECT, related_name='contract_objecthistory', to='mainsite.contract', verbose_name='Договор объекта')),
                ('node', models.ForeignKey(help_text='Выберите узел объекта', on_delete=django.db.models.deletion.PROTECT, related_name='node_objecthistory', to='mainsite.node', verbose_name='Узел объекта')),
                ('type', models.ForeignKey(help_text='Выберите тип объекта', on_delete=django.db.models.deletion.PROTECT, related_name='type_objecthistory', to='mainsite.type', verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'История объектов',
                'verbose_name_plural': 'История объектов',
                'db_table': 'objecthistory',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Введите код объекта', max_length=100, unique=True, verbose_name='Код объекта')),
                ('address', models.CharField(help_text='Введите адрес объекта', max_length=200, verbose_name='Адрес объекта')),
                ('start_value', models.IntegerField(default=0, help_text='Введите начальное показание счетчика', verbose_name='Начальное показание счетчика')),
                ('final_value', models.IntegerField(default=0, help_text='Введите конечное показание счетчика', verbose_name='Конечное показание счетчика')),
                ('info', models.TextField(blank=True, help_text='Введите дополнительную информацию', null=True, verbose_name='Дополнительная информация')),
                ('status', models.BooleanField(default=True, help_text='Выберите статус объекта', verbose_name='Статус объекта')),
                ('log', models.TextField(blank=True, help_text='Заполните журнал событий', null=True, verbose_name='Журнал событий')),
                ('agent', models.ForeignKey(blank=True, help_text='Выберите исполнителя', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='agent_object', to='mainsite.agent', verbose_name='Исполнитель')),
                ('contract', models.ForeignKey(help_text='Выберите договор объекта', on_delete=django.db.models.deletion.PROTECT, related_name='contract_object', to='mainsite.contract', verbose_name='Договор объекта')),
                ('node', models.ForeignKey(help_text='Выберите узел объекта', on_delete=django.db.models.deletion.PROTECT, related_name='node_object', to='mainsite.node', verbose_name='Узел объекта')),
                ('type', models.ForeignKey(help_text='Выберите тип объекта', on_delete=django.db.models.deletion.PROTECT, related_name='type_object', to='mainsite.type', verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'Объекты',
                'verbose_name_plural': 'Объекты',
                'db_table': 'object',
            },
        ),
    ]
