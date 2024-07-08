# test_example.py

def test_custom_option(request):
    custom_option = request.config.getoption("--custom-option")
    assert custom_option == "default value"
