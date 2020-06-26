### 문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

### 입출력 예

numbers | return
:-------------------------:|:-------------------------:
"17" | 3
"011" | 2


### 입출력 예 설명

예제 #1

[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2

[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.

---

### Solution code

```python
from itertools import permutations

def isPrime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False


def solution(numbers):
    answer = 0

    possible_per = []
    # every possible permutations
    for i in range(len(numbers)):
        possible_per.extend(list(permutations(numbers, i+1)))

    possible_per = [''.join(i) for i in possible_per]  # joining for converting into number
    possible_per = sorted(list(set(map(int, possible_per))))  # mapping into int

    for item in possible_per:
        if isPrime(item): 
            answer += 1
    
    return answer
```

---

### Notes

- 완전탐색 문제
- 입력받은 숫자 string으로 만들 수 있는 모든 수의 조합 생성
- 각 숫자가 소수인지 판별
- 소수 판별 시, 2부터 루트 값까지 나눗셈 수행하는 동안 나눠지지 않으면 소수