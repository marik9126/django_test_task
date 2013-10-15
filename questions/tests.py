from django.contrib.auth.models import User
from django.test import TestCase, Client
from questions.models import Question, QuestionForm
from django.utils import timezone
from django.contrib.comments.models import Comment

class FormCreateQuestionTests(TestCase):
    def test_create_question(self):
        c = Client()
        response = c.get('/questions/create/')
        self.assertEquals(response.status_code, 200)    

    def test_forms(self):
        form_data = {'title':'test?', 'content': 'something'}
        form = QuestionForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

class QuestionTest(TestCase):
    def create_user(name='test_user6', email='a@example.com', password='12'):
        return User.objects.create(username=name,
                                                    email=email,
                                                    password=password)

    def create_question(self, user, title='test_title', content='why?'):
        return Question.objects.create(title=title,
                                                        content=content,
                                                        datetime=timezone.now(),
                                                        author=user)

    def test_qustion_creation(self):
        user = self.create_user()
        question = self.create_question(user)
        self.assertTrue(isinstance(question, Question))
        self.assertTrue(isinstance(user, User))
        self.assertEqual(question.__unicode__(), question.title)
        question_url = "/questions/%i/" % question.id
        question_url_method = question.get_absolute_url()
        self.assertEqual(question_url_method, question_url)

    def test_questions_list_page_avaliable(self):
        c = Client()
        response = c.get('/questions/')
        self.assertEquals(response.status_code, 200)

    def test_question_detail_page_avaliable(self):
        c = Client()
        user = self.create_user()
        question = self.create_question(user)
        question_url = "/questions/%i/" % question.id
        response = c.get(question_url)
        self.assertEquals(response.status_code, 200)

class AccountPagesAvaliableTest(TestCase):
    def test_accounts_pages_avaliable(self):
        c = Client()
        response = c.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)
        response = c.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)
        response = c.get('/password/reset/')
        self.assertEquals(response.status_code, 200)
        response = c.get('/password/reset/done/')
        self.assertEquals(response.status_code, 200)
        response = c.get('/accounts/register/complete/')
        self.assertEquals(response.status_code, 200)
        response = c.post('/accounts/login/', {'username': 'ma', 'password': '12'})
        self.assertEquals(response.status_code, 200)