import uuid
from django.db import models


class pulpit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, verbose_name='Номер', primary_key=True)
    name = models.CharField('Название кафедры', max_length=50)
    phone = models.CharField('Телефон', max_length=13)
    fio = models.CharField('Глава кафедры', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class leaders(models.Model):
    id = models.UUIDField(default=uuid.uuid4, verbose_name='Номер', primary_key=True)
    fio = models.CharField('ФИО', max_length=50)
    pulpit_name = models.ForeignKey(
        pulpit,
        verbose_name='Название кафедры',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'


class Pulpit1(models.Model):
    pulid = models.CharField(default=uuid.uuid4, verbose_name='Номер кафедры', max_length=50, primary_key=True)
    pulname = models.CharField('Название каф.', max_length=50)
    pulphone = models.CharField('Телефон кафедры', max_length=13)
    pulfio = models.CharField('Глава', max_length=50)

    def __str__(self):
        return self.pulname

    class Meta:
        verbose_name = 'Кафедра предмета'
        verbose_name_plural = 'Кафедры предметов'


class Leaders1(models.Model):
    leadid = models.CharField(default=uuid.uuid4, verbose_name='Номер руководителя', max_length=50, primary_key=True)
    leadfio = models.CharField('ФИО Руководителя', max_length=50)
    pulpit1_pulname = models.ForeignKey(
        Pulpit1,
        verbose_name='Название каф.',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.leadfio

    class Meta:
        verbose_name = 'Руководитель проекта'
        verbose_name_plural = 'Руководители проектов'


class Reviewers(models.Model):
    revid = models.UUIDField(default=uuid.uuid4, verbose_name='Номер', max_length=50, primary_key=True)
    revfio = models.CharField('ФИО', max_length=50)
    pulpit_pulname = models.ForeignKey(
        Pulpit1,
        verbose_name='Название каф.',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.revfio

    class Meta:
        verbose_name = 'Рецензент'
        verbose_name_plural = 'Рецензенты'


class Project(models.Model):
    prid = models.UUIDField(default=uuid.uuid4, verbose_name='Номер проекта', primary_key=True)
    prname = models.CharField('Название дипломного проекта', max_length=50)

    def __str__(self):
        return self.prname

    class Meta:
        verbose_name = 'Дипломный проект'
        verbose_name_plural = 'Дипломные проекты'


class Student(models.Model):
    stid = models.UUIDField(default=uuid.uuid4, verbose_name='Номер', primary_key=True)
    stfio = models.CharField('ФИО Студентов', max_length=50)
    group = models.CharField('Группа', max_length=10)
    appraisal = models.CharField('Оценка', max_length=2)
    date = models.CharField('Срок сдачи', max_length=20)
    leaders_fio = models.ForeignKey(
        Leaders1,
        verbose_name='Руководитель',
        on_delete=models.CASCADE,
        null=True
    )
    reviewers_fio = models.ForeignKey(
        Reviewers,
        verbose_name='Рецензент',
        on_delete=models.CASCADE,
        null=True
    )
    project_name = models.ForeignKey(
        Project,
        verbose_name='Дипломный проект',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.stfio

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'




