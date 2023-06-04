import datetime

from .models import Question
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
# Create your tests here.

class QuestionModelTest(TestCase):
    
    def setUp(self):
        self.question = Question(question_text='Quien es el mejor developer?')
    
    def test_was_published_recently_with_future_question(self):
        """was published recently returns False for questions whose pub_date is in the future"""

        time = timezone.now() + datetime.timedelta(days=30)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(), False)
        
    def test_was_published_recently_with_present_question(self):
        """was published recently returns True for question whose pub_date is in the present"""
        
        time = timezone.now()
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(),True)
        
    def test_was_published_recently_with_past_question(self):
        """was published recently returns false for questions whose pub_date is en the past """
        
        time = timezone.now() - datetime.timedelta(days=1,minutes=1)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(),False)

def create_question(question_text, days):
    """Create a question with the given question text an the given 
    days in defference to now negative numbers for question published
    in te past positive numbers for question that are not yet published"""

    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date = time)

class QuestionIndexViewTest(TestCase):
    
    def test_no_question(self):
        """If no question exist retunrs ans appropiate messague"""
        
        response = self.client.get(reverse('polls:index'))
        
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'No Polls are available.')
        self.assertQuerysetEqual(response.context['lastest_question_list'], [])
        
    def test_no_future_question_are_displayed(self):
        """The questions whose pub_date is in the future will not be displayed"""
        future_question = create_question("Probando Probando 1. 2. 3. Probando",30)
        response = self.client.get(reverse('polls:index'))
        
        self.assertNotIn(future_question,response.context['lastest_question_list'])
        
    def test_past_questions_are_desplayed(self):
        """The questions whose pub_date is in the past will be displayed"""

        question = create_question("Probando Probando 1. 2. 3. Probando",-30)
        question_2 = create_question("Probando Probando 1. 2. 3. Probando",30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context["lastest_question_list"], [question])
        