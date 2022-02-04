from django.db import models


class CommonBaseModel(models.Model):
    title = models.CharField(max_length=256, unique=True, )
    is_active = models.BooleanField(default=True, )
    is_hidden = models.BooleanField(default=False, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}.{1}".format(self.id, self.title)

    class Meta:
        abstract = True

    @property
    def show_in_ui(self, ):
        return (not self.is_hidden) and self.is_active
