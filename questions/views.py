#coding: utf-8
from django.shortcuts import redirect
from questions.models import QuestionForm, Question
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

class QuestionsListView(ListView): # представление в виде списка
    model = Question                   # модель для представления 
    paginate_by=3
    queryset=Question.objects.order_by("-datetime")

class QuestionDetailView(DetailView): # детализированное представление модели
    model = Question
    
class CreateQuestion(CreateView):
    form_class = QuestionForm
    template_name = 'create_question.html'
    succes_url = 'complete/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save() 
        return redirect(self.succes_url)

class CompleteCreateQuestion(TemplateView):
    template_name = "complete.html"

