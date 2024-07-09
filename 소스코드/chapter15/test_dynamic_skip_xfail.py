# test_dynamic_skip_xfail.py

import pytest

def is_feature_available():
    # 특정 기능의 사용 가능 여부를 확인하는 로직
    return False

def is_known_issue():
    # 알려진 문제 여부를 확인하는 로직
    return True

def test_dynamic_skip():
    if not is_feature_available():
        pytest.skip("Feature not available")
    assert True

def test_dynamic_xfail():
    if is_known_issue():
        pytest.xfail("Known issue")
    assert False
