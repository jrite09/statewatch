from django.contrib import admin

# Register your models here.
from .models import State
from .models import Body
from .models import Legislature
from .models import Bills

admin.site.register(State)
admin.site.register(Body)
admin.site.register(Legislature)
admin.site.register(Bills)