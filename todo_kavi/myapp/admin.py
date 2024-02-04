from django.contrib import admin
from .models import TeamMember,Task,ChatMessage
# Register your models here.

admin.site.register(TeamMember)
admin.site.register(Task)
admin.site.register(ChatMessage)