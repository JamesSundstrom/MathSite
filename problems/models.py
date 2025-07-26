from django.db import models

class Problem(models.Model):
    question = models.CharField(max_length=200)
    answer = models.IntegerField()

    def __str__(self):
        return self.question
    
    def check_answer(self, answer):
        return answer == self.answer
