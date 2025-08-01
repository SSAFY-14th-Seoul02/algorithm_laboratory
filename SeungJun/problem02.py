############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    res = str_list[0]         # 길이가 가장 긴 문자열을 반환하기 위한 res를 str_list의 첫번째 인자로 초기화
    for s in str_list:        # str_list를 순회
        s_len = 0             # 해당 반복의 문자열 s의 길이를 측정하기 위한 변수를 0으로 초기화
        res_len = 0           # 현재 가장 긴 문자열로 판단되고 있는 문자열의 길이를 측정하기 위한 변수를 0으로 초기화
        for i in s:           # 해당 반복의 문자열 s를 순회하면서 길이 측정
            s_len += 1
        for i in res:         # 현재 가장 긴 문자열인 res를 순회하면서 길이 측정
            res_len += 1
        if s_len > res_len:   # 가장 긴 문자열을 판단해서 해당 문자열로 변경.
            res = s           # 이 때, >=이 아닌 >를 사용해서 같은 길이의 문자열일 경우 먼저 찾은 문자열을 반환하도록 함.
    return res

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(longest_string(['apple', 'banana', 'cherry', 'date']))  # 'banana'
print(longest_string(['cat', 'caterpillar', 'dog', 'elephant']))  # 'caterpillar'
print(longest_string(['a', 'ab', 'abc', 'abcd']))  # 'abcd'
#####################################################
