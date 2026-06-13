CREATE TABLE bronze.race_results_RUNSIGNUP_V1(race_event_id VARCHAR PRIMARY KEY, race_event_name VARCHAR, race_event_data_source_id VARCHAR, raw_data JSON, created_at TIMESTAMP WITH TIME ZONE);;

CREATE TABLE bronze.visual_crossing_weather(race_event_id VARCHAR PRIMARY KEY, race_location_id VARCHAR, zip_code VARCHAR, race_date DATE, fetched_at TIMESTAMP WITH TIME ZONE, api_response JSON, processing_status VARCHAR DEFAULT('PENDING'));;

CREATE TABLE pipeline_log(logged_at TIMESTAMP WITH TIME ZONE, run_id VARCHAR, "level" VARCHAR, layer VARCHAR, event_type VARCHAR, race_event_id VARCHAR, message VARCHAR, stack_trace VARCHAR, process VARCHAR, context JSON);;

CREATE TABLE unmapped_source_fields(data_source_id VARCHAR, source_field_name VARCHAR, sample_value VARCHAR, logged_at TIMESTAMP WITH TIME ZONE, PRIMARY KEY(data_source_id, source_field_name));;

CREATE TABLE silver.race(race_id VARCHAR, race_name VARCHAR, race_description VARCHAR, race_active BOOLEAN);;

CREATE TABLE silver.race_course(race_course_id VARCHAR, race_course_type VARCHAR, race_course_name VARCHAR, race_course_description VARCHAR);;

CREATE TABLE silver.race_distance(race_distance_id VARCHAR, race_distance_name VARCHAR, race_distance_weather_observation_count VARCHAR);;

CREATE TABLE silver.race_event(race_event_id VARCHAR, race_event_name VARCHAR, race_date TIMESTAMP, race_start_hour VARCHAR, race_event_metadata_1_key VARCHAR, race_event_metadata_1_value VARCHAR, race_event_metadata_2_key VARCHAR, race_event_metadata_2_value VARCHAR, race_event_metadata_3_key VARCHAR, race_event_metadata_3_value VARCHAR, race_id VARCHAR, race_distance_id VARCHAR, race_location_id VARCHAR, race_course_id VARCHAR, race_event_data_source_id VARCHAR, race_event_active BOOLEAN);;

CREATE TABLE silver.race_event_data_source(data_source_id VARCHAR, data_source_name VARCHAR, data_ingestion_type VARCHAR, data_ingestion_detail VARCHAR, data_source_key_1_name VARCHAR, data_source_key_1_value VARCHAR, data_source_key_2_name VARCHAR, data_source_key_2_value VARCHAR, data_source_key_3_name VARCHAR, data_source_key_3_value VARCHAR, data_source_path VARCHAR);;

CREATE TABLE silver.race_event_data_source_field_map(data_source_id VARCHAR, source_field_name VARCHAR, target_field_name VARCHAR);;

CREATE TABLE silver.race_location(race_location_id VARCHAR, race_location_name VARCHAR, race_address VARCHAR, race_city VARCHAR, race_state VARCHAR, race_zip VARCHAR);;

CREATE TABLE silver.race_results(age BIGINT, chip_time VARCHAR, bib VARCHAR, first_name VARCHAR, clock_time VARCHAR, last_name VARCHAR, gender VARCHAR, source_result_id VARCHAR, result_id VARCHAR, race_event_id VARCHAR, created_at TIMESTAMP, finish_time VARCHAR, finish_time_seconds DOUBLE, is_active BOOLEAN DEFAULT(CAST('t' AS BOOLEAN)));;

CREATE TABLE silver.race_result_field(race_result_field_name VARCHAR);;

CREATE TABLE silver.race_weather_hourly(race_event_id VARCHAR, "hour" VARCHAR, temp_f DOUBLE, feels_like_f DOUBLE, humidity_pct DOUBLE, dew_point_f DOUBLE, precip_in DOUBLE, precip_prob_pct DOUBLE, precip_type VARCHAR, wind_speed_mph DOUBLE, wind_gust_mph DOUBLE, wind_dir_deg DOUBLE, pressure_mb DOUBLE, visibility_mi DOUBLE, cloud_cover_pct DOUBLE, uv_index DOUBLE, conditions VARCHAR, is_active BOOLEAN DEFAULT(CAST('t' AS BOOLEAN)), created_at TIMESTAMP WITH TIME ZONE, PRIMARY KEY(race_event_id, "hour"));;

