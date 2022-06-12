def make_car(mark, model, **other):
    """Function accepts two postional and many Arbitrary arguments"""
    car={}
    car['mark'] = mark
    car['model'] = model
    for key, value in other.items():
        car[key] = value
    return car

car = make_car('bmw', '3', color = 'silver', year = '2017')
print(car)