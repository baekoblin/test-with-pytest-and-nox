# test_env.py
import pytest

def test_environment(env):
    if env == "prod":
        # 프로덕션 환경 설정
        assert True
    elif env == "dev":
        # 개발 환경 설정
        assert True
    else:
        pytest.fail("Unknown environment")
