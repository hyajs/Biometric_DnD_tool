def attributes_change(race,profession,ans):

    if race == 'Dwarf':
        if ans['Constitution'] <= 16:
            ans['Constitution'] += 2
    elif race == 'Elf' or race == 'Halfling':
        if ans['Dexterity'] <= 16:
            ans['Dexterity'] += 2
    else:
        if ans['Constitution'] <= 17:
            ans['Constitution'] += 1
        if ans['Dexterity'] <= 17:
            ans['Dexterity'] += 1
        if ans['Strength'] <= 17:
            ans['Strength'] += 1
        if ans['Charisma'] <= 17:
            ans['Charisma'] += 1
        if ans['Wisdom'] <= 17:
            ans['Wisdom'] += 1

    if profession =='Bard':
        if ans['Charisma'] <= 16:
            ans['Charisma'] += 2
        if ans['Dexterity'] <= 17:
            ans['Dexterity'] += 1
    if profession =='Cleric':
        if ans['Wisdom'] <= 16:
            ans['Wisdom'] += 2
        if ans['Strength'] <= 17:
            ans['Strength'] += 1
        if ans['Constitution'] <= 17:
            ans['Constitution'] += 1

    if profession =='Fighter':
        if ans['Strength'] <= 16:
            ans['Strength'] += 2
        if ans['Constitution'] <= 17:
            ans['Constitution'] += 1

    if profession =='Rogue':
        if ans['Dexterity'] <= 16:
            ans['Dexterity'] += 2
        if ans['Intelligence'] <=17:
            ans['Intelligence'] +=1


    if profession =='Wizard':
        if ans['Intelligence'] <=16:
            ans['Intelligence'] +=2
        if ans['Dexterity'] <= 17:
            ans['Dexterity'] += 1
        if ans['Constitution'] <= 17:
            ans['Constitution'] += 1

    return ans

