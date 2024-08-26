from django.contrib.admin import register , ModelAdmin
from teacher_app.models import Teacher

@register(Teacher)
class TeacherAdmin(ModelAdmin) :
    list_display = [
        'name', 
        'email',
        'phone_number',
        'rate',
        'category',
        'class1',
        'wallet',
    ]
    search_fields = [
        'name',
    ]
    
# Register your models here.
