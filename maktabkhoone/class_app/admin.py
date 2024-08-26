from django.contrib.admin import register , ModelAdmin
from class_app.models import Class

@register(Class)
class ClassAdmin(ModelAdmin) :
    list_display = [
        'name',
        'time',
        'price',
        'teacher',
        'category',
        'student',
    ]
    search_fields = [
        'name',
    ]
# Register your models here.
