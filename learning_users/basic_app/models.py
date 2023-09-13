from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # com isso, sabe-se que os bancos tem somente uma chave em comum (como se fossem espelhos um do outro)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # campos adicionais que não estão em User
    portfolio_site = models.URLField(blank=True)  # aceita nãda ser informado
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)  # upload é a pasta para onde a imagem será enviada


