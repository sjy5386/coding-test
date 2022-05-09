/*
 * 이름에 el이 들어가는 동물 찾기
 * https://programmers.co.kr/learn/courses/30/lessons/59047
 */

SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where lower(NAME) like '%el%'
  and ANIMAL_TYPE = 'Dog'
order by NAME;