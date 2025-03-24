## enumerate() 사용법🚀
- enumerate()는 리스트, 튜플 등 반복 가능한(iterable) 객체를 순회할 때, 인덱스와 값을 동시에 가져오는 함수
- `enumerate(iterable, start=0)`
    - iterable: 리스트, 튜플, 문자열 등 반복 가능한 객체
    - start: 인덱스 시작 값 (기본값은 0)

- ```python
    fruits = ["apple", "banana", "cherry"]

    for index, fruit in enumerate(fruits):
    print(index, fruit)
    # 0 apple
    # 1 banana
    # 2 cherry
    ```
    - ➡ enumerate(fruits)를 사용하면 (인덱스, 값) 형태의 튜플이 반환

- start 값 변경하기
    - ```python
        fruits = ["apple", "banana", "cherry"]

        for index, fruit in enumerate(fruits, start=1):  # 인덱스를 1부터 시작
        print(index, fruit)
        # 1 apple
        # 2 banana
        # 3 cherry
        ```
- 리스트 컴프리헨션과 함께 사용
    - ```python
        fruits = ["apple", "banana", "cherry"]
        fruit_list = [(i, fruit) for i, fruit in enumerate(fruits)]
        print(fruit_list)
        # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
        ```

- 딕셔너리로 변환하기
    - ```python
        fruits = ["apple", "banana", "cherry"]
        fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}
        print(fruit_dict)
        # {0: 'apple', 1: 'banana', 2: 'cherry'}
        #  ➡ 인덱스를 키, 값을 값으로 하는 딕셔너리
        ```

- 인덱스가 필요한 경우 enumerate() 활용하기
    - range(len(리스트))를 쓰는 대신 enumerate()를 쓰기
    - ```python
        # 일반적인 방법
        fruits = ["apple", "banana", "cherry"]
        for i in range(len(fruits)):
         print(i, fruits[i])

        # enumerate 사용
        for i, fruit in enumerate(fruits):
        print(i, fruit)
        ```