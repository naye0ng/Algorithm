# SQL

> 코딩테스트 대비 정리

|   연산자    | 종류 |
| :---------: | :-----------------------------: |
| 비교 연산자 | `=`, `<>`, `<`, `>`, `<=`, `>=`, `IS NULL` |
| 부울 연산자 | `AND`, `OR`, `NOT`            |
| 집합 연산자 | `IN`, `NOT IN`, `ANY`, `SOME`, `ALL`, `EXIST` |
| 집단 함수<br />(GROUP BY와 함께 사용) | `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` |



## 1. SELECT 

`SELECT`는 온라인 코딩테스트에서 가장 많은 부분을 차지한다.

```sql
SELECT 칼럼     -- ⑤ 4번으로 그룹화된 튜플들 중, 특정 칼럼을 가져와서 표기한다.
FROM 테이블     -- ① FROM에 명시된 테이블을 가져와서 합친다.
WHERE 조건      -- ② 1번에서 합친 테이블 중, 조건을 만족하는 것만 남긴다.
GROUP BY 조건   -- ③ 2번 수행 후, 남아있는 값을 조건으로 묶어준다.
HAVING 조건     -- ④ 3번에서 하나의 그룹으로 묶인 튜플들 중, 조건을 만족하는 그룹만 남긴다.
ORDER BY 칼럼1, 칼럼2 DESC;  -- ⑥ SELECT문의 결과를 칼럼1에 대하여 오름차순, 칼럼2에 대하여 내림차순 정렬한다.
```

- WHERE 조건을 SELECT문의 결과로 줄 수 있다. 이럴 경우, `IN`, `EXISTS` 등의 연산자를 활용한다.
- 일반 비교 연산자로는 NULL을 구분할 수 없다. 그러므로 `IS NULL`, `IS NOT NULL` 연산자를 사용해야한다.
- 중복제거 : `DISTINCT`
- 문자열 비교 연산 : `LIKE`
  - `%` : 글자수 상관 없이 뭔가 들어가기만하면 됨
  - `_` : 한글자를 의미함
- 개수 제한 : `LIMIT`
  - 상위 n개의 레코드만 출력하는 문제에서 유용하게 사용됨



### 1) GROUP BY

[입양 시각 구하기(1)](https://programmers.co.kr/learn/courses/30/lessons/59412)

```sql
SELECT HOUR(DATETIME) HOUR2, COUNT(*) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR2	-- 보이는 것처럼 SELECT 문에서 설정한 칼럼 명을 기준으로 그룹을 만드는 것도 가능하다!!
HAVING HOUR2 >= 9 AND HOUR2 < 20
ORDER BY HOUR2;
```



### 2) SET

[입양 시각 구하기(2)](https://programmers.co.kr/learn/courses/30/lessons/59413)

- 로컬 변수 사용하기

```sql
SET @hour := -1;

SELECT 
    (@hour := @hour+1) as HOUR, 
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;
```






## 2. INSERT 

테이블에 튜플을 삽입하는 방법

```
INSERT INTO 릴레이션(애트리뷰트1, ..., 애트리뷰트n)
VALUES (값1, ..., 값n);
```

```
INSERT INTO 릴레이션(애트리뷰트1, ..., 애트리뷰트n)
SELECT 애트리뷰트1, ..., 애트리뷰트n 
FROM 테이블
WHERE 조건;
```



## 3. DELETE

`DELETE`는 테이블 삭제가 아니라 테이블에 삽입된 튜플을 삭제하는 방법

```
DELETE FROM 테이블
WHERE 조건;
```

- 조건이 생략되면 해당 테이블의 모든 데이터가 삭제된다. 그렇다고 테이블이 삭제되는 것은 아니다.



## 4. UPDATE

튜플을 갱신하는 방법

```
UPDATE 테이블
SET 애트리뷰트 = 변경할 값
WHERE 조건;
```







