from django.contrib import admin
from .models import User, Teacher, Course, Video, Review, Bank

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Review)
admin.site.register(Bank)