DROP TABLE effective_clean;
CREATE TABLE effective_clean
STORED AS PARQUET
AS
select measure_id, measure_name, provider_id, state, CAST(score AS DOUBLE) AS score
from effective_care
where score RLIKE '^[0-9]+(\.[0-9]*)$' 
and measure_id != 'ED_1b'
and measure_id != 'ED_2b'
and measure_id != 'AMI_7a'
and measure_id != 'OP_1'
and measure_id != 'OP_18b'
and measure_id != 'OP_2'
and measure_id != 'OP_20'
and measure_id != 'OP_21'
and measure_id != 'OP_22'
and measure_id != 'OP_23'
and measure_id != 'OP_3b'
and measure_id != 'OP_5'
and measure_id != 'OP_6';



DROP TABLE readmissions_clean;
CREATE TABLE readmissions_clean
STORED AS PARQUET
AS
select measure_id, measure_name, provider_id, state, CAST(score AS DOUBLE) AS score
from readmissions
where score RLIKE '^[0-9]+(\.[0-9]*)$';


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
select provider_number, hospital_name, state, CAST(hcahps_base_score/100 + hcahps_consistency_score/100 AS DOUBLE) AS survey_score
from survey_responses
where hcahps_base_score RLIKE '^[0-9]+(\.[0-9]*)$' 
AND hcahps_consistency_score RLIKE '^[0-9]+(\.[0-9]*)$';

