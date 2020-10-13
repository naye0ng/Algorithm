-- [1] 최대값 구하기
SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS;

-- [2] 최소값 구하기
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS;

-- [3] 동물 수 구하기
SELECT COUNT(*) AS count
FROM ANIMAL_INS;

-- [4] 중복 제거하기
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;