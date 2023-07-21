from django.contrib import admin
from product_catalogue.models import *

from django.contrib.auth import get_user_model

User = get_user_model()


admin.site.register(User)
admin.site.register(Product)
