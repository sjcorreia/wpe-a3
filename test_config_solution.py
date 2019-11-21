from config_solution import ConfigFile


def test_set_get():
    cf = ConfigFile('myconfig.txt')
    cf.set('a', '1')
    cf.set('b', '2')
    cf.set('c', 3)

    assert cf.config == {'a': '1', 'b': '2', 'c': '3'}

    assert cf.get('a') == '1'
    assert cf.get('b') == '2'
    assert cf.get('c') == '3'


def test_store_retrieve(tmp_path):
    filename = tmp_path / 'myconfig.txt'

    cf = ConfigFile(filename)

    cf.set('a', '1')
    cf.set('b', '2')
    cf.set('c', '3')

    cf.dump()

    config_lines = open(filename).readlines()
    assert config_lines[0] == 'a=1\n'
    assert config_lines[1] == 'b=2\n'
    assert config_lines[2] == 'c=3\n'

    new_cf = ConfigFile(filename)
    new_cf.load()
    assert cf.config == new_cf.config

def test_store_retrieve2(tmp_path):
    filename = tmp_path / 'myconfig2.txt'

    cf = ConfigFile(filename, sep='::')
    assert cf.sep == '::'

    cf.set('a', '1')
    cf.set('b', '2')
    cf.set('c', '3')

    cf.dump()

    config_lines = open(filename).readlines()
    assert config_lines[0] == 'a::1\n'
    assert config_lines[1] == 'b::2\n'
    assert config_lines[2] == 'c::3\n'

    new_cf = ConfigFile(filename, sep='::')
    new_cf.load()
    assert cf.config == new_cf.config
