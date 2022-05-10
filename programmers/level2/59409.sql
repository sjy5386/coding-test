/*
 * 중성화 여부 확인하기
 * https://programmers.co.kr/learn/courses/30/lessons/59409
 */

SELECT ANIMAL_ID,
       NAME,
       case when (SEX_UPON_INTAKE like 'Neutered%' or SEX_UPON_INTAKE like 'Spayed%') then 'O' else 'X' end as 중성화
from ANIMAL_INS;