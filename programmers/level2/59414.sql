/*
 * DATETIME에서 DATE로 형 변환
 * https://programmers.co.kr/learn/courses/30/lessons/59414
 */

SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') as 날짜
from ANIMAL_INS;