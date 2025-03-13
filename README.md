# python

-처음 오면 가상환경 활성화 > jupyter lab
## 가상환경

-`python -m venv venv` : 가상환경 생성

-`source venv/Scripts/activat` : 가상환경 활성화
  - linux, mac의 경우 bin

-`deactivate` : 가상환경 비활성화

-`pip` : 파이썬 프로그램에 만들어진 다양한 도구들 

- ctrl + c : 종료


## 01_intro
  - 변수의 정의
  - 리스트, 튜플, range, string
  - set, dictionary

---

## 02_control_of_flow
  - if문
  - while문
  - for문
  - dictionary 반복
  - continue, breake
---

## 03_function
  - 함수의 선언과 호출
  - 함수의 return
  - lambda (임시 함수)
---

## 04_data_structure
  - 자료구조
  - 문자열 메소드
     - capitalize() - 시작 글자만 대문자로 바꾸기기
     - title() - 각각의 시작되는 단어를 대문자로 바꾸기기
     - lower() - 모든 문자를 소문자로 바꾸기기
     - upper() - 모든 문자를 대문자로 바꾸기기
    - .join()
    - .strip() - 원하는 문자를 지워줌
    - .replace() - 바꾸는 함수 두개의 정보가 필요함 (바꾸는 함수, 바꿀함수) 3은 앞에서부터 몇번 바꿀지 결정
    - .find() 
    - .split() - 리스트로 바꿔줌
  - 리스트 메소드
    - .append() - 추가하는 메소드
    - .extend() - 여러개의 데이터를 추가할 때
    - insert(a, b) - a번째에 b 집어넣기
    - .remove() - 제거
    - .pop() - 맨 마지막 데이터를 지울 때
    - .sort() -오름차순으로 정렬
    - .sort(reverse=True) - 내림차순순으로 만들기

  - 리스트 카피
    - 복사본을 변경해도 원본은 유지(import copy)

  - list comperhension
  
  - dictionary 메소드
    - .update(k = 'v') - v값 바꾸기
  
  - dict comprehension

  - set 메소드
  
  - map, filter, zip
  ---
  ## 05_module
  - import fact
    - fact.factorial(5) # 120
    - fact.my_max(2, 3) # 3
  - import random
    - random.randint(1,10) # 내가 지정한 범위 내에서 랜덤한 숫자
    - random.seed() 숫자 고정
    - random.sample(numbers, 2) # numbers에서 2개 뽑기기
  
  - datetime

  - 외부라이브러리
    - request
---
## 06_errors
  - 각종 에러들에 대해서
---

## 07_OOP
  - 객체지향 프로그래밍
    - class
    - 속성
    - 행동
    - 인스턴스
    - 상속
    - 다중상속

## 08_movie_data
  - 영화진흥위원회 데이터 수집