from django import forms

# this is for the form in the page survey.html. It is set for questions and choices
class UserForm(forms.Form):

    YES_OR_NO_QUESTION = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    RACE_QUESTION = [
        ('Dwarf','Dwarf'),
        ('Elf','Elf'),
        ('Halfling', 'Halfing'),
        ('Human', 'Human'),
    ]
    CLASS_QUESTION = [
        ('Bard','Bard'),
        ('Cleric','Cleric'),
        ('Fighter', 'Fighter'),
        ('Rogue', 'Rogue'),
        ('Wizard', 'Wizard'),
    ]

    first_question = forms.ChoiceField(
        label='Have you played Dungeons and Dragons (D&D) before?',
        widget=forms.RadioSelect(attrs={'class': 'question'}),
        choices=YES_OR_NO_QUESTION,

    )
    second_question = forms.ChoiceField(
        label='What is your favourite Character Race?',
        widget=forms.RadioSelect(),
        choices=RACE_QUESTION,
        required=False,
    )
    third_question = forms.ChoiceField(
        label='What is your favourite Character Class?',
        widget=forms.RadioSelect(attrs={'class': 'special'}),
        choices=CLASS_QUESTION,
        required=False,
    )
    fourth_question = forms.ChoiceField(
        label='Would you like to have attributes similar to your favourite race and class?',
        widget=forms.RadioSelect(),
        choices=YES_OR_NO_QUESTION,
        required=False,
    )
    user_face = forms.ImageField(
        label='Please Upload a selfie or an image of your own!'
    )
