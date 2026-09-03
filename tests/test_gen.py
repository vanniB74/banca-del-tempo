"""Tests for gen.py module"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_gen_module_imports():
    """Test that gen.py can be imported"""
    try:
        import gen
        assert hasattr(gen, 'W'), "gen module should have W list"
        assert hasattr(gen, 'A'), "gen module should have A function"
        assert hasattr(gen, 'T'), "gen module should have T function"
    except Exception as e:
        raise AssertionError(f"Failed to import gen: {e}")


def test_gen_w_is_list():
    """Test that W is a list"""
    import gen
    assert isinstance(gen.W, list), "W should be a list"


def test_gen_a_function():
    """Test A function appends to W"""
    import gen
    initial_count = len(gen.W)
    gen.A('<test>')
    assert len(gen.W) == initial_count + 1, "A() should append to W"
    assert gen.W[-1] == '<test>', "A() should append correct value"
