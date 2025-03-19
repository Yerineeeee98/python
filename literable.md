# 반복(iterable) 가능한 자료형
- Iterable은 for문에서 하나씩 꺼내 쓸 수 있는 자료형
![사진](../python/1.png)

# mutable (변경 가능한) 자료형
- 객체를 생성한 후에도 내부의 데이터나 상태를 변경할 수 있음
1. list
 - `.append(x)`: 리스트의 끝에 요소 x를 추가.
 - `.extend(iterable)`: 다른 iterable의 모든 요소를 리스트에 추가.
 - `.insert(i, x)`: 인덱스 i에 요소 x를 삽입.
 - `.remove(x)`: 리스트에서 첫 번째로 등장하는 x를 삭제.
 - `.pop([i])`: 인덱스 i의 요소를 제거하고 반환 (인덱스가 없으면 마지막 요소 제거).
 - `.clear()`: 리스트의 모든 요소를 제거.
 - `.index(x)`: x의 인덱스를 반환.
 - `.count(x)`: x가 리스트에 몇 번 나타나는지 셈.
 - `.sort()`: 리스트를 정렬.
 - `.reverse()`: 리스트의 요소 순서를 뒤집음.
 - `.copy()`: 리스트의 얕은 복사본 생성.
 - `.join('')` : ''을 기준으로 각 단어를 연결함

2. dict
 - `.keys()`: 키들의 iterable 반환.
 - `.values()`: 값들의 iterable 반환.
 - `.items()`: (키, 값) 튜플의 iterable 반환.
 - `.get(key, default)`: key의 값을 반환 (없으면 default 값 반환).
 - `.pop(key, default)`: key를 제거하고 해당 값을 반환.
 - `.update(dict_or_iterable)`: 딕셔너리를 업데이트.
 - `.clear()`: 모든 항목 제거.

3. set {}
 - 집합의 특성
 - 순서가 없음
 - `.add()` 단일 데이터 추가
 - `.update({,})` 여러개의 데이터 추가
 - `.remove()` 데이터 지우기
 - `.pop()` 데이터 하나 랜덤으로 지우기

# immutable (변경 불가능한) 자료형
 - 객체가 생성된 후에는 내부의 데이터를 변경할 수 없음. 변경하려면 새 객체를 만들어야 함.
 1. 정수, 실수, 복소수
 2. str
 3. 튜플
 