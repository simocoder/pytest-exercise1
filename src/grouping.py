class TestClass:
    def test_one(self):
        x = 'blah'
        assert 'b' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x,"check")

# Note this this file has no import pytest in it, not sure why it doesn't seem to 
# need it, perhaps the class TestClass is inherited from it???

