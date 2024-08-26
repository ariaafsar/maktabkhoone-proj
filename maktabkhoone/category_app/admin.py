from django.contrib.admin import register , ModelAdmin 
from category_app.models import Category

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = [
        'name',
        'class1'
    ]
    search_fields = [
        'name',
    ]
# Register your models here.
