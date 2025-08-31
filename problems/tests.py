from django.test import TestCase
from .models import Problem

class EvaluationProblemTests(TestCase):
    def test_evaluation_problems(self):
        """
        Check that every question in the database that asks the user to
        evaluate a given expression has the correct answer.
        """
        for problem in Problem.objects.all():
            try:
                correct_answer = eval(problem.question)
                self.assertEqual(correct_answer, problem.answer)
            except SyntaxError:
                continue # Problem is not an "evaluate the expression" problem
            