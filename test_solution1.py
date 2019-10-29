from solution import Room


def test_simple():
    my_office = Room('office', 10)
    assert my_office.name == 'office'
    assert my_office.size == 10


def test_str():
    my_office = Room('office', 10)
    assert str(my_office) == 'office, 10m'


def test_several_rooms():
    bedroom1 = Room('child bedroom', 10)
    bedroom2 = Room('master bedroom', 15)
    bedroom3 = Room('guest bedroom', 8)

    assert sum([one_room.size
                for one_room in [bedroom1, bedroom2, bedroom3]]) == 33
