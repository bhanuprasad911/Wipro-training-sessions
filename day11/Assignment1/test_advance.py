import pytest

# 1. Parameterization: Testing multiple input combinations
@pytest.mark.parametrize("input_val, expected", [
    (2, 4),
    (3, 9),
    (10, 100),
])
def test_squares(input_val, expected):
    assert input_val ** 2 == expected

# 3 & 5. Using CLI options and Config values
def test_environment_logic(env_config, pytestconfig):
    # Reading from pytest.ini (Requirement 3)
    ini_env = pytestconfig.getini("env_name")
    
    print(f"Running in CLI env: {env_config}")
    print(f"Default INI env: {ini_env}")
    assert env_config in ["dev", "staging", "prod"]

# 4. Handling Skips and Expected Failures
@pytest.mark.skip(reason="Functionality not yet implemented in v1.0")
def test_upcoming_feature():
    assert True

@pytest.mark.xfail(reason="Known bug in legacy API", strict=True)
def test_known_broken_logic():
    # This test is expected to fail
    assert 1 == 2

@pytest.mark.skipif(True, reason="Conditional skip: only runs on Linux")
def test_os_specific():
    pass