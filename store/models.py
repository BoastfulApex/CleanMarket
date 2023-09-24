from django.db import models


class Category(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz


class SubCategory(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_uz


class Product(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)
    top = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name_uz


class About(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)


class News(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=20000, null=True, blank=True)
    description_ru = models.TextField(max_length=20000, null=True, blank=True)
    description_en = models.TextField(max_length=20000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    actual = models.BooleanField(default=False)
    views = models.IntegerField(default=0)


class FAQ(models.Model):
    question_uz = models.CharField(max_length=200, null=True, blank=True)
    question_ru = models.CharField(max_length=200, null=True, blank=True)
    question_en = models.CharField(max_length=200, null=True, blank=True)
    answer_uz = models.TextField(max_length=20000, null=True, blank=True)
    answer_ru = models.TextField(max_length=20000, null=True, blank=True)
    answer_en = models.TextField(max_length=20000, null=True, blank=True)


