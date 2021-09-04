from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    poll = models.ForeignKey('poller.Poll', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.TextField()
    question = models.ForeignKey('poller.Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey('poller.Question', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    choice = models.ForeignKey('poller.Choice', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question} - {self.choice}'
