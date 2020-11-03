from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  get_object_or_404, render
from django.template import loader
from .models import Question, Choice
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    #output = ' , '.join([q.question_test for q in latest_question_list])
    #return HttpResponse(output)
    #用loader函数，讲html文件提取作为模板
    template = loader.get_template('polls/index.html')
    #构建字典
    context = {'latest_question_list': latest_question_list}
    #将上面创建的字典context，前端的请求request，作为模板template的参数，来渲染模板
    return HttpResponse(template.render(context, request))

# %s表示输入一个数字参数（类似C语言的%d），外面填参数时也要加一个%，例如 HttpResponse('%s' % example)
# 留意参数中的question_id，这个要作为urls中的一个参数，类型可自定义，urls中具体介绍规则<>
# ********将选项的上下文传到模板，由question_id得到question，通过函数choice_set.all()获取到Choice对象的集合choice，将choice放入上下文传递
# ********模板处只要将choice集合里的变量取出，通过{% for %} <ul></ul> （for循环，无序列表）将choice排列即可
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("question does not Exit")
    template = loader.get_template('polls/detail.html')
    choice = question.choice_set.all()
    context = {'question': question}
    #context[question] = question
    return HttpResponse(template.render(context, request))
    #return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #choice = question.choice_set.all()
    try:
        #测试有没有默认选项,request.POST['choice'],意思是获取提交的字符串数据，这里指明了是choice类型
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    #return HttpResponse("You're voting on question %s." % question_id)
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
    #重定向页面到results页面，并且要给出重定向参数
