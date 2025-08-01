############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, map 사용 시 감점

def calc_total(price_map, orders):
    res = 0                         # 주문한 물품의 총 금액을 위한 res 변수를 0으로 초기화
    for o in orders:                # orders를 순회하면서
        res += price_map.get(o, 0)  # 해당 물품이 price_map에 존재하면 가격을 반환하고 아니면 0을 반환하도록 get을 사용해 총합 계산
    return res                      # 총 금액 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(calc_total({'apple': 1000, 'pear': 800}, ['pear', 'apple', 'apple']))  # 2800
print(calc_total({'pen': 1200, 'note': 1500}, [])) # 0
print(calc_total({'apple': 1000, 'orange': 900, 'grape': 1200}, ['orange', 'orange'])) # 1800
#####################################################
