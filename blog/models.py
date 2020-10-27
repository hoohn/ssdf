from django.db import models


class Article(models.Model):

    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    brief_content = models.TextField()
    conTent = models.TextField()
    public_Date = models.DateTimeField(auto_now= True)

    def _str_(self):
         return self.Title


