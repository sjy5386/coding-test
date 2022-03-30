/*
 * 이름이 있는 동물의 아이디
 * https://programmers.co.kr/learn/courses/30/lessons/59407
 */

SELECT ANIMAL_ID
from ANIMAL_INS
where NAME is not null
order by ANIMAL_ID;