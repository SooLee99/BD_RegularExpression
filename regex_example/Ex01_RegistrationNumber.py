# 예제1) 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해 보자.
"""
우선 정규식을 전혀 모르면 다음과 같은 순서로 프로그램을 작성해야 할 것이다.
    1. 전체 텍스트를 공백 문자로 나눈다(split).
    2. 나뉜 단어가 주민등록번호 형식인지 조사한다.
    3. 단어가 주민등록번호 형식이라면 뒷자리를 *로 변환한다.
    4. 나뉜 단어를 다시 조립한다.
"""

# (1) 정규 표현식을 사용하지 않은 코드
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))


"""
위 코드의 결과 값:
park 800905-*******
kim  700905-*******

"""

# (2) 정규 표현식을 사용한 코드
import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


"""
위 코드의 결과 값:
park 800905-*******
kim  700905-*******

"""

# 결론 : 정규 표현식을 사용하면 이렇게 간단한 예제에서도 코드가 상당히 간결해진다는 것을 알 수 있다.
