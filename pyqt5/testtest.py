import sys

# 현재 모듈의 이름 확인
current_module = sys.modules[__name__]

# 모듈 이름을 리스트에 추가
module_list = []
module_list.append(current_module.__name__)

print(f"현재 실행 중인 모듈: {current_module.__name__}")
print("모듈 리스트:", module_list)
