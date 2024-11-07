from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = dict(null=True, blank=True)


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35, verbose_name="Телефон", help_text="Укажите телефон", **NULLABLE
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("pk",)


class Payment(models.Model):
    class PaymentType(models.TextChoices):
        CASH = "cash", "Наличными"
        BANK = "bank", "Перевод на счёт"

    # класс Пользователя и его оплаты за курс/урок
    payer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="плательщик",
        related_name="payer",
    )
    payment_date = models.DateField(auto_now=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, verbose_name="Оплаченный курс", **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.SET_NULL, verbose_name="Оплаченный урок", **NULLABLE
    )
    amount = models.DecimalField(
        decimal_places=2, max_digits=20, verbose_name="Сумма оплаты"
    )
    type = models.CharField(max_length=255, verbose_name="Способ оплаты")

    def __str__(self):
        return f"{self.payer} - {self.paid_course if self.paid_course else self.paid_lesson} - {self.amount}"

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"
        ordering = ("payer", "payment_date")
