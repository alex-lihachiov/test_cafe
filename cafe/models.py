from datetime import date

from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Cafe(models.Model):
    """Кафешки"""
    name = models.CharField("Название", max_length=150)
    image = models.ImageField("Изображение", upload_to="cafe/")
    address = models.CharField("Адрес", max_length=150)
    description = models.TextField("Описание")
    year = models.DateField("Дата регистрации", default=date.today)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default="False")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафе"
        verbose_name_plural = "Кафе"


class Photos(models.Model):
    """Фото кафе"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото интерьера", "cafe_shots/")
    cafe = models.ForeignKey(Cafe, verbose_name="Кафе", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография интерьера"
        verbose_name_plural = "Фотографии интерьера"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    cafe = models.ForeignKey(Cafe, on_delete=models.CharField, verbose_name="Кафе")

    def __str__(self):
        return f"{self.star} - {self.cafe}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Текст отзыва", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    cafe = models.ForeignKey(Cafe, verbose_name="Кафе", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
