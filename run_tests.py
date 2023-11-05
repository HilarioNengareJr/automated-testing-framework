import pytest

if __name__ == '__main__':
    pytest.main(['-m', 'register', 'tests'])
    pytest.main(['-m', 'login', 'tests'])
    pytest.main(['-m', 'register_fail', 'tests'])
    pytest.main(['-m', 'login_fail', 'tests'])