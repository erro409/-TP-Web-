from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models import Sum

# Create your models here.
#change some textfields on charfields where needed

#ANSWERS
class AnswerManager(models.Manager):
    def get_by_id(self, questionId):
        question_answers = self.filter(question_id__exact=questionId)
        return question_answers

class Answer(models.Model):
    title = models.TextField(max_length=100)
    text = models.TextField()#should use min
    time = models.DateTimeField(auto_now = False, auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,)
    question = models.ForeignKey('Question', on_delete = models.CASCADE,)
    #should add something like rating = integerfield - the same idea as fr questions
    #service
    objects = AnswerManager()
    class Meta:
        ordering = ['-time']
    def __str__(self):
        return self.title

#QUESTIONS
class QuestionManager(models.Manager):
    def get_by_time(self):
        return self.all()
    def get_by_rating(self):
        return self.order_by('-rating')
    def get_by_tag(self, tag):
        question_by_tag = self.filter(tags__text__exact=str(tag))
        return question_by_tag
    def get_by_user(self, name):
        return self.filter(user__username = user_name)
    

class Question(models.Model):
    title=models.TextField(max_length=100)
    text = models.TextField()#should use min or max dont know yet
    time = models.DateTimeField(auto_now = False, auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,)
    answersAmount = models.IntegerField(default = 0)
    tags = models.ManyToManyField('Tag')
    rating = models.IntegerField(default = 0)
    #service
    objects = QuestionManager()
    class Meta:
        ordering = ['-time']
    def __str__(self):
        return self.title

class Like(models.Model):#set default values
    question = models.ForeignKey('Question', on_delete = models.CASCADE,)
    user = models.ForeignKey(User, on_delete = models.CASCADE,)
    like = models.IntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=10)
    #service 
    def __str__(self):
        return self.text
#PROFILES
class ProfileManager(models.Manager):
    def get_by_name(self, name):
        return self.filter(user__username = name)
    def get_by_id(self, id):
        return self.filter(user__id= id)

class Profile(models.Model):#user must inherit from django.user
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatars')
    #service
    objects = ProfileManager()
    def __str__(self):
        return self.user
