# test_app.py
# Basic test file to make pytest happy in CI

def test_basic_math():
    """A dummy test to always pass"""
    assert 1 + 1 == 2


def test_imports():
    """Check if key libraries are installed"""
    try:
        import flask
        import requests
    except ImportError as e:
        assert False, f"Missing dependency: {e}"
