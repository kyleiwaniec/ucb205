DROP TABLE hospitals;
CREATE EXTERNAL TABLE IF NOT EXISTS hospitals
(
Provider_ID STRING,
Hospital_Name STRING,
Address STRING,
City STRING,
State STRING,
ZIP_Code STRING,
County_Name STRING,
Phone_Number STRING,
Hospital_Type STRING,
Hospital_Ownership STRING,
Emergency_Services STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ",",
	"quoteChar"		= '"',
	"escapeChar"	= '\\'
)
STORED as TEXTFILE
LOCATION '/user/w205/hospital_compare/hospitals';


DROP TABLE effective_care;
CREATE EXTERNAL TABLE IF NOT EXISTS effective_care
(
Provider_ID STRING,
Hospital_Name STRING,
Address STRING,
City STRING,
State STRING,
ZIP_Code  STRING,
County_Name STRING,
Phone_Number STRING,
Condition  STRING,
Measure_ID  STRING,
Measure_Name STRING,
Score  STRING,
Sample STRING,
Footnote STRING,
Measure_Start_Date STRING,
Measure_End_Date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ",",
	"quoteChar"		= '"',
	"escapeChar"	= '\\'
)
STORED as TEXTFILE
LOCATION '/user/w205/hospital_compare/effective_care';


DROP TABLE effective_care_national;
CREATE EXTERNAL TABLE IF NOT EXISTS effective_care_national
(
Measure_Name STRING,
Measure_ID STRING,
Condition STRING,
Category STRING,
Score STRING,
Footnote STRING,
Measure_Start_Date STRING,
Measure_End_Date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ",",
	"quoteChar"		= '"',
	"escapeChar"	= '\\'
)
STORED as TEXTFILE
LOCATION '/user/w205/hospital_compare/effective_care_national';


DROP TABLE readmissions;
CREATE EXTERNAL TABLE IF NOT EXISTS readmissions
(
Provider_ID STRING,
Hospital_Name STRING,
Address STRING,
City STRING,
State STRING,
ZIP_Code STRING,
County_Name STRING,
Phone_Number STRING,
Measure_Name STRING,
Measure_ID STRING,
Compared_to_National STRING,
Denominator STRING,
Score STRING,
Lower_Estimate STRING,
Higher_Estimate STRING,
Footnote STRING,
Measure_Start_Date STRING,
Measure_End_Date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ",",
	"quoteChar"		= '"',
	"escapeChar"	= '\\'
)
STORED as TEXTFILE
LOCATION '/user/w205/hospital_compare/readmissions';


DROP TABLE readmissions_national;
CREATE EXTERNAL TABLE IF NOT EXISTS readmissions_national
(
Measure_Name STRING,
Measure_ID STRING,
National_Rate STRING,
Number_of_Hospitals_Worse STRING,
Number_of_Hospitals_Same STRING,
Number_of_Hospitals_Better STRING,
Number_of_Hospitals_Too_Few STRING,
Footnote STRING,
Measure_Start_Date STRING,
Measure_End_Date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ",",
	"quoteChar"		= '"',
	"escapeChar"	= '\\'
)
STORED as TEXTFILE
LOCATION '/user/w205/hospital_compare/readmissions_national';



DROP TABLE survey_responses;
CREATE EXTERNAL TABLE IF NOT EXISTS survey_responses
(
Provider_Number STRING,
Hospital_Name STRING,
Address STRING,
City STRING,
State STRING,
ZIP_Code STRING,
County_Name STRING,
Communication_with_Nurses_Achievement_Points STRING,
Communication_with_Nurses_Improvement_Points STRING,
Communication_with_Nurses_Dimension_Score STRING,
Communication_with_Doctors_Achievement_Points STRING,
Communication_with_Doctors_Improvement_Points STRING,
Communication_with_Doctors_Dimension_Score STRING,
Responsiveness_of_Hospital_Staff_Achievement_Points STRING,
Responsiveness_of_Hospital_Staff_Improvement_Points STRING,
Responsiveness_of_Hospital_Staff_Dimension_Score STRING,
Pain_Management_Achievement_Points STRING,
Pain_Management_Improvement_Points STRING,
Pain_Management_Dimension_Score STRING,
Communication_about_Medicines_Achievement_Points STRING,
Communication_about_Medicines_Improvement_Points STRING,
Communication_about_Medicines_Dimension_Score STRING,
Cleanliness_and_Quietness_of_Hospital_Environment_Achievement_Points STRING,
Cleanliness_and_Quietness_of_Hospital_Environment_Improvement_Points STRING,
Cleanliness_and_Quietness_of_Hospital_Environment_Dimension_Score STRING,
Discharge_Information_Achievement_Points STRING,
Discharge_Information_Improvement_Points STRING,
Discharge_Information_Dimension_Score STRING,
Overall_Rating_of_Hospital_Achievement_Points STRING,
Overall_Rating_of_Hospital_Improvement_Points STRING,
Overall_Rating_of_Hospital_Dimension_Score STRING,
HCAHPS_Base_Score STRING,
HCAHPS_Consistency_Score STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
	"separatorChar" = ",",
	"quoteChar"		= '"',
	"escapeChar"	= '\\'
)
STORED as TEXTFILE
LOCATION '/user/w205/hospital_compare/survey_responses';



