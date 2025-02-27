from django.db import models


class Course(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Картинка",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Внешка",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Картинка",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="lessons",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]
        permissions = []

    def __str__(self):
        return self.name
