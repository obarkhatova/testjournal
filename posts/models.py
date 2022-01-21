from choicesenum import ChoicesEnum
from choicesenum.django.fields import EnumIntegerField
from django.db import models


class STATUS(ChoicesEnum):
    DRAFT = (0, 'draft')
    LOW = (1, 'published')


DEF_STATUS = STATUS.DRAFT


class Post(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    published = models.DateField(null=True)
    content = models.TextField()
    status = EnumIntegerField(enum=STATUS, default=DEF_STATUS)
    blog = models.ForeignKey('blogs.Blog', on_delete=models.CASCADE,
                             related_name='posts')
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class PostRead(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             related_name='posts_read')
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             related_name='users_read')

    class Meta:
        unique_together = (("post", "user"),)

