

## CREATE JOB SERVICE

```sql
USE ROLE TECHUP_DEMO_ROLE;
USE DATABASE TECHUP_DEMO_DB;
USE SCHEMA DATA_SCHEMA;
USE WAREHOUSE TECHUP_DEMO_WH;


SHOW IMAGES IN IMAGE REPOSITORY TECHUP_DEMO_REPOSITORY;
list @TECHUP_DEMO_STAGE;


EXECUTE JOB SERVICE
IN COMPUTE POOL TECHUP_DEMO_COMPUTE_POOL
NAME=TECHUP_JOB_SERVICE
FROM @TECHUP_DEMO_STAGE
SPEC='techup_job.yaml';


SELECT SYSTEM$GET_SERVICE_STATUS('TECHUP_JOB_SERVICE');
SELECT SYSTEM$GET_SERVICE_LOGS('TECHUP_JOB_SERVICE', 0, 'main');

SELECT * FROM results;


--drop  SERVICE TECHUP_JOB_SERVICE;
```
