const melonsToAdd = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas', 'Christmas', 'Christmas',
'Watermelon', 'Sharlyn', 'Xigua', 'Cantaloupe', 'Christmas', 'Watermelon',
'Christmas','Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen', 'Horned Melon',
'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn', 'Horned Melon', 'Sharlyn',
'Cantaloupe', 'Christmas', 'Horned Melon', 'Horned Melon', 'Horned Melon',
'Xigua', 'Xigua', 'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
'Watermelon', 'Santa Claus', 'Casaba'];

function countMelons(melonList = melonsToAdd){ //py: def countMelons(melonList)
    const melonCount = {}; //init empty Object

    for (const melon of melonList){ //py: for melon in melonList
        if (melonCount[melon]){
            melonCount[melon] += 1;
        }
        else{
            melonCount[melon] = 1;
        }
    }

    return melonCount;
}