## 정규표현식(Regular Expression)에 대해 공부해보고, 이에 대해 설명하는 저장소입니다.
---

### 1. 정규표현식이란?
- 문자열 내에 있는 복잡한 패턴을 식별하거나 조작하는데 사용되는 문자열 패턴입니다. 
- 이 문자열 패턴은 단순히 특정 단어나 문자열을 찾는 것 이상으로, 특정 구조를 가진 문자열을 찾거나, 문자열의 특정 부분을 추출하거나, 일치하는 문자열 전체나 일부를 다른 문자열로 바꾸는 등의 작업을 가능하게 합니다.
- 이는 일반적인 문자열 검색 및 대체 작업에서 복잡하거나 변동성이 있는 문자열 패턴을 식별할 수 있는 강력한 도구로 쓰입니다. 
- 파이썬과 같은 많은 프로그래밍 언어는 이런 패턴을 처리하기 위한 내장 지원을 제공합니다.

### 2. 정규표현식의 사용 분야
- 정규 표현식을 사용하면 이메일 주소의 유효성을 검사하거나, 웹페이지에서 URL을 추출하거나, 코드에서 특정 주석을 찾아 제거하는 등의 작업을 수행할 수 있습니다. 
- 이런 강력한 기능 때문에 정규 표현식은 데이터 처리, 웹 스크래핑, 텍스트 처리, 로그 파일 분석 등 다양한 분야에서 많이 사용됩니다.

### 3. 메타 문자 (Meta characters)
- 메타 문자란 문자가 가진 원래의 의미가 아닌 특별한 용도로 사용되는 문자를 말합니다. 정규표현식에서 사용되는 메타 문자는 다음과 같습니다.
```
. ^ $ * + ? \ | ( ) { } [ ]  
```
---
#### [] 문자 클래스
- 정규표현식에서 대괄호 [] 는 대괄호 안에 포함된 문자들 중 하나와 매치를 뜻한다.
```
[abc] # abc 중 하나와 매치
```
```
'a' # a와 매치
'boy' # b와 매치
'dye' # a, b, c 중 어느 문자와도 매치되지 않음
```

- [] 안의 두 문자에 -를 사용하면 두 문자 사이의 범위를 뜻한다.
```
[a-c] # [abc]와 같음
[0-5] # [012345]와 같음
[a-zA-Z] # 모든 알파벳
[0-9] # 숫자
```

- [] 안에서 ^는 반대를 뜻한다.
```
[^0-9] # 숫자를 제외한 문자만 매치
[^abc] # a, b, c를 제외한 모든 문자와 매치
```
---
#### . 모든 문자
- .은 줄바꿈 문자인 \n 을 제외한 모든 문자와 매치된다.
```
a.b # 'a + 모든 문자 + b'를 뜻함
```
```
aab # a와 b 사이의 a는 모든 문자에 포함되므로 매치
a0b # a와 b 사이의 0은 모든 문자에 포함되므로 매치
abc # a와 b 사이에 문자가 없기 때문에 매치되지 않음
```
- [] 사이에서 .을 사용할 경우 문자 원래의 의미인 마침표가 된다.
```
a[.]b
```
```
a.b # a와 b 사이에 마침표가 있으므로 매치
a0b # a와 b 사이에 마침표가 없으므로 매치 안됨
```
---
#### * 반복
- * 앞에 오는 문자가 0개를 포함하여 몇 개가 오든 모두 매치된다.
```
lo*l
```
```
ll # 매치
lol # 매치
looool # 매치
looooooooooooooooooooool # 매치
lbl # 매치 안됨
loooooooooooobooooooool # 매치 안됨
```
---
#### + 최소 한 번 이상 반복
- + 앞에 있는 문자가 최소 한 번 이상 반복되어야 매치된다.
```
lo+l
```
```
ll # 매치 안됨
lol # 매치
looooool # 매치
```
---
#### ? 없거나 하나 있거나
? 앞에 있는 문자가 없거나 하나 있을 때 매치된다.
```
lo?l
```
```
ll # 매치
lol # 매치
lool # 매치 안됨
```
---
#### {m, n} 반복 횟수 지정
- {m, n} 앞에 있는 문자가 m 번에서 n 번까지 반복될 때 매치된다.
```
 lo{3, 5}l
 ```
 ```
 ll # 매치 안됨
 lol # 매치 안됨
 loool # 매치
 loooool # 매치
 looooool # 매치 안됨
 ```
- {m}의 형태로 사용하면 반드시 m 번 반복인 경우만 매치된다.
- {0,} 는 *, {1,} 는 +, {0,1} 는 ? 와 각각 동일하다.
---
#### | 여러 개의 표현식 중 하나
여러 개의 정규표현식들을 | 로 구분하면 or 의 의미가 적용되어 정규표현식들 중 어느 하나와 매치된다.
```
a|b|c # hello or hi or bye
```
```
a # 매치
b # 매치
c # 매치
a b # 매치
a b c # 매치
d # 매치 안됨
```
---
#### ^ 문자열의 제일 처음과 매치
- 문자열이 ^의 뒤에 있는 문자로 시작되면 매치된다. 여러 줄의 문자열일 경우 첫 줄만 적용된다. (단, re.MULTILINE 옵션이 적용되면 각 줄의 첫 문자를 검사하여 매치된다.)
```
^a
```
```
a # 매치
aaa # 매치
baaa # 매치 안됨
1aaa # 매치 안됨
```
---
#### $ 문자열의 제일 마지막과 매치
문자열이 $의 앞에 있는 문자로 끝나면 매치된다. 여러 줄의 문자열일 경우 마지막 줄만 적용된다. (단, re.MULTILINE 옵션이 적용되면 각 줄의 마지막 문자를 검사하여 매치된다.)
```
a$
```
```
a # 매치
aa # 매치
baa # 매치
aabb # 매치안됨
```
---
#### \A , \Z
- \A 는 ^ 와 동일하지만 re.MULTILINE 옵션을 무시하고 항상 문자열 첫 줄의 시작 문자를 검사한다. \Z 는 $ 와 동일하지만 re.MULTILINE 옵션을 무시하고 항상 문자열 마지막 줄의 끝 문자를 검사한다.
---
#### 조건이 있는 표현식
- 표현식1(?=표현식2): 표현식1 뒤의 문자열이 표현식2와 매치되면 표현식1 매치.
```
'hello(?=world)' # hello 뒤에 world가 있으면 hello를 매치
```
```
helloworld # hello 뒤에 world가 있기 때문에 hello가 매치됨
byeworld # hello가 없기 때문에 매치 안됨
helloJames # hello 뒤에 world가 없기 때문에 매치 안됨
```
- 표현식1(?!표현식2): 표현식1 뒤의 문자열이 표현식2와 매치되지 않으면 표현식1 매치.
```
'hello(?!world)' # hello 뒤에 world가 없으면 hello를 매치
```
```
helloworld # hello 뒤에 world가 있기 때문에 매치 안됨
byeworld # hello가 없기 때문에 매치 안됨
helloJames # hello 뒤에 world가 없기 때문에 hello가 매치됨
```
- (?<=표현식1)표현식2: 표현식2 앞의 문자열이 표현식1과 매치되면 표현식2 매치.
```
'(?<=hello)world' # world 앞에 hello가 있으면 world를 매치
helloworld # world 앞에 hello가 있기 때문에 world가 매치됨
byeworld # world 앞에 hello가 없기 때문에 매치 안됨
helloJames # world가 없기 때문에 매치 안됨
```
- (?<!표현식1)표현식2: 표현식2 앞의 문자열이 표현식1과 매치되지 않으면 표현식2 매치.
```
'(?<!hello)world' # world 앞에 hello가 없으면 world를 매치
```
```
helloworld # world 앞에 hello가 있기 때문에 매치 안됨
byeworld # world 앞에 hello가 없기 때문에 world가 매치됨
helloJames # world가 없기 때문에 매치 안됨
```
---
### re Python 정규표현식 모듈
- Python 에서는 re 모듈을 통해 정규표현식을 사용한다.
```
import re
```
---
#### compile 정규표현식 컴파일
- re.compile() 명령을 통해 정규표현식을 컴파일하여 변수에 저장한 후 사용할 수 있다.
```
변수이름 = re.compile('정규표현식')
```
- 정규표현식을 컴파일하여 변수에 할당한 후 타입을 확인해보면 _sre.SRE_Pattern 이라는 이름의 클래스 객체인 것을 볼 수 있다.
```
p = re.compile('[abc]')
print(type(p))
```
<class '_sre.SRE_Pattern'>
---
### 패턴 객체의 메서드
- 패턴 객체는 매치를 검색할 수 있는 네 가지 메서드를 제공한다.
다음의 정규표현식으로 각각의 메서드를 비교해본다.
```
p = re.compile('[a-z]+')
```
---
#### match: 시작부터 일치하는 패턴 찾기
- 문자열의 처음 시작부터 검색하여 일치하지 않는 부분이 나올 때까지 찾는다.
```
p.match('aaaaa')
<_sre.SRE_Match object; span=(0, 5), match='aaaaa'>

p.match('bbbbbbbbb')
<_sre.SRE_Match object; span=(0, 9), match='bbbbbbbbb'>

p.match('1aaaa')
None

p.match('aaa1aaa')
<_sre.SRE_Match object; span=(0, 3), match='aaa'>
```
- 검색의 결과로 _sre.SRE_Match 객체를 리턴한다.
--- 
#### search: 전체 문자열에서 첫 번째 매치 찾기
- 문자열 전체에서 검색하여 처음으로 매치되는 문자열을 찾는다.
```
p.search('aaaaa')
<_sre.SRE_Match object; span=(0, 5), match='aaaaa'>

p.search('11aaaa')
<_sre.SRE_Match object; span=(2, 6), match='aaaa'>

p.search('aaa11aaa')
<_sre.SRE_Match object; span=(0, 3), match='aaa'>

p.search('1aaa11aaa1')
<_sre.SRE_Match object; span=(1, 4), match='aaa'>
```
match와 동일한 형태로 결과를 출력해준다.
---
#### findall: 모든 매치를 찾아 리스트로 반환
- 문자열 내에서 일치하는 모든 패턴을 찾아 리스트로 반환한다.
```
p.findall('aaa')
['aaa']

p.findall('11aaa')
['aaa']

p.findall('1a1a1a1a1a')
['a', 'a', 'a', 'a', 'a']

p.findall('1aa1aaa1a1aa1aaa')
['aa', 'aaa', 'a', 'aa', 'aaa']
```
---
#### finditer: 모든 매치를 찾아 반복가능 객체로 반환
```
p.finditer('a1bb1ccc')
<callable_iterator object at 0x7f850c4285f8>
```
- callable_iterator라는 객체가 반환되었다. for을 사용하여 하나씩 출력해보자.
```
f_iter = p.finditer('a1bb1ccc')
for i in f_iter:
    print(i)
```
```
<_sre.SRE_Match object; span=(0, 1), match='a'>
<_sre.SRE_Match object; span=(2, 4), match='bb'>
<_sre.SRE_Match object; span=(5, 8), match='ccc'>
```
- 반복가능 객체는 각 매치의 결과인 매치 객체를 포함하고 있다.
---
#### 매치 객체의 메서드
- 패턴 객체의 메서드를 통해 리턴된 매치 객체는 아래와 같은 정보를 담고 있다.
```
<_sre.SRE_Match object; span=(매치 시작지점 인덱스, 매치 끝지점 인덱스), match='매치된 문자열'>
```
```
p = re.compile('[a-z]+')
result = p.search('1aaa11aaa1')
print(result)
# 위의 코드를 실행하면 아래의 매치 오브젝트를 얻는다.

<_sre.SRE_Match object; span=(1, 4), match='aaa'>
# 매치 객체의 메서드를 실행한 결과는 아래와 같다.

result.group()
aaa

result.start()
1

result.end()
4

result.span()
(1, 4)
```
--- 
#### () 그룹화
- 정규표현식을 () 안에 넣으면 그 부분만 그룹화된다. groups 메서드를 통해 그룹들을 튜플 형태로 리턴 할 수 있다.
```
p = re.search('(hello)(world)', 'helloworld') # 정규표현식 hello와 world의 매치 결과를 각각 그룹화하였다
grouping = p.groups()
print(grouping)
```
- ('hello', 'world') # 각 그룹의 매치 결과가 튜플로 묶여서 리턴됨
- group 메서드를 통해 각 그룹을 호출할 수 있다.
```
p.group() # 인자를 넣지 않으면 전체 매치 결과 리턴
helloworld

p.group(0) # group()와 같다
helloworld

p.group(1) # 1번 그룹 매치 결과 리턴
hello

p.group(2) # 2번 그룹 매치 결과 리턴
world
```
---
#### 그룹 이름 지정
- 그룹에 이름을 지정하려면 다음과 같이 한다.
```
(?P<그룹이름>표현식)
```
- 표현식 a의 매치 결과는 그룹 first에 저장되고 표현식 b의 매치 결과는 그룹 second에 저장된다.
```
re.match('(?P<first>a)(?P<second>b)', 'ab')
<_sre.SRE_Match object; span=(0, 2), match='ab'>
```
- 위의 표현식은 그룹화가 된다는 점을 제외하면 아래의 표현식과 동일한 결과를 돌려준다.
```
re.match('ab', 'ab')
<_sre.SRE_Match object; span=(0, 2), match='ab'>
```
---
#### 그룹 재참조
- 그룹을 지정하면 같은 \그룹번호 와 같은 형식으로 표현식 내에서 다시 호출하여 사용할 수 있다.
이 때, 반드시 표현식 앞에 r 을 붙여야 제대로 작동한다. 이에 대해서는 아래에 자세히 설명한다.
```
re.match(r'(a)(b)\1\2', 'abab') # 표현식 'abab'와 동일하다
<_sre.SRE_Match object; span=(0, 4), match='abab'> # abab가 모두 매치되었다
```
- 그룹의 이름을 지정하였을 경우 (?P=그룹이름) 의 형식으로 호출할 수 있다.
```
re.match('(?P<first>a)(?P<second>b)(?P=first)(?P=second)', 'abab') # 표현식 'abab'와 동일하다
<_sre.SRE_Match object; span=(0, 4), match='abab'> # abab가 모두 매치되었다
```
---
#### 컴파일 옵션
- 정규표현식을 컴파일 할 때 옵션을 지정해줄 수 있다.
```
변수이름 = re.compile('정규표현식', re.옵션)
```
---
#### DOTALL, S
- .은 줄바꿈 문자 \n 를 제외한 모든 것과 매치된다. 컴파일 할 때 re.DOTALL 또는 re.S 옵션을 넣어주면 \n 까지 매치되도록 할 수 있다.
```
p = re.compile('.') # 옵션 없음
result = p.findall('1a\nbc')
print(result)
```
- ['1', 'a', 'b', 'c'] # \n이 매치되지 않음
```
p = re.compile('.', re.DOTALL) # re.DOTALL 옵션 추가
result = p.findall('1a\nbc')
print(result)
```
['1', 'a', '\n', 'b', 'c'] # \n까지 매치
---
#### IGNORECASE, I
- re.IGNORECASE 또는 re.I 옵션을 넣어주면 대소문자를 구별하지 않고 매치된다.
```
p = re.compile('[a-z]') # 소문자만 매치
result = p.findall('aAbB')
print(result)
```
- ['a', 'b']
```
p = re.compile('[a-z]', re.IGNORECASE) # re.IGNORECASE 옵션 추가
result = p.findall('aAbB')
print(result)
```
['a', 'A', 'b', 'B'] # 소문자와 대문자 모두 매치
---
#### MULTILINE, M
- re.MULTILINE 또는 re.M 옵션을 넣어주면 여러 줄의 문자열에 ^ 와 $ 를 적용할 수 있다.
```
text = '''student-1-name: James
student-2-name: John
student-3-name: Jordan
teacher-1-name: Mike
student-5-name: John'''
```
```
p = re.compile('^student.*') # 뒤따라 오는 문자 종류와 개수에 상관없이 student로 시작하는 문자열 매치 
result = p.findall(text)
print(result)
```
- ['student-1-name: James'] # 첫 줄만 매치되었다.
```
p = re.compile('^student.*', re.MULTILINE) # re.MULTILINE 옵션 추가
result = p.findall(text)
print(result)
```
- ['student-1-name: James', 'student-2-name: John', 'student-3-name: Jordan', 'student-5-name: John']
- # student로 시작하는 모든 줄이 매치되었다.
```
p = re.compile('.*John$') # John으로 끝나는 문자열 매치
result = p.findall(text)
print(result)
```
- ['student-5-name: John'] # 가장 마지막 줄만 매치되었다
```
p = re.compile('.*John$', re.MULTILINE) # re.MULTILINE 옵션 추가
result = p.findall(text)
print(result)
```
- ['student-2-name: John', 'student-5-name: John'] # John으로 끝나
---
#### VERBOSE, X
- re.VERBOSE 또는 re.X 옵션을 주면 좀 더 가독성 좋게 정규표현식을 작성할 수 있게 된다. 아래의 두 표현식은 동일하게 작동한다.
```
p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
```
```
p = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE) # re.VERBOSE 옵션 추가
```
- re.VERBOSE 옵션을 추가하면 정규표현식에 컴파일시 자동으로 제거되는 공백과 코멘트를 추가할 수 있게된다. (단, [] 안에 입력된 공백문자 제외)
---
### Python 정규표현식의 \ 문제
- Python에서 정규표현식에 \ 을 사용할 때 아래와 같은 문제가 발생할 수 있다.
```
text = '\section'
result = re.match('\\section', text)
print(result)
```
```
None
```
- \s는 공백문자를 뜻하는 메타문자로 인식되기 때문에 \section 이라는 문자열을 찾으려면 위해 이스케이프 코드 \\를 사용한 \\section 를 정규표현식에 입력해야한다.
- 그러나 Python 정규식 엔진에서 리터럴 규칙에 의해 \\ 가 \로 해석되어 전달된다.
- 따라서 \\ 를 문자 그대로 넘겨주어야하는데 이를 위해서는 \\\\ 로 입력해야한다.
```
text = '\section'
result = re.match('\\\\section', text)
print(result)
```
```
<_sre.SRE_Match object; span=(0, 8), match='\\section'>
```
- 가독성이 심각하게 저하되는데 이를 방지하기 위해 다음과 같이 작성한다.
```
text = '\section'
result = re.match(r'\\section', text) # raw string을 뜻하는 r을 앞에 붙여준다.
print(result)
```
```
<_sre.SRE_Match object; span=(0, 8), match='\\section'>
```
- 정규표현식 앞에 r은 항상 붙여주는 것이 권장된다.
---
< Reference >
- 정규 표현식에 대한 정의와 사용 분야 : Chat GPT
- 정규 표현식 문법 : Che1's Blog [https://nachwon.github.io/regular-expressions/]
- 정규 표현식 문법 : 이한영 강사님 github
- 정규 표현식 문법 : 점프 투 파이썬 [https://wikidocs.net/4308]
