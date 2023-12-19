from django.db import models

class Answer(models.Model):
    answer = models.TextField()

    def __str__(self):
        return self.answer

class RateLimit(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    connection_number = models.PositiveIntegerField(default=0)

class RateLimit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    question = models.TextField()
    answers = models.ManyToManyField(Answer)
    correct = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="correct")

    def __str__(self):
        return self.question

class Test(models.Model):
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return str(self.id)

class Theme(models.Model):
    name = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    presentation_url = models.CharField(max_length=255)
    position_in_themes_list = models.IntegerField()

    class Meta:
        ordering = ['position_in_themes_list']

    def __str__(self):
        return self.name

class Course(models.Model):
    themes = models.ManyToManyField(Theme)
    name = models.CharField(max_length=255)
    control_test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
