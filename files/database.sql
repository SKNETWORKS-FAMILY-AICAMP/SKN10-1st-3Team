-- 데이터베이스 목록을 확인
show databases;

-- car_data_analysis 데이터베이스 사용
use miniproject;

-- 테이블 목록을 확인
show tables;

-- vehicle_registration_data 테이블의 모든 데이터를 조회
select * from vehicle_registration_data2;

desc vehicle_registration_data2;

-- formatted_date 컬럼을 DATE 타입으로 추가
ALTER TABLE vehicle_registration_data2 ADD COLUMN formatted_date DATE;

-- date 데이터를 DATE 형식으로 변환하여 formatted_date 컬럼에 저장
UPDATE 
    vehicle_registration_data2
SET formatted_date = STR_TO_DATE(CONCAT('01-', date), '%d-%y-%b');

-- year 컬럼을 INT 타입으로 추가
ALTER TABLE vehicle_registration_data2 ADD COLUMN year INT;

-- formatted_date 컬럼에서 연도를 추출하여 year 컬럼에 저장
UPDATE vehicle_registration_data2
SET year = YEAR(formatted_date);

-- formatted_date와 year 컬럼 데이터를 조회
SELECT formatted_date, year FROM vehicle_registration_data2;

-- 쉼표 제거: official, personal, commercial, total, year 컬럼의 값에서 쉼표(,)를 제거
UPDATE 
    vehicle_registration_data2
SET 
    official = REPLACE(official, ',', ''),
    personal = REPLACE(personal, ',', ''),
    commercial = REPLACE(commercial, ',', ''),
    total = REPLACE(total, ',', ''),
    year = REPLACE(year, ',', '')
;

-- 데이터 타입 변경: official, personal, commercial, total 컬럼을 INT 타입으로 변환
ALTER TABLE 
    vehicle_registration_data2
MODIFY COLUMN 
    official INT,
MODIFY COLUMN 
    personal INT,
MODIFY COLUMN 
    commercial INT,
MODIFY COLUMN 
    total INT,
MODIFY COLUMN
    year INT
;


-- 연도별 12월의 자동차 등록 현황 합계 조회
SELECT 
    YEAR(formatted_date) AS year, 
    SUM(total) AS total_registered_vehicles
FROM 
    vehicle_registration_data2
WHERE 
    MONTH(formatted_date) = 12
    AND district = '계' -- 총계 행만 필터링
GROUP BY 
    YEAR(formatted_date)
ORDER BY 
    YEAR(formatted_date)
;