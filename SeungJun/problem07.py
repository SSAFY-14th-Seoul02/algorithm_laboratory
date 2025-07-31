############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
def reverse_string(s):
    res_str = ''                                 # 결과값을 위한 res_str 변수 초기화
    if len(s) == 1:                              # 재귀적으로 문자열을 함수에 넣어주면서 len(s)가 1인 지점
        res_str = s[0]                           # 즉, 제일 끝 문자열인 경우 res_str에 넣고 반환
        return res_str
    else:                                        # 끝 문자열이 아닐 경우, 내부의 재귀 함수로부터 반환받은
        res_str = reverse_string(s[1:]) + s[0]   # 문자열에 해당 함수의 첫째 문자열 추가해서 반환
        return res_str

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_string('hello'))  # 'olleh'
print(reverse_string('world'))  # 'dlrow'
print(reverse_string('python'))  # 'nohtyp'
#####################################################
