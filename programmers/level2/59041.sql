/*
 * 동명 동물 수 찾기
 * https://programmers.co.kr/learn/courses/30/lessons/59041
 */

SELECT NAME, count(*) as COUNT
from ANIMAL_INS
where NAME is not null
group by NAME
having count(NAME) >= 2
order by NAME;