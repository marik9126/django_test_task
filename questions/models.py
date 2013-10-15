#coding: utf-8
from django.db import models
from django import forms

from django.db.models import signals
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Question(models.Model):
    title = models.CharField(max_length=255) 
    content = models.TextField(max_length=10000) 
    datetime = models.DateTimeField(auto_now_add=True,  verbose_name = u'Дата публикации') 
    author = models.ForeignKey(User) 

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/questions/%i/" % self.id

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('author',)

def notify_author(sender, instance, created, **kwargs):
    if created:
       subject = 'New comment created'
       message = 'Comment " %s " was added' % instance.comment
       from_addr = 'a@example.com'
       question = Question.objects.get(id=instance.object_pk)
       author_email =  question.author.email
       recipient_list = (str(author_email),)
       send_mail(subject, message, from_addr, recipient_list)       
       

signals.post_save.connect(notify_author, sender=Comment)