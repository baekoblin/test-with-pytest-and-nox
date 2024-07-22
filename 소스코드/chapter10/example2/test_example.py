
# test_example.py

def test_custom_option(request):
    # 커스텀 옵션 값 가져오기
    custom_option = request.config.getoption("--custom-option")
    print(f"Custom option value: {custom_option}")

    # 현재 테스트 함수의 이름 가져오기
    test_name = request.node.name
    print(f"Test name: {test_name}")

    # 현재 테스트 파일의 경로 가져오기
    test_file = request.node.fspath
    print(f"Test file: {test_file}")

    # 현재 테스트 모듈 가져오기
    test_module = request.node.module.__name__
    print(f"Test module: {test_module}")

    # 현재 테스트 클래스 가져오기 (클래스 기반 테스트인 경우)
    test_class = request.node.cls.__name__ if request.node.cls else None
    print(f"Test class: {test_class}")
