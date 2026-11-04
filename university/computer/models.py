from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    student_id = models.CharField(max_length=10, unique=True, verbose_name="شماره دانشجویی")
    email = models.EmailField(verbose_name="ایمیل")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "دانشجو"
        verbose_name_plural = "دانشجویان"


class Professor(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    national_code = models.CharField(max_length=10, unique=True, verbose_name="کد ملی")
    email = models.EmailField(verbose_name="ایمیل")
    department = models.CharField(max_length=100, verbose_name="دانشکده")

    def __str__(self):
        return f"دکتر {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "اساتید"


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان درس")
    code = models.CharField(max_length=10, unique=True, verbose_name="کد درس")
    units = models.PositiveIntegerField(default=3, verbose_name="تعداد واحد")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="استاد",
        null=True,
        blank=True
    )
    students = models.ManyToManyField(Student, related_name="courses", blank=True, verbose_name="دانشجویان")

    def __str__(self):
        return f"{self.title} ({self.code})"

    class Meta:
        verbose_name = "درس"
        verbose_name_plural = "دروس"
        