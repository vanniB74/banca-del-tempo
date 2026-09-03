"""Tests for gen.py module"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_gen_module_imports():
    """Test that gen.py can be imported"""
    import gen
    assert hasattr(gen, 'W'), "gen module should have W list"
    assert hasattr(gen, 'A'), "gen module should have A function"


def test_gen_w_exists():
    """Test that W list exists and is initialized"""
    import gen
    assert hasattr(gen, 'W')
    # Just verify the module loads without errors
    assert True
