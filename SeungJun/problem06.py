############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def grade_distribution(scores):
    res = dict()                              # 결과를 담을 딕셔너리 선언
    for key in scores:                        # scores를 순회하면서
        if scores[key] >= 90:                 # 점수 구간마다 분기
            temp_list = res.get('A', list())  # 결과 딕셔너리에서 해당 등급을 키로 하는 값이 있다면 가져오고 아니면 빈 리스트를 반환해주도록 get 사용
            temp_list.append(key)             # 현재 순회 중이던 key를 임시 리스트에 추가
            res['A'] = temp_list              # 결과 딕셔너리의 해당 등급의 키에 임시 리스트를 밸류로 저장
        elif scores[key] >= 80:
            temp_list = res.get('B', list())
            temp_list.append(key)
            res['B'] = temp_list
        elif scores[key] >= 70:
            temp_list = res.get('C', list())
            temp_list.append(key)
            res['C'] = temp_list
        elif scores[key] >= 60:
            temp_list = res.get('D', list())
            temp_list.append(key)
            res['D'] = temp_list
        elif scores[key] <= 59:
            temp_list = res.get('F', list())
            temp_list.append(key)
            res['F'] = temp_list
    return res                               # 결과 반환


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
case1 = {'Kim': 92, 'Lee': 75, 'Park': 88, 'Choi': 60}
# {'A': ['Kim'],  'C': ['Lee'], 'B': ['Park'], 'D': ['Choi']}
print(grade_distribution(case1))

print(grade_distribution({'Min': 95, 'Oh': 93}))       
# {'A': ['Min', 'Oh']}

case2 = {
    'Ahn': 90,   
    'Baek': 82,  
    'Choi': 75,  
    'Dong': 60,  
    'Eun': 59    
}
# {'A': ['Ahn'], 'B': ['Baek'], 'C': ['Choi'], 'D': ['Dong'], 'F': ['Eun']}
print(grade_distribution(case2))

case3 = {
    'Kim': 100,  
    'Lee': 89,   
    'Park': 70,  
    'Shin': 69,  
    'Yang': 0    
}
# {'A': ['Kim'], 'B': ['Lee'], 'C': ['Park'], 'D': ['Shin'], 'F': ['Yang']}
print(grade_distribution(case3))
#####################################################