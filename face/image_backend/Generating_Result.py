from face.image_backend.trial import att_trial
# dict for sorting
corrosponding_attributes = {'Strength': 'aggressive', 'Dexterity': 'confident', 'Intelligence': 'intelligent',
                            'Charisma': ['attractive', 'sociable'], 'Wisdom': ['calm', 'humble'], }

# this function is used to generate corrosponding alignments [chaotic/lawful/neutral]
# or good/evil/neutral
def alignment_generate(dict):
    allignment_result = ['neutral', 'neutral']
    responsible = int(dict['responsible'][0])
    weird = int(dict['weird'][0])
    print(responsible)
    print(weird)
    chaotic_lawful = int(dict['caring'][0]) + int(dict['kind'][0])
    if responsible == 1 and weird == 3:
        allignment_result[0] = 'Chaotic'
    if responsible == 1 and weird == 2:
        allignment_result[0] = 'Chaotic'
    if responsible == 2 and weird == 3:
        allignment_result[0] = 'Chaotic'
    if responsible == 2 and weird == 1:
        allignment_result[0] = 'lawful'
    if responsible == 3 and weird == 2:
        allignment_result[0] = 'lawful'
    if responsible == 3 and weird == 1:
        allignment_result[0] = 'lawful'
    if chaotic_lawful <= 3:
        allignment_result[1] = 'Evil'
    if chaotic_lawful > 4:
        allignment_result[1] = 'good'
    return allignment_result[0] + ' ' + allignment_result[1]

def constitution_generate(dict):
    age = dict['age']
    if age >= 60 or age <=14:
        constitution = 3
    elif age>30:
        difference = int((age - 30) / 2)
        constitution = 18 - difference
    else:
        difference = abs(age-29)
        constitution = 18-difference
    return constitution

def attribute_generate(dict):
    attribute_solution = {}
    constitution = constitution_generate(dict)
    attribute_solution['Constitution'] = constitution
    for key in corrosponding_attributes:
        try:

            attributes = att_trial(key, level=[int(dict[corrosponding_attributes[key]][0])],
                                   percentage=[float(dict[corrosponding_attributes[key]][1])])
            attribute_solution[attributes.name] = attributes.decide()
        except TypeError:
            attributes = att_trial(key, level=[int(dict[corrosponding_attributes[key][0]][0]),
                                               int(dict[corrosponding_attributes[key][1]][0])],
                                   percentage=[(float(dict[corrosponding_attributes[key][0]][1])),
                                               float(dict[corrosponding_attributes[key][1]][1])],
                                   )
            attribute_solution[attributes.name] = attributes.decide()

    alignment = alignment_generate(dict)
    attribute_solution['Alignment'] = alignment

    return attribute_solution
