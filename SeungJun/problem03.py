############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, len, filter, 리스트 count 메서드 사용 시 감점
def defect_rate(results):
    total_cnt = 0                # 입력될 리스트의 총 길이를 구하기 위한 변수를 0으로 초기화
    fail_cnt = 0                 # 입력된 문자열이 'fail'인 경우의 갯수를 위한 변수를 0으로 초기화
    for i in results:            # results를 순회하면서 총 길이를 측정하고
        total_cnt += 1
        if i == 'fail':          # 해당 문자열이 'fail'인 경우 fail_cnt를 증가시켜서 fail 갯수 측정
            fail_cnt += 1
    return fail_cnt / total_cnt  # 불량 부품 비율을 계산해서 반환
        

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(defect_rate(['pass', 'fail', 'pass', 'fail']))   # 0.5
print(defect_rate(['pass', 'pass']))                   # 0.0
print(defect_rate(['fail', 'fail', 'fail']))           # 1.0
#####################################################