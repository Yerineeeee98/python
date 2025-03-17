### 🔹 random 함수 정리
- ✅ 1. random.randint(a, b)
    - a부터 b까지의 정수 하나 랜덤 선택
    ```
    import random
    num = random.randint(1, 10)  # 1~10 사이 정수 랜덤 선택
    print(num)  # 예: 4
    ```
- ✅ 2. random.choice(리스트)
    - 리스트에서 하나의 요소 랜덤 선택
    ```
    fruits = ["🍎", "🍌", "🍇", "🍊"]
    pick = random.choice(fruits)
    print(pick)  # 예: 🍇
    ```
- ✅ 3. random.sample(리스트, k)
    - 리스트에서 중복 없이 k개 랜덤 선택
    ```
    numbers = list(range(1, 46))  # 1~45 숫자 리스트
    lotto = random.sample(numbers, 6)  # 6개 뽑기
    print(lotto)  # 예: [3, 12, 22, 34, 41, 45]
    ```
- ✅ 4. random.shuffle(리스트)
    - 리스트의 요소를 섞음 (셔플)
    ```
    cards = ["A", "2", "3", "4", "5"]
    random.shuffle(cards)
    print(cards)  # 예: ['4', 'A', '3', '2', '5']
    ```
- ✅ 5. random.uniform(a, b)
    -  a부터 b까지의 실수(float) 랜덤 선택
    ```
    num = random.uniform(1, 10)  # 1~10 사이 실수 랜덤 선택
    print(num)  # 예: 3.876523
    ```
- 🎯 정리
    - ✅ random.choice() → 리스트, 튜플, 문자열, range에서 사용 가능
   -  ✅ random.sample() → 리스트, 튜플, 문자열, range, set에서 사용 가능
   -  ✅ random.choice()는 딕셔너리에서 직접 사용 불가 → list()로 변환해야 함
   -  ✅ random.sample()도 딕셔너리에서 직접 사용 불가 → list()로 변환해야 함


### 🔹 sort() vs sorted()
|   |sort()|sorted()|
|------|---|---|
|리스트 자체 변경|✅ (O)|❌ (X)|
|반환값|	None (없음)|	새로운 정렬된 리스트|
|원본 리스트 유지|	❌ (X)|	✅ (O)|
|사용 방법|	리스트.sort()|	sorted(리스트)|

-   ```
    pick = random.sample(range(1, 46), 6).sort()
    print(pick)  # None 출력됨 😭
    ```
     sort()는 리스트를 직접 정렬하지만 새로운 리스트를 반환하지 않음!
-   ```
    pick = sorted(random.sample(range(1, 46), 6))
    print(pick)  # 정렬된 리스트 출력 🎉
    ```
    sorted()는 새로운 정렬된 리스트를 반환하니까 pick에 저장 가능! 😊