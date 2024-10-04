def solution(name, yearning, photo):
    # 딕셔너리로 만들어보자
    dic = {}
    for i in range(len(name)):
        dic.update({name[i]:yearning[i]})
    answer = []
    # 사진 점수 만들기
    for i in range(len(photo)):
        result = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                result += dic.get(photo[i][j])
        answer.append(result)
    return answer