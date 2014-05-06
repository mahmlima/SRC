from django.db import models

class Artigo(models.Model):
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.titulo

class General(models.Model):
	bio = models.TextField()
	blog_title = models.CharField(max_length=20)
	updated_in = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.blog_title
