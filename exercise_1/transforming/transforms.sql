DROP TABLE effective_clean_pos;
CREATE TABLE effective_clean_pos
STORED AS PARQUET
AS
select measure_id, measure_name, provider_id, state, CAST(score AS DOUBLE) AS score
from effective_care
where score RLIKE '^[0-9]+(\.[0-9]*)$'
and measure_id != 'ED_1b'
and measure_id != 'ED_2b'
and measure_id != 'OP_1'
and measure_id != 'OP_18b'
and measure_id != 'OP_20'
and measure_id != 'OP_21'
and measure_id != 'OP_3b'
and measure_id != 'OP_5'
and measure_id != 'VTE_6';

DROP TABLE effective_clean_neg;
CREATE TABLE effective_clean_neg
STORED AS PARQUET
AS
select measure_id, measure_name, provider_id, state, CAST(score AS DOUBLE) AS score
from effective_care
where score RLIKE '^[0-9]+(\.[0-9]*)$'
and (measure_id = 'ED_1b'
or measure_id = 'ED_2b'
or measure_id = 'OP_1'
or measure_id = 'OP_18b'
or measure_id = 'OP_20'
or measure_id = 'OP_21'
or measure_id = 'OP_3b'
or measure_id = 'OP_5'
or measure_id = 'VTE_6'
);


DROP TABLE effective_clean_national;
CREATE TABLE effective_clean_national
STORED AS PARQUET
AS
select measure_id, measure_name, CAST(score AS DOUBLE) AS national_score
from effective_care_national
where score RLIKE '^[0-9]+(\.[0-9]*)$';


DROP TABLE readmissions_clean;
CREATE TABLE readmissions_clean
STORED AS PARQUET
AS
select measure_id, measure_name, provider_id, state, CAST(score AS DOUBLE) AS score
from readmissions
where score RLIKE '^[0-9]+(\.[0-9]*)$';



DROP TABLE readmissions_clean_national;
CREATE TABLE readmissions_clean_national
STORED AS PARQUET
AS
select measure_id, measure_name, CAST(national_rate AS DOUBLE) AS national_rate
from readmissions_national
where national_rate RLIKE '^[0-9]+(\.[0-9]*)$';



DROP TABLE total_perf_scores_clean;
CREATE TABLE total_perf_scores_clean
STORED AS PARQUET
AS
select provider_number, hospital_name, state, CAST(total_performance_score AS DOUBLE) AS tot_score
from total_perf_scores;



DROP TABLE hospitals_clean;
CREATE TABLE hospitals_clean
STORED AS PARQUET
AS
select provider_id, hospital_name, state
from hospitals
where provider_id RLIKE '.+';



DROP TABLE survey_responses_clean;
CREATE TABLE survey_responses_clean
STORED AS PARQUET
AS
select provider_number, hospital_name, state, CAST(hcahps_base_score + hcahps_consistency_score AS DOUBLE) AS survey_score
from survey_responses
where hcahps_base_score RLIKE '^[0-9]+(\.[0-9]*)$' 
AND hcahps_consistency_score RLIKE '^[0-9]+(\.[0-9]*)$';

