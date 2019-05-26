from django.contrib import admin

from .models import UserProfile

# Register your models here.
class UserProfileManager(admin.ModelAdmin):
	list_display = ['username']
	search_fields = ['username']
	list_filter = ['username']


admin.site.register(UserProfile, UserProfileManager)