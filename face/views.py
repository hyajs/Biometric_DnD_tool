from django.shortcuts import render, redirect
import os
from unimelb.settings import BASE_DIR
from .forms import UserForm
from .models import user_info
from django.http import HttpResponse,Http404

import django.utils.timezone as timezone
from face.image_backend.Image_process import image_process, bio_metric
from face.image_backend.Generating_Result import attribute_generate
from face.image_backend.attributes_alter import attributes_change

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'face/index.html')


# If requesting method is post, user's results will be recorded to database, images will be sent to database for process
# results will be sent to results.html for displaying
def survey_view(request):
    if request.method == 'POST':
        userform = UserForm(request.POST, request.FILES)
        if userform.is_valid():
            first = userform.cleaned_data['first_question']
            second = userform.cleaned_data['second_question']
            third = userform.cleaned_data['third_question']
            fourth = userform.cleaned_data['fourth_question']
            photo = userform.cleaned_data['user_face']
        new_operator = user_info.objects.create(
            time=timezone.now(),
            first_survey_question=first,
            second_survey_question=second,
            third_survey_question=third,
            fourth_survey_question=fourth,
            user_image=photo,
        )
        new_operator.save()
        try:
            final_dir = os.path.join(BASE_DIR, 'media/images/', str(photo)).replace('\\', '/')
            saving_dir = os.path.join(BASE_DIR, 'media/cropped_image/').replace('\\', '/')

            age = image_process(final_dir, saving_dir, request.session.session_key)
            attribute_result = bio_metric(saving_dir, request.session.session_key)
            attribute_result['age'] = age
            ans = attribute_generate(attribute_result)

            if first == 'Yes' and fourth == 'Yes':
                ans = attributes_change(second,third, ans)


            new_operator.constitution=ans['Constitution']
            new_operator.strength=ans['Strength']
            new_operator.dexterity=ans['Dexterity']
            new_operator.intelligence=ans['Intelligence']
            new_operator.charisma=ans['Charisma']
            new_operator.wisdom=ans['Wisdom']
            new_operator.alignment=ans['Alignment']
            new_operator.user_result = attribute_result
            new_operator.save()

            result = {
                'dict': {'Constitution' : ans['Constitution'],
                'Strength' : ans['Strength'],
                'Dexterity': ans['Dexterity'],
                'Intelligence': ans['Intelligence'],
                'Charisma': ans['Charisma'],
                'Wisdom': ans['Wisdom'],
                'Alignment': ans['Alignment'],}

            }
            return render(request,'face/result.html',result)
        except IndexError:
            return HttpResponse("System can't detect your face, please refresh the page and upload again")
    else:
        form = UserForm(request.POST or None)
        context = {
            "form": form
        }
    return render(request, 'face/survey.html', context)



def page_not_found(request,exception):
    return render('face/404.html')