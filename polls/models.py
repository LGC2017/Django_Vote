from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_test = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_test

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text


#测试一下API得依赖关系，
#可以通过外键对象来关联创建对象，外键
#question作为外键，Question对象会有一个属性，小写函数名_set这样一个创建函数（psmessage_set）
#通过dir(对象)可以看到

#另外question.choice_set 指向一个地址，地址里包含了choice对象的QuerySet（类似集合set），从QuerySet中能取出对应序列号的choice对象，从choice对象中能提取choice的text

class PSmessage(models.Model): #附加信息，PS信息

    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    ps_text = models.CharField(max_length=200)

    def __str__(self):
        return self.ps_text