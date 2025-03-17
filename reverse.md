### 🌀 reverse()
- `.reverse()`
- reverse() 함수는 리스트의 요소들을 반대로 뒤집는 함수
- reverse()가 리스트 자체를 직접 변경
- 리스트만 사용 가능
- ```
    print(numbers)
    numbers.reverse() # 정렬이 되어있지 않아도 정렬 할 수 있음 
    print(numbers) # (45445121) > (12154454)
    ```


### 🌀 reversed()
- `reversed(method)`
- 순서가 있는 자료형을 뒤집은 반복자(iterator)**를 반환하는 함수(리스트, 문자열, 튜플 등)
- 문자열도 reversed()로 뒤집어서 . ''.join()을 사용해서 문자열로 다시 합침.
- ```
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = reversed(numbers)

    print(reversed_numbers)  # <list_reverseiterator object at 0x000002504CE8AEF0>
    ```
    - list로 다시 변환하지 않고 출력하면 메모리 주소가 표시 됨

- ```
    def solution(my_string):
    return ''.join((reversed(my_string)))
  ```
  - str을 바로 변환하고 ''.join으로 다시 str로 합침