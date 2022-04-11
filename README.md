# knurii.github.io

# 1. text 전처리
## - 허프만 부호화 알고리즘에 넣기 위한 데이터를 전처리 하였다.
## - 압축 효율을 높이고 성능분석을 편하게 하기 위함
## - 문장부호, 공백, 숫자, 특수문자 등을 제거
## **1) 알고리즘에 넣기 위한 txt 선정**
### - 영문으로 된 문서가 편리할 것 같아 alice_in_wonderland.txt 파일로 선정하였다.
### - github에서 다운로드
## **2) 파일 읽고 텍스트를 전처리 하는 코드 작성**
### - 작성 언어는 python
### - 파일 오픈 -> clean_text -> 쓰기 모드로 파일 오픈 후 전처리 된 결과를 파일에 작성 -> 파일 닫기
### 💻 작성 코드
```python
import os
from re import findall, sub

print('\n현재 경로 :', os.getcwd())

#파일 오픈-str 형태로 받아준다
with open("/Users/kimnuri/PycharmProjects/ComputerAlgorithm/huffman/data/alice_in_wonderland.txt") as f:
    content = " ".join([l.rstrip() for l in f])

#전처리 위한 함수 수행
def clean_text(content):
    texts_re = content.lower() #소문자로 변경
    texts_re2 = sub('[0-9]', '', texts_re) #숫자 제거
    texts_re3 = sub('[\'`,.?!;:"\-\[\]]', '', texts_re2) #문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3) #특수문자 제거
    texts_re5 = sub('[가-힣]','',texts_re4) #한글 제거
    texts_re6 = texts_re5.replace(' ','') #white space 제거
    return texts_re6

print(clean_text(content))

#위에서 처리된 결과를 파일에 다시 써준다
texts2 = open('/Users/kimnuri/PycharmProjects/ComputerAlgorithm/huffman/data/alice_in_wonderland.txt',mode='w',encoding='UTF8')
texts2.write(clean_text(content))
texts2.close()
```
### 💻 결과 화면
![결과1](https://user-images.githubusercontent.com/101931446/162650590-8cc73f34-e246-4459-80ac-b693f4ed0fab.png)
### **주의할 점**
#### - 파일 쓰기모드로 오픈 하였기 때문에 파일을 str 구조로 불러와야 했다.
#### - 문장 부호 제거에서 파이썬 언어로 인식 되는 부분들을 신경써야 했다.
## **3) 성능 분석을 위한 알파벳 빈도수와 텍스트 길이 계산**
### - 이론적으로 이진코드를 구하기 위해 알파벳 빈도수를 계산하였다.
### - 압축률을 이론적으로 구하기 위해 text의 길이를 계산하였다.
### 💻 작성 코드
```python
import os
from re import findall, sub

#파일 오픈-str구조로 받아온다
with open("/Users/kimnuri/PycharmProjects/ComputerAlgorithm/huffman/data/alice_in_wonderland.txt") as f:
    content = " ".join([l.rstrip() for l in f])

Alphabet = 'abcdefghijklmnopqrstuvwxyz' #for문에서 돌리기 위함과 빈도수를 계산하기 위해 미리 문자열을 만들어준다

texts_freq = [0] * 26

#알파벳 빈도수 계산
for al in content:
    if al in Alphabet:
        idx = Alphabet.find(al)
        texts_freq[idx] += 1

#알파벳 빈도수 출력
print("알파벳 빈도수")
for i in range(0,26):
    print(Alphabet[i], ":", texts_freq[i])

#텍스트 길이
print('texts 길이 =',len(content))
```
### 💻 결과 화면
![결과2](https://user-images.githubusercontent.com/101931446/162650689-7638a4a1-2557-47ec-a396-91296cd06181.png)


