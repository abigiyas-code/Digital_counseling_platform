from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_therapist = models.BooleanField(default=False)


class Question(models.Model):
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.question.question_text}-{self.answer_text}'


class UserAnswer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Answer)

    def __str__(self):
        return f'{self.user.username}'   


MARITAL_CHOICES = (
    (1, 'single'),
    (2, 'married'),
    (3, 'divorced')
)


EDUCATION_CHOICES = (
    (1, 'BSC'),
    (2, 'Masters'),
    (3, 'Phd')
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='user_images', blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200, blank=True)
    dob = models.DateField()
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    emergency_contact = models.CharField(max_length=15)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} profile'


class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='therapist_images')
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    education_level = models.CharField(max_length=10, choices=EDUCATION_CHOICES)
    dob = models.DateField()
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    emergency_contact = models.CharField(max_length=15)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} profile'  
