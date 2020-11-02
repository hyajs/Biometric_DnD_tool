from django.contrib import admin


from .models import user_info

class user(admin.ModelAdmin):
    list_display = ('id','time','first_survey_question','second_survey_question','third_survey_question','fourth_survey_question','user_image','constitution','strength','dexterity','intelligence','charisma','wisdom','alignment','user_result')
    list_filter = ('time','first_survey_question','second_survey_question','third_survey_question','fourth_survey_question')



admin.site.register(user_info,user)


