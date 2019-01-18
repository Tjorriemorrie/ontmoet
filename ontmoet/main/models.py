from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField('Created at', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Question(TimestampedModel):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Choice(TimestampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
