from django.db import models


class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    interest = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.interest}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
