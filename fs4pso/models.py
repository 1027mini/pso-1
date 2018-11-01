# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Subject(models.Model):
	subject = models.CharField(max_length=20, verbose_name='과목')
	created_date = models.DateTimeField(auto_now=True)

	def publish(self):
		self.save()

	def __str__(self):
		return str(self.subject)

class Post(models.Model):
	subject = models.ForeignKey('fs4pso.Subject', default=1, on_delete=models.CASCADE )
	name = models.CharField(max_length=10, verbose_name='작성자', default=' ')
	good_points = models.TextField(verbose_name='좋았던 점', default=' ')
	improving_points = models.TextField(verbose_name='개선되었으면 하는 점', default=' ')
	another_points = models.TextField(verbose_name='하고싶은 말', default=' ')
	created_date = models.DateTimeField(auto_now=True)
	num_of_likes = models.IntegerField(default=0)

	def publish(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.name)

class Comment(models.Model):
	post = models.ForeignKey('fs4pso.Post', related_name='comments', default=1, on_delete=models.CASCADE)
	name = models.CharField(verbose_name='댓글 작성자', max_length=10, default=' ')
	text = models.TextField(verbose_name='댓글', default=' ')
	created_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.text)

class User(models.Model):
	user_id = models.CharField(verbose_name = '아이디', max_length = 20)
	user_pw = models.CharField(verbose_name = '비밀번호', max_length = 20)
	user_name = models.CharField(verbose_name = '이름', max_length = 20)
	user_nickname = models.CharField(verbose_name = '닉네임', max_length = 20)
	user_email = models.CharField(verbose_name = '이메일', max_length = 40)

	def __str__(self):
		return str(self.user_nickname)