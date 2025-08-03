from django.db import models

class Problem(models.Model):
    question = models.CharField(max_length=200)
    answer = models.IntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.question
    
    def problem_type(self):
        return self.type
    
    def check_answer(self, answer):
        return answer == self.answer
