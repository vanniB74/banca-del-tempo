"""Basic tests for gen.py"""


def test_import_gen():
    """Test that gen.py can be imported without errors"""
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import gen
    assert gen.W is not None
    assert isinstance(gen.W, list)


def test_append_function():
    """Test that A() function works correctly"""
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import gen
    initial_len = len(gen.W)
    gen.A('<test>')
    assert len(gen.W) == initial_len + 1
    assert gen.W[-1] == '<test>'
