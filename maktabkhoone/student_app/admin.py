from django.contrib.admin import register , ModelAdmin
from student_app.models import Student

@register(Student)
class StudentAdmin(ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone_number',
        'class1',
        'cupon',
        'wallet',
    ]
    search_fields = [
        'name',
    ]
# Register your models here.
