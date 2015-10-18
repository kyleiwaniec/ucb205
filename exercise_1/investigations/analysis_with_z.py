#execfile('/data/w205/ucb205/exercise_1/investigations/analysis_with_z.py')

from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.window import Window

####################################################################################################################################
# Data and shenanigans
####################################################################################################################################

effective = sqlContext.sql("SELECT * FROM  effective_clean")
effective_national = sqlContext.sql("SELECT * FROM  effective_clean_national")
readmissions = sqlContext.sql("SELECT * FROM  readmissions_clean")
readmissions_national = sqlContext.sql("SELECT * FROM  readmissions_clean_national")
hospitals = sqlContext.sql("SELECT * FROM hospitals_clean")
surveys = sqlContext.sql("SELECT * FROM survey_responses_clean")

#readmissions.select("measure_id").distinct().count() # 14
#readmissions_national.select("measure_id").distinct().count() #14

readmissions_stddev = sqlContext.sql("SELECT measure_id, stddev(score) AS stddev FROM readmissions_clean GROUP BY measure_id")
effective_stddev = sqlContext.sql("SELECT measure_id, stddev(score) AS stddev FROM effective_clean GROUP BY measure_id")

readmissions_national_w_std = readmissions_national.join(readmissions_stddev, readmissions_national.measure_id == readmissions_stddev.measure_id, "inner").select(readmissions_national.measure_id, readmissions_national.measure_name, readmissions_national.national_rate, readmissions_stddev.stddev)
readmissions_national_w_std.registerTempTable('readmissions_national_w_std_tbl')

# scores get flipped becuase bigger is worse.
readmissions_normalized = sqlContext.sql("SELECT *, (-(rc.score-r.national_rate)/r.stddev) as zscore FROM readmissions_clean rc INNER JOIN readmissions_national_w_std_tbl r ON r.measure_id = rc.measure_id GROUP BY r.measure_id, rc.measure_id,r.measure_name, rc.measure_name, rc.provider_id, rc.state, rc.score, r.national_rate, r.stddev  ORDER BY zscore DESC")

effective_national_w_std = effective_national.join(effective_stddev, effective_national.measure_id == effective_stddev.measure_id, "inner").select(effective_national.measure_id, effective_national.measure_name, effective_national.national_score, effective_stddev.stddev)
effective_national_w_std.registerTempTable('effective_national_w_std_tbl')

effective_normalized = sqlContext.sql("SELECT rc.measure_id, r.measure_name, rc.provider_id, rc.state, rc.score, r.national_score, r.stddev, (rc.score-r.national_score)/r.stddev as zscore FROM effective_clean rc INNER JOIN effective_national_w_std_tbl r ON r.measure_id = rc.measure_id GROUP BY rc.measure_id, r.measure_name, rc.provider_id, rc.state, rc.score, r.national_score, r.stddev  ORDER BY zscore DESC")
effective_normalized.registerTempTable('effective_normalized_tbl')
#.select(first("measure_id"), "measure_name","provider_id","state","score","measure_name","national_score","stddev","zscore")
effective_normalized_sigened = sqlContext.sql("SELECT *, -zscore FROM effective_normalized_tbl WHERE measure_id = 'ED_1b'")

#normalized_ec 
#normalized_rc 

#union_procedures = normalized_ec.unionAll(normalized_rc)

####################################################################################################################################
# What hospitals are models of high-quality care? What states are models of high-quality care?
####################################################################################################################################

# top 10 hospitals
union_procedures_avg = union_procedures.groupBy("provider_id").agg(F.avg("score").alias("avg_score"))
joined_procedures = union_procedures_avg.join(hospitals, hospitals.provider_id == union_procedures_avg.provider_id, "inner").orderBy(union_procedures_avg.avg_score.desc())
joined_procedures.show(10)

# top 10 states
union_procedures_avg_byState = union_procedures.groupBy("state").agg(F.avg("score").alias("avg_score"))
joined_procedures_byState = union_procedures_avg_byState.orderBy(union_procedures_avg_byState.avg_score.desc())
joined_procedures_byState.show(10)

####################################################################################################################################
# Which procedures have the greatest variability between hospitals?
####################################################################################################################################

union_procedures.registerTempTable('union_procedures_tbl')

union_procedures_tbl_variance = sqlContext.sql("SELECT measure_name, measure_id, variance(score) AS variance FROM union_procedures_tbl GROUP BY measure_name, measure_id  ORDER BY variance DESC")
union_procedures_tbl_variance.show(10)

union_procedures_hospitals_variance = sqlContext.sql("SELECT provider_id, variance(score) AS variance FROM union_procedures_tbl GROUP BY provider_id  ORDER BY variance DESC")


####################################################################################################################################
# Are average scores for hospital quality or procedural variability correlated with patient survey responses?
####################################################################################################################################

joined_scores = union_procedures_avg.join(surveys, surveys.provider_number == union_procedures_avg.provider_id, "inner")
joined_scores.stat.corr('avg_score', 'survey_score')

joined_scores_proc = union_procedures_hospitals_variance.join(surveys, surveys.provider_number == union_procedures_hospitals_variance.provider_id, "inner")
joined_scores_proc.stat.corr('variance', 'survey_score')



