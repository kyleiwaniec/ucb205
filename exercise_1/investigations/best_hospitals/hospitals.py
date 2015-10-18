####################################################################################################################################
# What hospitals are models of high-quality care?
####################################################################################################################################

# top 10 hospitals
union_procedures_avg = union_procedures.groupBy("provider_id").agg(F.avg("zscore").alias("avg_zscore"))
joined_procedures = union_procedures_avg.join(hospitals, hospitals.provider_id == union_procedures_avg.provider_id, "inner").orderBy(union_procedures_avg.avg_zscore.desc())
joined_procedures.show(10)