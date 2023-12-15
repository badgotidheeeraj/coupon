from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UserAccount
from datetime import datetime




class Post(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255, )
    category = models.CharField(max_length=255, )  
    File_name = models.ImageField(upload_to='media/')
    text = models.TextField(_("Description"), max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.brand



class masterdata(models.Model):
    brand = models.CharField(max_length=255, unique=True)  
    category = models.CharField(max_length=255 )  
    def __str__(self):
        return self.brand




# class RequestModule(models.Model):
#     username = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
#     ModuleName = models.ForeignKey(MasterModule, verbose_name=_("Module Name"), on_delete=models.CASCADE)
#     request_name = models.CharField(max_length=1000, blank=True, null=True)
#     json_field = models.JSONField(blank=True, null=True)
#     created_at = models.DateTimeField(default=datetime.now)
#     is_favorite = models.BooleanField(default=False)