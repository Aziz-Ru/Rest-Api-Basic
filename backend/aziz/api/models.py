from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=False)
    is_ok=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
