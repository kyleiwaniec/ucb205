####################################################################################################################################
# Are average scores for hospital quality or procedural variability correlated with patient survey responses?
####################################################################################################################################

joined_scores = union_procedures_avg.join(surveys, surveys.provider_number == union_procedures_avg.provider_id, "inner")
hospital_quality_correlation = joined_scores.stat.corr('avg_zscore', 'survey_score')

joined_scores_proc = hospitals_variance.join(surveys, surveys.provider_number == hospitals_variance.provider_id, "inner")
hospital_variance_correlation = joined_scores_proc.stat.corr('variance', 'survey_score')
