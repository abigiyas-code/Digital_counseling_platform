from django.db import models
from django.contrib.auth.models import AbstractUser

# Question about hobbie when user get started
class Hobbie_Question(AbstractUser):
    hquestion_text = models.TextField()

    def __str__(self):
        return self.hquestion_text

MARITAL_CHOICES = (
    (1, 'single'),
    (2, 'married'),
    (3, 'divorced')
)

class UserProfile(AbstractUser):
    user = models
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

# Question for an appointment
class Appoint_Question(models.Model):
    aquestion_text = models.TextField()

    def __str__(self):
        return self.aquestion_text

class Hobbie_Answer(models.Model):
    hquestion = models.ForeignKey(Hobbie_Question, related_name='hobbie', on_delete=models.CASCADE)
    hanswer_text = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.hquestion.hquestion_text}-{self.hanswer_text}'

class Appoint_Answer(models.Model):
    aquestion = models.ForeignKey(Appoint_Question, related_name='answer', on_delete=models.CASCADE)
    aanswer_text = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.aquestion.aquestion_text}-{self.aanswer_text}'


class UserAnswer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Appoint_Answer)

    def __str__(self):
        return f'{self.user.username}'   


# EDUCATION_CHOICES = (
#     (1, 'BSC'),
#     (2, 'Masters'),
#     (3, 'Phd')
# )

# class TherapistProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='therapist_images')
#     first_name = models.CharField(max_length=200)
#     middle_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     education_level = models.CharField(max_length=10, choices=EDUCATION_CHOICES)
#     dob = models.DateField()
#     marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
#     emergency_contact = models.CharField(max_length=15)
#     pub_date = models.DateTimeField()

#     def __str__(self):
#         return f'{self.user.username} profile'  
