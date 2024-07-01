-- 코드를 입력하세요
SELECT  u.USER_ID, u.NICKNAME, SUM(b.PRICE) AS TOTAL_SALES
FROM    USED_GOODS_BOARD b JOIN USED_GOODS_USER u
WHERE   b.WRITER_ID = u.USER_ID
        AND b.STATUS = 'DONE'
GROUP BY    u.USER_ID
HAVING      TOTAL_SALES >= 700000
ORDER BY    TOTAL_SALES ASC;