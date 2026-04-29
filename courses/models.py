from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # BURASI YENİ: CharField yerine ImageField kullanıyoruz
    image = models.ImageField(upload_to="courses", default="") 
    isActive = models.BooleanField(default=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"{self.title}"