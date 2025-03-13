blood_type = ['A', 'B', 'O', 'AB']

# 1. a형이랑 b형이 몇명인지 알고 싶을 때

result = {}

for blood in blood_type:
    if blood in result:
        result[blood] += 1
    else:
        result[blood] = 1


print(result)

# 미세먼지
dust = {
    '서울': 50,
    '인천': 100,
    '수원': 30,
    '부산': 0,
    
}

# 미세먼지  50 미만인 도시 고르기

result = {}
for