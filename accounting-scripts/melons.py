melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

flesh_color = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
}

rind_color ={
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
}

average_weight = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
}

melon_data = {}
for idx in melon_names:
    melon_data[melon_names[idx]] = {
        'price': melon_prices[idx],
        'seedlessness': melon_seedlessness[idx],
        'flesh color': flesh_color[idx],
        'rind color': rind_color[idx],
        'average weight': average_weight[idx],
    }