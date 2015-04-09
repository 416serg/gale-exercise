from django.db import models

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    article_category = models.CharField(max_length=200)
    article_hero = models.ImageField()
    article_img = models.ImageField()
    article_body = models.TextField()

    def __unicode__(self):
        return self.article_title
