from django.db import models
import os


class Question(models.Model):
    CAT_MANGAS = 'Mangas'
    CAT_COMICS = 'Mangas'
    CAT_WEB = 'Web'
    CAT_MANAGEMENT = 'Management'
    CAT_ART = 'Art'
    CAT_CHOICES = (
        (CAT_MANGAS, 'Mangas'),
        (CAT_COMICS, 'Comics'),
        (CAT_WEB, 'Web'),
        (CAT_MANAGEMENT, 'Management'),
        (CAT_ART, 'Art'),
    )
    LEVEL_ONE = "1"
    LEVEL_TWO = "2"
    LEVEL_THREE = "3"
    LEVEL_CHOICES = (
        (LEVEL_ONE, 'Level 1'),
        (LEVEL_TWO, 'Level 2'),
        (LEVEL_THREE, 'Level 3'),
    )
    question = models.CharField(max_length=200)
    q_image = models.ImageField(upload_to='question', null=True, blank=True)
    q_level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default=LEVEL_ONE)
    q_category = models.CharField(max_length=15, choices=CAT_CHOICES, default=CAT_WEB)

    def delete(self, using=None):
        os.remove(self.q_images.path)

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=160)
    a_response = models.BooleanField()
    a_question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.answer
