from django.contrib.admin import register , ModelAdmin
from cupon_app.models import Cupon

@register(Cupon)
class CuponAdmin(ModelAdmin):
    list_display = [
        'name',
        'percent',
        'expire_date',
    ]
    search_fields = [
        'name',
    ]
# Register your models here.
