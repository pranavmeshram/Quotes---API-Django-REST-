from django.contrib import admin
from quotes_app.models import *
# Register your models here.


class QuotesAdmin(admin.ModelAdmin):
    list_display = ("sr_lang", "en_lang", "author", "source", "rating")


admin.site.register(Quotes, QuotesAdmin)



