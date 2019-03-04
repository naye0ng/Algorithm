# Algorithm / Data Structure

효율적인 코드 구현을 위해 알고리즘과 자료구조를 공부하고 이를 기록한 내용입니다.

### Algorithm 

- 문제를 해결하기 위한 것으로, 명확하게 정의되고 순서가 있는 유한 개의 규칙으로 이루어진 집합

### Data Structure

- 자료(Data)의 집합의 의미하며, 각 원소들이 논리적으로 정의된 규칙에 의해 나열되며 자료에 대한 처리를 효율적으로 수행할 수 있도록 자료를 구분하여 표현한 것

<br />

## 1. 배열

### 1-1. 소수

[누적 소수의 배열] 

>- 2부터 차례로 소수를 배열에 누적시키기
>
>- 누적이 필요한 이유? 소수는 자기보다 작은 소수들로도 나눠 떨어지지 않는다.
>
>  *code: /Study-Algorithm/decimal.py*

[에라토스테내스의 체 ]

>- 소수가 아닌 값에 마킹하기
>- 그러나 이 방법은 배열의 크기가 커질수록 최악이 되므로 이미 체크된 값은 체크하지 않도록 하는 것이 중요하다.
> *code: /Study-Algorithm/decimal2.py*

<br />

## 2. 검색

### 2-1. 선형검색

- 무작위로 늘어놓은 데이터의 모임에서 순차적으로 검색을 수행, 가장 일반적으로 생각할 수 있는 검색

- 시간복잡도 : O(n)
- 선형검색의 종료 조건은 다음 두가지 이다.

> 1. 검색할 값과 같은 값을 발견한 경우
> 2. 검색할 값을 발견하지 못하고 배열의 끝을 지나간 경우

​	*code: /Study-Algorithm/seqSearch.py*

[보초법] 

> - 선형검색 과정에서 불필요한 판별식을 줄이기 위해 사용하는 방법
> - 보초법은 2번을 없애기 위해 검색할 값을 배열의 맨 뒤에 추가하는 방법으로, 이 경우 종료조건은 1번 한가지 뿐이다. 결과적으로 판별식이 반으로 줄어들게 된다.

<br />

### 2-2. 이진검색

- 일정한 규칙으로 늘어놓은 데이터의 모임에서 아주 빠른 검색

- 시간복잡도 : O(logn)

- 전제 조건 : 데이터값이 정렬(sort)된 상태에만 가능

- 중간 값과 검색할 값을 비교하면서 범위를 좁혀나가는 검색 방법

  *code: /Study-Algorithm/seqSearch.py*

[이진검색시 주의할 점]

> - 중복된 값이 존재하는 정렬된 배열에서 검색하는 경우, 이진검색만으로는 중복된 값 모두를 발견하기 어렵다.
> - 검색할 값이 배열에 2개 이상이상 저장되어 있다면, 앞 뒤로 같은 값을 검색하는 로직을 추가해야 한다.

<br />

### 2-3. 해시법 

- 추가, 삭제가 자주일어나는 데이터의 모임에서 아주 빠른 검색

- 체인법 : 같은 해시 값의 데이터를 선형리스트로 연결하는 방법
- 오픈 주소법 : 데이터를 위한 해시 값이 충돌할 때 재해시하는 밥법





## 추가

## A. 백트래킹

### A-1. 백트래킹과 깊이우선탐색(DFS)의 차이

> - 기본적인 로직은 비슷
> - DFS는 비선형 자료구조의 모든 로직을 빠짐없이 탐색할 수 있는 형태이다. 즉, 지수승의 시간복잡도를 가진다.
> - 백트래킹의 경우 가지치기(Prunning)를 통해, 해결책으로 이어질 것 같지 않으면 더이상 그 경로를 따라가지 않음으로써 시도 횟수를 줄인다.
> - 물론 백트래킹 또한 최악의 경우에는 지수승의 복잡도를 가진다.
> - 굳이 가지치기가 없더라도 재귀적인 경우를 백트래킹이라 하기도함. 그래프에서를 DFS라고 생각하면 된다. 

<br />

### A-2. 백트래킹을 이용한 순열 구하기

>- {1,2,3}의 부분집합을 구한다고 한다면, 최초의 순열을 추출하고 다음 단계에서 추출되지 않은 값을 추출하여 순열을 만든다고 보면 된다. 
>- 자신을 선택하고 이후 남은 후보의 수만큼 자식노드를 생성해서 백트래킹을 하겠다는 것으로 이해하면됨
>-  ex) {1,(다음 후보는 2,3)},{2,(후보1,3)},{3,(후보1,2)}

<br />

### A-3. 백트래킹으로 부분집합 구하기

> **[문제] {1,2,3,4,5,6,7,8,9,10}의 powerset중 원소의 합이 10인 부분집합을 구하시오.**
>
> *code: /Study-Algorithm/BackTracking-Powerset.py*
>
> ```python
> def backtrack(a,k,end) :
>     # for문을 돌면서 부분집합의 포함(True), 불포함(False)을 나타냄
>     c = [True, False]
>     
>     if k == end :
>         # 마지막 노드까지 도착한 경우, 원하는 연산 수행
>     else :
>         k+=1
>         for i in range(len(c)) :
>             a[k] = c[i]
>             backtrack(a,k,end)
>           
> # 0(공집합)~10까지 이므로 총 배열의 크기는 10+1=11이 된다.        
> a = [0]*11 
> backtrack(a,0,10)
> ```
>
> 그러나 위의 경우의 경우, 연산을 약 2^10번 수행하게 된다. 집합의 크기가 커질 수록 연산의 횟수가 2^N으로 증가하게 된다.
>
> **[최적화]**
>
> 2,3,5가 선택된 경우, 이미 합이 10이 되었으므로 나머지 6이후의 부분집합을 구하는 연산을 수행하지 않도록 하자
>
> ```python
> def backtrack(a,k,sum) :
>     c = [True, False]
>     
>     # 마지막 노드까지 도착한 경우 중 합이 10인 경우만 출력하자!
>     if k == 10 :
>         if sum == 10 :
>             for i in range(1, 11) :
>                 if a[i] == 1 :
>                     print(i, end=' ')
>             print()
>     else :
>         k+=1
>         if sum + k <= 10 :
>             # 합이 10이하 일때만 본인을 선택한다.
>             a[k] = 1
>             backtrack(a,k,sum+k)
>         a[k] = 0; backtrack(a,k,sum)
> ```



## B. 분할정복

- O(log2n)
- 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복 : 나눈 작은 문제를 각각 해결한다.
- 통합 : 필요하다면, 해결된 해답을 모은다.

<br />

### B-1. 분할정복 

> **[문제] 거듭제곱**
>
> C^2 = CxC
>
> C^3 = CxCxC
>
> ...
>
> C^n = CxCx...xC
>
> 거듭제곱의 경우 중복 연산이 많다. 분할정복을 사용하여 중복을 최소화 할 수 있다.
>
> ```
> C^n = C^n/2 x C^n/2 , n은 짝수, 
> C^n = C^(n-1)/2 x C^(n-1)/2 x C , n은 홀수
> ```

<br />

## C. 퀵정렬

- 주어진 배열을 두개로 분할하고, 각각을 정렬한다.
- 시간복잡도 O(nlogn)
- 최악의 경우, O(n^2)이지만 평균적으로 가장 빠르다.

<br />

### C-1. 퀵정렬 방법

1. pivot을 잡고 왼쪽 끝에서부터는 pivot보다 큰거나 같은 값(L)을, 오른쪽 끝에서는 pivot보다 작은 값(R)을 찾는다.
2. L != R이면서 L과 R이 결정되면 L과 R의 자리를 바꾼다. 다시 이후부터 L, R을 움직인다.
3. L == R이면 pivot과 자리를 바꾼다.
4. pivot이었던 값들은 놔둔채 나머지 부분집합에서 퀵정렬을 계속해서 수행한다.

```python
def quickSort(a, begin, end) :
    if begin < end :
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
        
def partition(a, begin, end):
    pivot = (begin+end)//2
    L = begin
    R = end
    while L < R :
        # a[L]이 a[pivot]보다 크거나 같아야 하므로 작은 a[L]경우, 오른쪽으로 한칸 이동
        # L < R을 항상 주는 이유는 L==R(pivot교환)는 가능하지만 R<L는 안됨
        while(a[L]<a[pivot] and L<R) : L += 1
        while(a[R]>=a[pivot] and L<R) : R -= 1
        # L < R 인 상황에서 멈췄을때
        if L < R :
            # L==pivot인 경우는 원소가 두개 있는 경우 중에 역순으로 정렬된 경우만 나옴
            # 예를 들면, {10, 8}
            if L==pivot : 
                pivot = R
            # L과 R의 자리교환, 
            a[L], a[R] = a[R], a[L]
            
            
    # pivot의 왼쪽에서 R=L인 경우, pivot과 자리교환
    a[pivot], a[R] = a[R], a[pivot]
    # R에는 pivot이 바꾼 위치가 그대로 들어가 있음
    return R
```

<br />

### C-2. 퀵정렬과 합병정렬의 차이점

> - 합병정렬은 두 부분으로 그냥 나눔, 퀴정렬은 분할시 아이템을 중심으로 작은 것은 왼편, 큰 것은 오른편에 위치한다.
> - 각 부분의 정렬이 끝난 후, 합병정렬은 '합병'의 과정이 필요하지만 퀵정렬은 추가 작업이 없다.



## D. 큐(Queue)

- FIFO 구조

<br />

### D-1. 선형 큐

*code: /Study-Algorithm/Queue.py*

<br />

#### 상태표현

- front : 저장된 첫번째 원소의 인덱스
- rear : 저장된 마지막 원소의 인덱스
- 초기 상태 : front = rear = -1
- 공백 상태 : front =rear
- 포화 상태 : rear = n-1(n은 배열의 크기, n-1은 배열의 마지막 인덱스)

<br />

#### 구현

| 연산          | 기능                                   |
| ------------- | -------------------------------------- |
| enQueue()     | 큐의 뒷쪽에 원소를 삽입하는 기능       |
| deQueue()     | 큐의 앞쪽에서 원소를 삭제하고 반환     |
| createQueue() | 공백 상태의 큐를 생성                  |
| isEmpty()     | 큐가 공백인지를 확인                   |
| isFull()      | 큐과 포화상태인지를 확인               |
| Qpeek()       | 큐의 앞쪽에서 원소 삭제 없이 값을 반환 |

*주의 할 점:  front 값이 0이 아니라 저장된 첫번째 원소를 가리키도록 계속해서 변한다는 점*

```python
class Queue :
    def __init__(self, n) :
        self.n = n
        self.front = -1
        self.rear = -1 
        self.queue = [None]*self.n
    
    def inQueue(self, value) :
        if self.isFull() :
             print("Full")
        self.rear += 1
        self.queue[self.rear] = value

    def deQueue(self) :
        if self.isEmpty() :
             return None
        self.front += 1
        value = self.queue[self.front]
        self.queue[self.front] = None
        return value

    def isEmpty(self) :
        return self.front == self.rear
    
    def isFull(self) :
        return self.rear == self.n-1 
    
    def Qpeek(self) :
        if self.isEmpty() :
             return None
        return self.queue[self.front+1]
```

<br />

>#### 선형 큐의 문제점
>
>선형 큐를 이용해 원소를 삽입 삭제를 하게 되면 배열의 앞에 공간이 남아 있음에도 잘못된 포화 상태를 인식하게 되어 near=n-1인 상태에선 더 이상의 삽입을 허용하지 않는다.
>
>이를 해결하기 위해 선형 큐에 원소를 삽입할 때마다 배열을 앞쪽으로 당기게 되면 효율성이 떨어진다. 원형 큐를 사용하자.

<br />

### D-2. 원형 큐(Round Queue)

*code: /Study-Algorithm/RoundQueue.py*

#### index의 순환

- front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 논리적인 순환을 이루어 배열의 처음 인덱스인 0을 가리키도록 하자. 

- **mod연산**을 활용

  - front 변수 : 공백상태와 포화상태 구분을 쉽게 하기 위해 front의 자리는 항상 빈자리

    |        | 삽입 위치               | 삭제 위치                 |
    | ------ | ----------------------- | ------------------------- |
    | 선형큐 | rear = rear +1          | front = front + 1         |
    | 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |

```python
class RoundQueue :
    def __init__(self, n) :
        self.n = n
        self.front = 0
        self.rear = 0 
        self.queue = [None]*self.n
    
    def inQueue(self, value) :
        if self.isFull() :
            print("Full")
        self.rear = (self.rear+1)%self.n
        self.queue[self.rear] = value

    def deQueue(self) :
        if self.isEmpty() :
             return None
        self.front = (self.front+1)%self.n
        value = self.queue[self.front]
        self.queue[self.front] = None
        return value

    def isEmpty(self) :
        return self.front == self.rear
    
    def isFull(self) :
        # 원형 큐의 경우 원형을 돌아왔는데 값이 front랑 같다면 full이라고 볼 수 있다.
        return (self.rear+1)%self.n == self.front
    
    def Qpeek(self) :
        if self.isEmpty() :
             return None
        return self.queue[self.front+1]

```

- **원형 큐의 크기가 n이라면 원형 큐에 넣을 수 있는 값의 수는 n-1개이다.** 
- 만약 n개를 다 채울경우, front와 rear의 값이 같아져서 시작이 어디인지 문제가 발생하게 된다.

<br />

### D-3. 연결 큐(Linked Queue)

연결 큐의 경우 하나의 노드가 다음 노드를 가리키도록 만들어 줘야한다. 원형큐나 선형큐와는 다르게 하나의 노드에 노드의 값과 다음 원소의 주소값 총 2가지 데이터를 가지게 된다.

*code: /Study-Algorithm/LinkedQueue.py*

<br />

#### 상태표현

- front : 첫번째 노드를 가리키는 링크
- rear : 마지막 노드를 가리키는 링크
- 초기 상태 : front = rear = null
- 공백 상태 : front = rear = null

<br />

#### 구현

**(1). enQueue**

- 첫 노드가 생성(비어 있다면)되면 front와 rear는 해당노드를 가리킨다.
- 첫 노드가 아닌 노드가 생성되면 기존의 rear가 가리키고 있던 마지막 노드는 새로 생성된 노드를 가리킨다.
- rear는 새로 들어온 마지막 노드를 가리킨다.

<br />

**(2). deQueue**

- front가 가리키고 있던 값(첫번째 노드)을 다음 노드로 변경, 즉 현재 front가 가리키고 있던 노드가 가리키고 있는 노드를 front가 가리키도록
- 그런데 front가 가리키는 값이 마지막 하나 남은 노드였다면( 즉, deQueue)연산을 수행하면 빈 큐가 될 경우 rear값을 null로 변경해준다.
- (선택) front가 가리키고 있었던 노드의 다음노드를 null로 변경하여 고립

<br />

```python
class Node :
    def __init__(self, item, n=None) :
        self.item = item
        self.next = n

class LinkedQueue :
    def __init__(self) :
        # front랑 rear모두 Node가 될것임
        self.front = None
        self.rear = None

    def enQueue(self, item) :
        # 새로운 노드 생성
        newNode = Node(item)
        # 처음으로 생성된 노드이면 front는 새로 생성된 노드를 가리킴
        if self.front == None :
            self.front = newNode
        else :
            # 현재의 마지막 노드에 다음 노드 할당
            self.rear.next = newNode
        # 마지막 노드 가리키도록 rear값 변경
        self.rear = newNode

    def deQueue(self) :
        if self.isEmpty() :
            return None
        
        item = self.front.item
        self.front = self.front.next

        # 그런데 만약 마지막 노드라면 마지막 노드를 가리키는 rear 변경
        if self.front == None :
            self.rear = None

        return item

    def isEmpty(self) :
        return self.front == None

    def Qpeek(self) :
        return self.front.item

    def printQ(self) :
        f = self.front
        s = ""
        while f :
            s += str(f.item)+" "
            f = f.next
        return s
```

<br />

### D-4. 우선 순위 큐

- 우선 순위를 가진 항목들을 저장하는 큐
- FIFO가 아니라 우선순위가 높은 순서대로 먼저 나간다.
- 값이 큐에 삽입될때 우선순위를 비교하여 우선순위가 높은 노드를 앞쪽으로 배치한다.

<br />

**문제점**

- 삽입 삭제 연산이 발생하면 원소의 재배치가 일어나는데 이는 시간이나 메모리 닝비가 크다.

<br />

**적용분야**

- 시뮬레이션 시스템
- 네트워크 트래픽 제어
- 운영체제의 테스크 스케줄링

<br />

>**버퍼**
>
>- 시스템이 사용하는 큐라고 볼 수 있다.
>- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다.
>- 순서대로 입/출력이 되어야 하므로 FIFO방식의 큐가 활용된다.

<br />

### D-5. BFS : 너비 우선 탐색

DFS와 다르게 같은 레벨의 노드부터 탐색을 수행한다. 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 한다.

선입선출 형태의 큐를 활용한다.(DFS는 스택을 사용)

<br />

#### 구현

- 큐에 같은 레벨의 노드를 넣어 놓고 deQueue할 때마다 해당 노드에 연결된 하위 노드를 큐에 넣는 방식으로 구현

```python
def BFS(G, v) :
    global n
    # 방문 확인
    visitied = { i:0 for i in range(1,n+1)}

    queue = []
    # 정점 v부터 탐색 시작
    queue.append(v)

    while queue :
        t= queue.pop(0)
        if not visitied[t] :
            visitied[t] = True
            
            # 원하는 연산 
            print("방문 완료",t)
            visit(t)
        
        for i in G[t-1] :
            if not visitied[i] :
                queue.append(i)

n = 9
G = [[2,3,4],[5,6],[8],[7,8,9],[],[],[],[],[]]
BFS(G, 1)
```



## E. 리스트

- 자료구조에서의 리스트는 순서를 가진 데이터의 집합을 가리키는 추상자료형을 말한다.
- 동일한 데이터를 가지고 있어도 상관없다.

<br>

#### 리스트의 종류

- 순차 리스트 : 배열을 기반으로 구현
- 연결 리스트 : 메모리의 동적할당을 기반으로 구현 (물리적인 주소가 연속적이지 않아도 됨)

<br>

#### 함수구현

| 함수명       | 기능                                  |
| ------------ | ------------------------------------- |
| addtoFirst() | 리스트의 앞쪽에 원소를 추가           |
| addtoLast()  | 리스트의 뒤쪽에 원소를 추가           |
| add()        | 리스트의 특정 위치에 원소를 추가      |
| delete()     | 리스트의 특정 위치에 있는 원소를 삭제 |
| get()        | 리스트의 특정 위치에 있는 원소를 리턴 |

<br>

### E-1. 순차 리스트

- 배열을 기반으로 생성된다. 즉, 메모리 공간에 물리적으로 연속된 리스트
- 배열이므로 인덱스 기반으로 원소에 접근이 가능하며 빠르다.
- 그러나, 삽입/삭제 연산이 빈번한 상황에서 사용하기 부적절하다.

<br>

>  #### 순차리스트의 문제점
>
> - 단순배열을 이용해 순차리스트를 구현하는 경우, 자료의 삽입/삭제 연산과정에서  연속적인 메모리 배열을 위해 원소들을 이동시키는 작업이 필요하다.
> - 즉, 원소의 갯수가 크고 삽입/삭제가 빈번한 작업의 경우 소요시간이 크게 증가하게 된다. 
> - 배열의 크기가 정해져 있는 경우, 리스트의 크기가 커지거나 실제 리스트에서 처리되는 연산이 작다면 메모리 공간이 낭비된다.

<br>

### E-2. 단순 연결 리스트(Linked List)

- 자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고, 개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룬다.
- 링크를 통해 원소에 접근하므로, 순차리스트처럼 물리적인 순서를 맞추기 위한 작업이 필요하지 않다.
- 자료구조의 크기를 동적으로 조정이 가능하므로, 메모리의 효율적인 사용이 가능

<br>

#### 연결리스트의 기본 구조

- 노드
  - 데이터 필드 : 원소의 값을 저장
  - 링크 필드 : 다음 노드의 주소를 저장 
- 헤드 
  - 리스트의 처음 노드를 가리킴
- 연결 구조 
  - 노드의 링크 필드에 의해 다음 노드와 연결되는 구조를 가진다.
  - 헤드는 가장 앞의 노드를 가리키며, 링크 필드가 연속적으로 다음 노드를 가리킨다.
  - 최종적으로 NULL을 가리키는 노드가 리스트의 가장 마지막 노드이다.

<br>

#### 구현	

*code: /Study-Algorithm/LinkedList.py*

```python
class Node :
    def __init__(self,data,link=None) :
        self.data = data 
        self.link = link

class LinkedList :
    def __init__(self) :
        self.head = None
    
    def addtoFirst(self, data) :
        """
        head가 가지고 있는 값 자체가 다음 노드이므로 
        self.head.link가 아니라 self.head가 되어야 한다.
        """
        self.head = Node(data, self.head)

    def add(self, pre, data) :
        if pre == None :
            print("error")
        else :
            pre.link = Node(data,pre.link)
    
    def addtoLast(self, data) :
        if self.head == None :
            self.head = Node(data,None)
        else :
            p = self.head
            # 마지막 노드 찾기
            while p.link != None :
                p = p.link
            
            p.link = Node(data,None)

    # pre의 다음 노드를 삭제
    def delete(self, pre) :
        if pre == None or pre.link == None :
            print('error')
        else :
            pre.link = pre.link.link
    
    def get(self, index) :
        if self.head == None :
            return None
        # 1번째는 head
        p = self.head 

        for _ in range(index-1) :
            # 연결리스트의 크기가 index보다 작은 경우
            if p.link == None :
                return None
            p = p.link
        return p

    def printList(self) :
        if self.head == None :
            print("empty")
        else :
            p = self.head 
            while p.link != None :
                print(p.data, end=' | ')
                p = p.link
            print(p.data)
```

<br>

*<b>항상 순차 리스트보다 연결 리스트가 좋은 것은 아니다.</b> 자료의 크기가 정해져 있고, 삽입/삭제 연산이 빈번하지 않고 조회가 많은 연산에서는 순차 리스트의 사용이 적절하다.*

<br>

### E-3. 이중 연결 리스트(Doubly Linked List)

#### 구현

```python
class Node :
    def __init__(self,data,pre=None,next=None) :
        self.data = data
        self.pre = pre
        self.next= next

class DoubleLinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        
	# 맨 뒤에 원소 삽입
    def addLast(self,data) :
        if self.head == None :
            self.head = Node(data)
            self.tail = self.head
        else :
            self.tail.next = Node(data,self.tail)
            self.tail = self.tail.next
```



#### 관련 문제

*code: /Study-Algorithm/5110.py*

*code: /Study-Algorithm/5120.py*



## F. 트리

- 비선형 구조
- 원소들 간에  1:n 관게를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 개념적으로는 재귀, 트리의 n개의 자식도 트리구조를 가진다. 
  - 부트리 : 트리의 자식, 트리구조를 가짐
  - 단말노드 : 자식이 없는 노드
  - 형제 노드 : 같은 무모를 갖는 자식 노드 들
- 차수 
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중 가장 큰 값
  - 단말 노드 : 차수가 0인 노드, 자식이 없는 노드
- 높이 
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 최대 레벨
  - 

### F-1. 이진트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대 2개 까지만 가질 수 있는 트리



#### 특성

- 레벨 i에서의 노드의 최대 개수는 2^i
- 높이가 h인 이진트리가 가질 수 있는 노드의 최소 갯수는 h+1이며, 최대 갯수는 2^(h+1)-1



#### 종류

#### (1). 포화 이진 트리(Full Binary Tree)

- 모든 레벨에서 노드가 포화 상태로 차 있는 트리
- 높이가 h일때 최대 노드 개수인 2^(h+1)-1의 노드를 가지는 트리



#### (2). 완전 이진 트리(Complete Binary Tree)

- 높이가 h이고 노드 수가 n일때, 포화 이진 트리의 노드 번호 1번부터 n번까지 빈자리가 없는 이진 트리



#### (3). 편향 이진 트리

- 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진트리
- 구현이 어려워서 잘 나오지 않음



### F-2. 순회(traversal)

- 순회란 트리의 각 노드를 중복되지 않게 전부 방문하는 것을 말한다.  트리는 비 선형 구조이기 때문에 선형구조에와 같이 선 후 연결 관계를 알 수 없다.

> ​	   A
> ​	 /     \
> ​    B		    C
>  /    \	   /    \
> D	E	F	G
>	​      /    \
> ​     H    I 

#### (1). 전회 순위(preorder traversal) : 

- 루트 - 왼쪽 -오른쪽
- A B D E H I C F G

```python
def preorder_traverse(T) :
    if T :
        print(T)
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])
        
# T는 index를 노드번호로 가지고 [left,right]형태의 2차원 배열
```

*code: /Study-Algorithm/PreorderTraverse.py*



#### (2).중위순위(inorder traversal) : 

- 왼쪽 - 루트 - 오른쪽
- D B H E I A F C G

```python
def inorder_traverse(T) :
    if T :
        preorder_traverse(tree[T][0])
        print(T)
        preorder_traverse(tree[T][1])
```



#### (3). 후위순위(postorder traversal) : 

- 왼쪽 - 오른쪽 - 루트
- D H I E B F G C A

```python
def postorder_traverse(T) :
    if T :
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])
        print(T)
```



### F-3.  이진트리의 표현

#### (1). 배열

- 노드번호를 배열의 인덱스로 사용
- 놀이가 h인 이진트리를 위한 배열의 크기는? 2^(h+1) -1

##### 단점

- 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 낭비가 발생
- 트리 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기의 변경이 어려워 비효율적이다.



#### (2). 연결리스트

- 배열의 단점을 보완



### F-4. 이진탐색트리

- 탐색작업을 효율적으로 하기 위한 자료구조
- **모든 원소는 서로 다른 유일한 키를 갖는다.**
- key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 왼쪽 서브트리와 오른쪽 서브트리도 이진탐색 트리이다.
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.
- 탐색 연산 횟숫를 줄일 수 있다. 1차원 배열을 사용하는 경우에 비해 높은 성능을 가진다.
- 탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다.
- O(h), h: BST의 깊이(height)
- 평균 O(log n), 최악 O(n)
- 최악을 없애기 위해서 해쉬를 생각해 볼 수 있다.



#### (1). 탐색연산

- 루트에서 시작
- 탐색할 키 값(x)과 루트 노드의 키값을 비교한다.
  - root = x : 원하는 값을 찾음
  - root > x : 왼쪽 서브트리 탐색
  - root < x : 오른쪽 서브트리 탐색
- 서브 트리에 대해서 순차적으로 탐색 연산을 반복한다.



#### (2). 삽입연산

- 탐색 연산부터 시작

  - 이미 존재하는 값이라면 트리에 삽입 할 수 없다.

  - **탐색 실패가 결정되는 위치가 원소 삽입 위치가 된다.**



#### (3). 삭제연산

- 삭제 연산의 경우, 왼쪽과 오른쪽의 서브노드의 값을 생각해서 루트를 재배치 해줘야 한다.



## G. 힙(heap)

완전 이진트리에 있는 노드 중에서 키 값이 가장 큰 노드나 가장 작은 노드를 찾기 적합한 자료구조이다. 최대 값과 최소값을 결과적으로 트리의 루트에 오도록 배열하여 루트값으로 빠르게 최대값, 최소값에 접속이 가능하다.

- 최대 힙
  - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키값 > 자식 노드의 키값
  - 루트 노드 : 키값이 가장 큰 노드
- 최소 힙
  - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키값 < 자식 노드의 키값
  - 루트 노드 : 키값이 가장 작은 노드



#### (1). 삽입연산

- 일단 완전 이진트리의 빈 자리에 삽입할 값을 넣는다.
- 삽입된 위치의 값과 부모의 키값을 비교하여 삽입된 값의 키값이 크다면 부모의 키값과 변경하는 작업을 반복적으로 수행하여 최종적인 자리를 찾도록 한다.



#### (2). 삭제연산

- 힙에서는 루트 노드의 원소만 삭제가 가능하다.

- 루트 노드 삭제를 먼저 실행한다.

- 완전이진트리의 맨 끝 노드를 삭제하여 루트로 올리고

- 루트로 올라오게된 노드와 서브 노드의 루트와 비교하여 제일 큰 값으로 바꿔주는 것을 반복한다.
