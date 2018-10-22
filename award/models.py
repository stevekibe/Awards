from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.dispatch import receiver

class Detail(models.Model):
    bio = HTMLField()
    user_image = models.ImageField(upload_to ='images/')
    user = models.OneToOneField(User, on_delete=models.CASCADE,null="True")

    @receiver(post_save, sender=User)
    def create_user_detail(sender,instance,created, **kwrgs):
        if created:
            Detail.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_detail(sender, instance, **kwargs):
        instance.detail.save()

    post_save.connect(save_user_detail,sender=User)

    def save_detail(self):
        self.save()

    @classmethod
    def get_by_id(cls,user_id):
        detail = Detail.objects.get(user_id=user_id)
        return detail

    def __str__(self):
        return self.bio

class Project(models.Model):
    title = models.CharField(max_length = 100)
    project_img = models.ImageField(upload_to = 'images/', blank=True)
    project_detail = HTMLField()
    link = models.URLField(max_length = 100)
    pub_date = models.DateTimeField(auto_now_add=True)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pub_date']

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        return projects

    @property
    def count_votes(self):
        votes = self.votes.count()
        return votes

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


    @classmethod
    def get_project_by_id(cls,id):
        project = Project.objects.get(pk=id)
        return project

    @classmethod
    def get_project_by_user(cls, id):
        project = Project.objects.filter(user_id=id).all()
        return project

    
    def __str__(self):
        return self.project_detail

class Comment(models.Model):
    comment = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='comments',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null="True")
    class Meta:
        ordering = ['pub_date']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment_by_project_id(cls,projet):
        comments = Comments.objects.get(image_id=image)
        return comments

    def __str__(self):
        return self.comment 

class Votes(models.Model):
    user_vote = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    voted_project =models.ForeignKey(Project, on_delete=models.CASCADE, related_name='votes',null=True)

    def save_like(self):
        self.save()

    def __str__(self):
        return self.user_vote




 

