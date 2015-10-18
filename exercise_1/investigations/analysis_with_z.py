#execfile('/data/w205/ucb205/exercise_1/investigations/analysis_with_z.py')

from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import *
from pyspark.sql import functions as F

####################################################################################################################################
# Data and shenanigans
####################################################################################################################################

effective = sqlContext.sql("SELECT * FROM  effective_clean")
effective_national = sqlContext.sql("SELECT * FROM  effective_clean_national")
readmissions = sqlContext.sql("SELECT * FROM  readmissions_clean")
readmissions_national = sqlContext.sql("SELECT * FROM  readmissions_clean_national")
hospitals = sqlContext.sql("SELECT * FROM hospitals_clean")
surveys = sqlContext.sql("SELECT * FROM survey_responses_clean")


ec_max = effective.agg(F.max("score").alias("max_score")).first()
name = 'score'
udf = UserDefinedFunction(lambda x: x/ec_max.max_score, StringType())
normalized_ec = effective.select(*[udf(column).alias(name) if column == name else column for column in effective.columns])

rc_max = readmissions.agg(F.max("score").alias("max_score")).first()
name = 'score'
udf = UserDefinedFunction(lambda x: 1-(x/rc_max.max_score), StringType())
normalized_rc = readmissions.select(*[udf(column).alias(name) if column == name else column for column in readmissions.columns])

union_procedures = normalized_ec.unionAll(normalized_rc)

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



