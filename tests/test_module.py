from project.module import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
