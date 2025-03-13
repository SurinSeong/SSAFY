# GNS

## 파일에서 입력 tc 읽어오기
- `sys.stdin` 은 키보드 입력과 연결된 데이터 연결 통로
- `open("input.txt")` 내장함수로 파일을 열고 얻은 파일객체로 설정
```python
import sys
sys.stdin = open('input.txt')
# 이후 input()은 키보드 입력이 아닌 open()함수로 연 파일의 내용을 읽어온다.
```

## 문자열의 대소 비교

- 다음 코드의 실행 결과는?
```python
arr = ['TWO', 'SIX', 'TWO', 'FIV', 'FOR', 'SIX']

print('TWO' < 'FOR')
print('TWO' < 'SIX')
```

> #### 문자열 비교 연산 
> - 비교 연산자를 사용해서 두 문자열을 비교하는 경우 사전순에 의해 수식의 값이 결정된다.
> - 사전 순서로 빠른 문자열이 더 작은 값이 된다.   
 
- 숫자 문자열을 숫자로 변환
```python
arr = ['TWO', 'SIX', 'TWO', 'FIV', 'FOR', 'SIX']

# 문자열을 대응하는 숫자로 변환
arr = [2, 6, 2, 5, 4, 6]
```

> 방법 1
```python

```

> 방법 2
```python

```

## 카운팅


## 출력 처리 
