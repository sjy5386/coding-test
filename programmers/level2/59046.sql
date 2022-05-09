/*
 * 루시와 엘라 찾기
 * https://programmers.co.kr/learn/courses/30/lessons/59046
 */

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS
where NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty');