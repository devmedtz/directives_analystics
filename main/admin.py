from django.contrib import admin
from .models import School, SubjectCombination, SchoolSubject, ExamResult, ExamRank,SearchResult,Subscribe

# Register your models here.
admin.site.register(School)
admin.site.register(SubjectCombination)
admin.site.register(SchoolSubject)
admin.site.register(ExamResult)
admin.site.register(ExamRank)
admin.site.register(SearchResult)
admin.site.register(Subscribe)
