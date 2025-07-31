############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    max_val = 0                            # 최댓값 저장을 위한 변수를 0으로 초기화
    max_x = 0                              # 최댓값의 행을 저장하기 위한 변수를 0으로 초기화
    max_y = 0                              # 최댓값의 열을 저장하기 위한 변수를 0으로 초기화
    for i in range(len(matrix)):           # 2차원 행렬을 2중 for문으로 순회
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:     # 최댓값을 찾음. 이 때, >를 사용해서 가장 큰 값이 여러 개일 경우 먼저 등장한 좌표로 저장하도록 함.
                max_val = matrix[i][j]     # 최댓값 저장
                max_x = i                  # 최댓값의 행 저장
                max_y = j                  # 최댓값의 열 저장
    res_list = list()                      # 결과 반환을 위한 빈 리스트
    res_list.append(max_x)                 # 가장 큰 값을 가지는 행 좌표 추가
    res_list.append(max_y)                 # 가장 큰 값을 가지는 열 좌표 추가
    return res_list                        # 결과 반환


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################
