####################################################################################################################################
# What states are models of high-quality care?
####################################################################################################################################

# top 10 states
union_procedures_avg_byState = union_procedures.groupBy("state").agg(F.avg("zscore").alias("avg_zscore"))
joined_procedures_byState = union_procedures_avg_byState.orderBy(union_procedures_avg_byState.avg_zscore.desc())
joined_procedures_byState.show(10)