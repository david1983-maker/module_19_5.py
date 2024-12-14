from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost',)  # фильтрация по полям
    list_display = ('title', 'cost', 'size',)  # отображение полей списком
    search_fields = ('title',)  # поиск по полю
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)

admin.site.register(News)