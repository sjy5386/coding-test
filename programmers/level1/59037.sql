/*
 * 어린 동물 찾기
 * https://programmers.co.kr/learn/courses/30/lessons/59037
 */

SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where INTAKE_CONDITION != 'Aged';