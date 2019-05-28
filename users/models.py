from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


# Create your models here.
class UserProfile(AbstractUser):
	id = models.AutoField(primary_key=True)
	phone = models.CharField(max_length=30, verbose_name='手机', default='')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

	USERNAME_FIELD = 'username'

	class Meta:
		verbose_name = '用户信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.username


class ResumeData(models.Model):
	'''简历信息表'''

	name = models.CharField(max_length=40, verbose_name='姓名')
	gender = models.CharField(max_length=6, verbose_name='性别', choices=(('male', '男'), ('female', '女')))
	email = models.EmailField(max_length=50, verbose_name='邮箱')
	phone = models.CharField(max_length=30, verbose_name='手机')
	birthday = models.CharField(max_length=30, verbose_name='生日')
	city = models.CharField(max_length=40, verbose_name='城市')
	website = models.URLField(max_length=40, verbose_name='个人主页')
	school = models.CharField(max_length=40, verbose_name='学校')
	major = models.CharField(max_length=40, verbose_name='专业')
	skill = models.TextField(verbose_name='技能信息')
	user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)

	class Meta:
		verbose_name = '简历信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class EduInfo(models.Model):
	'''教育经历'''

	school_1 = models.CharField(max_length=40, verbose_name='学校')
	start_time_1 = models.DateField(verbose_name='入学时间')
	end_time_1 = models.DateField(verbose_name='毕业时间')

	school_2 = models.CharField(max_length=40, verbose_name='学校', null=True)
	start_time_2 = models.DateField(verbose_name='入学时间', null=True)
	end_time_2 = models.DateField(verbose_name='毕业时间', null=True)

	school_3 = models.CharField(max_length=40, verbose_name='学校', null=True)
	start_time_3 = models.DateField(verbose_name='入学时间', null=True)
	end_time_3 = models.DateField(verbose_name='毕业时间', null=True)

	resume = models.ForeignKey(ResumeData, verbose_name='简历', on_delete=models.CASCADE)

	class Meta:
		verbose_name = '教育经历'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.resume.name