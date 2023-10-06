from django.contrib.auth.models import AbstractUser
from django.db import models


class Agent(models.Model):
    surname = models.CharField(
        max_length=100,
        help_text="Введите фамилию исполнителя",
        null=False,
        verbose_name="Фамилия исполнителя"
    )
    name = models.CharField(
        max_length=100,
        help_text="Введите имя исполнителя",
        null=False,
        verbose_name="Имя исполнителя"
    )
    patronymic = models.CharField(
        max_length=100,
        help_text="Введите отчество исполнителя",
        null=True,
        blank=True,
        verbose_name="Отчество исполнителя"
    )
    phone = models.CharField(
        max_length=20,
        help_text="Введите номер телефона исполнителя",
        null=False,
        verbose_name="Номер телефона исполнителя",
        unique=True
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Исполнители'
        verbose_name_plural = 'Исполнители'
        db_table = 'agent'


class Contract(models.Model):
    number = models.CharField(
        max_length=100,
        help_text="Введите номер договора",
        verbose_name="Номер договора",
        null=False,
        unique=True
    )
    date_of_issue = models.DateField(
        help_text="Введите дату оформления договора",
        null=False,
        verbose_name="Дата оформления договора"
    )
    status = models.BooleanField(
        help_text="Выберите статус договора",
        verbose_name="Статус договора",
        default=True
    )
    slug = models.SlugField(
        max_length=255,
        default=None,
        verbose_name="URL",
        unique=True,
        null=False
    )

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Договоры'
        verbose_name_plural = 'Договоры'
        db_table = 'contract'


class Node(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Введите имя объекта",
        verbose_name="Имя объекта",
        null=False,
        unique=True
    )
    address = models.CharField(
        max_length=200,
        help_text="Введите адрес объекта",
        verbose_name="Адрес объекта",
        null=False,
        unique=True
    )
    status = models.BooleanField(
        help_text="Выберите статус объекта",
        verbose_name="Статус объекта",
        default=True
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name="URL",
        default=None,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Узлы'
        verbose_name_plural = 'Узлы'
        db_table = 'node'


class Type(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Введите тип объекта",
        verbose_name="Тип объекта",
        null=False,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Типы объектов'
        verbose_name_plural = 'Типы объектов'
        db_table = 'type'


class Object(models.Model):
    code = models.CharField(
        max_length=100,
        help_text="Введите код объекта",
        verbose_name="Код объекта",
        null=False,
        unique=True
    )
    address = models.CharField(
        max_length=200,
        help_text="Введите адрес объекта",
        verbose_name="Адрес объекта",
        null=False
    )
    type = models.ForeignKey(
        'Type',
        on_delete=models.PROTECT,
        help_text="Выберите тип объекта",
        verbose_name="Тип объекта",
        null=False,
        related_name='type_object'
    )
    node = models.ForeignKey(
        'Node',
        on_delete=models.PROTECT,
        help_text="Выберите узел объекта",
        verbose_name="Узел объекта",
        null=False,
        related_name='node_object'
    )
    contract = models.ForeignKey(
        'Contract',
        on_delete=models.PROTECT,
        help_text="Выберите договор объекта",
        verbose_name="Договор объекта",
        null=False,
        related_name='contract_object'
    )
    agent = models.ForeignKey(
        'Agent',
        on_delete=models.PROTECT,
        help_text="Выберите исполнителя",
        null=True,
        blank=True,
        verbose_name="Исполнитель",
        related_name='agent_object'
    )
    start_value = models.IntegerField(
        help_text="Введите начальное показание счетчика",
        verbose_name="Начальное показание счетчика",
        null=False,
        default=0,
    )
    final_value = models.IntegerField(
        help_text="Введите конечное показание счетчика",
        null=False,
        default=0,
        verbose_name="Конечное показание счетчика"
    )
    info = models.TextField(
        help_text="Введите дополнительную информацию",
        verbose_name="Дополнительная информация",
        null=True,
        blank=True
    )
    status = models.BooleanField(
        help_text="Выберите статус объекта",
        verbose_name="Статус объекта",
        default=True
    )
    log = models.TextField(
        help_text="Заполните журнал событий",
        verbose_name="Журнал событий",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Объекты'
        verbose_name_plural = 'Объекты'
        db_table = 'object'


class ObjectHistory(models.Model):
    code = models.CharField(
        max_length=100,
        help_text="Введите код объекта",
        verbose_name="Код объекта",
        null=False,
        unique=True
    )
    address = models.CharField(
        max_length=200,
        help_text="Введите адрес объекта",
        verbose_name="Адрес объекта",
        null=False
    )
    type = models.ForeignKey(
        'Type',
        on_delete=models.PROTECT,
        help_text="Выберите тип объекта",
        verbose_name="Тип объекта",
        null=False,
        related_name='type_objecthistory'
    )
    node = models.ForeignKey(
        'Node',
        on_delete=models.PROTECT,
        help_text="Выберите узел объекта",
        verbose_name="Узел объекта",
        null=False,
        related_name='node_objecthistory'
    )
    contract = models.ForeignKey(
        'Contract',
        on_delete=models.PROTECT,
        help_text="Выберите договор объекта",
        verbose_name="Договор объекта",
        null=False,
        related_name='contract_objecthistory'
    )
    agent = models.ForeignKey(
        'Agent',
        on_delete=models.PROTECT,
        help_text="Выберите исполнителя",
        null=True,
        blank=True,
        verbose_name="Исполнитель",
        related_name='agent_objecthistory'
    )
    start_value = models.IntegerField(
        help_text="Введите начальное показание счетчика",
        verbose_name="Начальное показание счетчика",
        null=False
    )
    final_value = models.IntegerField(
        help_text="Введите конечное показание счетчика",
        null=False,
        verbose_name="Конечное показание счетчика"
    )
    info = models.TextField(
        help_text="Введите дополнительную информацию",
        verbose_name="Дополнительная информация",
        null=True,
        blank=True
    )
    status = models.BooleanField(
        help_text="Выберите статус объекта",
        verbose_name="Статус объекта",
        default=True
    )
    log = models.TextField(
        help_text="Заполните журнал событий",
        verbose_name="Журнал событий",
        null=True,
        blank=True
    )
    month = models.IntegerField(
        help_text="Введите месяц показания",
        verbose_name="Месяц показания",
        null=False
    )
    year = models.IntegerField(
        help_text="Введите год показания",
        verbose_name="Год показания",
        null=False
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'История объектов'
        verbose_name_plural = 'История объектов'
        db_table = 'objecthistory'


class User(AbstractUser):
    """Переопределенная модель пользователя"""
    patronymic = models.CharField(
        max_length=100,
        verbose_name="Отчество",
        null=True,
        blank=True
    )

    job_title = models.CharField(
        max_length=100,
        verbose_name="Должность",
        null=True,
        blank=True
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'user'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def get_short_name(self):
        if self.last_name and self.first_name and self.patronymic:
            return f'{self.last_name} {self.first_name[0]}. {self.patronymic[0]}.'
        return None
