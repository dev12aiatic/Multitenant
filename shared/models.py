from django.db import models
from tenant_schemas.models import TenantMixin
# Create your models here.
class Client(TenantMixin):
  name = models.CharField(max_length=100)
  on_trial=models.BooleanField(default=False)
  created_on= models.DateField(auto_now_add=True)
  auto_create_schema=True #cada vez que cree un cliente cree esquema en bd

class Language(models.Model):
  code= models.CharField(max_length=5)
  name= models.CharField(max_length=5)
