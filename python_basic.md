## python

1. ✅ for문에는 반복가능한 객체만 들어온다
  - str ()
  - list []
  - tuple ()  
  - dict {'k': v}
  - range () 숫자 반복


2. ✅ int는 len이 되지않는다.
 - 해결방법 > int를 str로 바꿔서하기
 - ```
        a = 4321
        n = len(str(a))
        print(n) # 4
    ```
3. ✅ while n:
   - n이 0이 될때까지 반복한다는 의미


4. ✅ 문자열 (str)에서는 append()를 사용할 수 없다.

- append는 list에서만 사용가능
- 문자열을 list로 변환후 사용 가능
- ```
    s = list("hello")  # 문자열 → 리스트 변환
    s.append("!")      # 리스트에 "!" 추가
    s = "".join(s)     # 리스트 → 문자열 변환
    print(s)  # "hello!"
    ```

5. ✅ `''.join()`은 리스트나 문자열들의 모음을 넣어야 함(문자 하나는 안됨)

6. ✅ `.replace('바꿀함수', '바꾸는함수 ')`
- 문자를 공백으로 바꾸고싶다면 
```        
    def solution(my_string, letter):
    return my_string.replace(letter, '') # letter에 포함된 글자를 ''으로 변형
```

7. ✅ `range(1, 10)` 함수는 1부터 9까지를 (int)형태로 출력 그러므로 '1'은 str형태이므로 비교가 안됨 비교하려면 변환이 필요 (숨어있는 숫자의 덧셈 참고)

8. ✅ `map(function, iterable)` 함수
    - ```numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # = > ['1', '2', '3'...'10'] 숫자를 글자로 바꾸고 싶을 때 int > str

        result = []
        for number in numbers:
        result.append(str(number)) # 여기서 append가 되는 이유: result가 list이기 때문에 append()에는 어떤 자료형이 와도 상관없다

        print(result)
        ```
    - 위에 int > str로 바꾸는 과정을 map함수로 한번에 할 수 있음
        `map(str, numbers)`
    - map 함수는 반드시 **list** 형태로 저장해줘야함 
        `list(map(str, numbers)))` 
    - ❌ map 객체는 직접 비교가 불가능 (map(a)>0) ❌
        - 리스트 형태로 바꿔서 해야함(`dot_int = list(map(int, dot[:]`)))
9. ✅ dict (순서가 없음)
    - pop() : 순서가 없어서 맨 끝 데이터를 pop 할 수 없음 pop('k')
    - dict['k'] = 'a' k 값의 v를 변경하고싶을때
    - dict.keys() / dict.values() : key와 value를 출력
    - dict.items() : k, v를 모두 출력
    - for문을 이용한 dict 저장 방법
        ```python
            my_dict = {}
            for i in range(5):  # 0부터 4까지 반복
                my_dict[f'key{i}'] = i * 10  # f-string을 이용해 key 이름 만들기

            print(my_dict) # {'key0': 0, 'key1': 10, 'key2': 20, 'key3': 30, 'key4': 40}
        ```

10. ✅ list + 1 = ?
    ```
        def solution(num_list):
        answer = [0,0] 
        for n in num_list:
        answer[n%2]+=1
        return answer
    ```
    print(solution([1, 2, 3, 4, 5]))이 결과를 얻을 때
    answer[1%2==1] = [0, 0] + 1
     = >answer[1] = [0 , 1] # 왜냐면 answer[1]에 들어가니깐
     = > 리스트의 특정 인덱스 값을 직접 바꾸는 방법은 
         ```
            my_num = [1, 2, 3]
            my_num[1] = 1
            my_num[2] = 2
            print(my_num) # 112
         ```    
    - '.append()' : 리스트의 끝에 값을 추가할 때
    - '.insert(인덱스번호, 삽입할 값)' : 리스트의 특정 위치에 값을 삽입할 때
    - '.extend([삽입할 값들])' : 리스트에 리스트를 추가할 때  

11. ✅ import 
    - import 패키지로 내가 원하는 패키지를 불러옴
    - 예를 들어 import math를 하게되면 math.pi = 3.14 등 math라는 패키지에 저장된 값이 나옴

12. ✅ import random
    - random의 패키지를 불러옴
    - random.randint(a, b) => a와 b사이에서 랜덤한 숫자 출력
    - random.sample(range(a, b), n) => a와 b사이에서 n개의 랜덤한 숫자 선택

13. ✅ request 외부라이브러리
    -  params = {'k1': v1, 'k2': v2...} 서버에 요청할 때 필요한 검색 조건이나 필터 정보등을 url에 담아 보낼 때 사용
    -  payload = {} 전달할 데이터라는 의미 
    1. import requests (먼저 request 모듈을 불러옴)    
    2. response = requests.get('url') (내가 원하는 사이트의 url을 불러옴)
    3. payload에 내가 필요한 k와 v 값들을 저장
    4. res = requessts.get('url', params=payload)
    5. res = res.json() => 디렉터리 형태로 저장

    - beautifulsoup을 이용해서 내가 requests로 불러온 html 소스에서 원하는 정보를 추출
        1. import bs4
        2. soup = bs4.BeautifulSoup(response.txt, 'html.parser')
          = > 이렇게 하면 beautifulsoup을 이용해 원하는 부분만 추출 가능
        3. find를 사용해서 원하는 정보 추출하기
            soup.find() < 여기다가 원하는 정보를 검색

 14. ✅ .split() 함수  
    - 문자열을 특정 구분자를 기준으로 나누어 리스트로 반환하는 함수
      ``` python         
            text = "사과,바나나,체리"
            fruits = text.split(",")
            print(fruits)

         # 출력: ['사과', '바나나', '체리']
        ```

    ``` python
        a, b = map(int, input.split)
        print(a + b)     
    ```
    - > 여기서 .split을 한 이유: .split을 하지않으면 35를 입력하면 3, 5 각각의 숫자로 되고 35 20 이런 공백으로 입력하면 오류가 난다  

15. ✅ \ (이스케이프 문자) 출력하기
    - 1. \\ 두번 사용하기
    - 2. `r''`이용하기 ex)`print(r"이것은 백슬래시: \")`                
    - 3. 맨 끝에 \가 오면 안됨 \\두개 써줘야함
    - 4. `print(' )  ( \')')` '안에 (')를 쓰고싶다면 역슬래시(\)로 이스케이프 처리 '

![스크린샷](/1.png)

16. ✅ else 문 안에 if와 elif를 중첩 할 수 있음

17. ✅ sys.stdin.readline()을 언제 써?
    - import sys 필수!!
    - 💡 많은 입력을 받을 때!
    - 예를 들어 100만 개의 숫자 입력을 받을 때, input()을 쓰면 너무 느려! 이때 sys.stdin.readline()을 쓰면 속도가 훨씬 빨라져! 🚀
    - 뒤에 \n 이 자동으로 붙기 때문에 .rstrip()을 해줘야 함!
    - 

18. ✅ .rstrip() vs .strip() vs .lstrip()

 - .rstrip()	문자열의 오른쪽 끝 공백(\n 포함) 제거
 - .lstrip()	문자열의 왼쪽 공백 제거
 - .strip()	    문자열 양쪽 공백 제거

19. ✅` _`는 반복 변수지만, 값을 안 쓸 거라 그냥 _로 표기한 것!
    - ex) for _ in range(T):

20. ✅ 공백 출력
 - ✅. 공백 한 칸 넣기
    - ```print("Hello", "World") ``` # 기본적으로 공백이 자동 추가됨, Hello World
 - ✅ 2. sep 옵션 활용하기
    - ``` print("Hello", "World", sep="💖") ```# Hello💖World
 - ✅ 3. 줄 바꿈 없이 공백 출력
    - ```print("Hello", end=" ")  print("World")``` # Hello World 
        - ✔️ end=" " → 줄 바꿈 대신 공백 출력
        - ✔️ 기본적으로 end="\n" (줄 바꿈)이 설정되어 있음

21. ✅ try와 except 기본 구조
    - ``` 
        try: 
            # 실행할 코드    
        except 예외:
            # 예외가 발생했을 때 실행할 코드 ```
        
     - 🔹 try 블록: 문법적으로 오류가 있을 수 있는 코드를 try 블록에 넣음.
    - 🔹 except 블록:
try 블록에서 오류가 발생하면, 어떤 예외(오류)가 발생했는지를 **except**로 처리할 수 있음
        - except는 특정 예외만 처리하거나 모든 예외를 처리할 수 있음

22. ✅ 입력 개수가 정해져 있지 않은 문제들을 해결하는 방법
    - 📝 입력이 끝나는 시점을 프로그램이 직접 알 수 없기 때문에, EOF를 감지해야 함
    - sys.stdin.readline()	빈 문자열("") 반환	ValueError 발생
    - input()	EOFError 발생	EOFError 발생
        - ✔️ sys.stdin.readline() 사용하면 except: 로 모든 예외를 처리해야 함!
        - ✔️ input() 사용하면 except EOFError: 만 처리하면 됨!

23. ✅ remove()
    - `.remove()`는 list에서 특정 요소를 지우는 메서드
    - ()직접적으로 list를 넣을 수 없음, ex('a', 'e')  ❌ ('a') ⭕
    