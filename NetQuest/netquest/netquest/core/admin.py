from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

	list_display = ['matricula', 'email', 'created_at']
	search_field = ['matricula', 'email']


admin.site.register(User, UserAdmin)


