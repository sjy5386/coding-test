/*
 * 여러 기준으로 정렬하기
 * https://programmers.co.kr/learn/courses/30/lessons/59404
 */

SELECT ANIMAL_ID, NAME, DATETIME
from ANIMAL_INS
order by NAME, DATETIME desc;