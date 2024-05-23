

## CREATE GIT JOB SERVICE 

```sql

USE ROLE TECHUP_DEMO_ROLE;
USE DATABASE TECHUP_DEMO_DB;
USE SCHEMA DATA_SCHEMA;
USE WAREHOUSE TECHUP_DEMO_WH;


SHOW IMAGES IN IMAGE REPOSITORY TECHUP_DEMO_REPOSITORY;
list @TECHUP_DEMO_STAGE;

USE ROLE ACCOUNTADMIN;

DROP EXTERNAL ACCESS INTEGRATION git_access_integration;

CREATE OR REPLACE NETWORK RULE git_network_rule
  MODE = EGRESS
  TYPE = HOST_PORT
  VALUE_LIST = ('github.com:443');

CREATE EXTERNAL ACCESS INTEGRATION git_access_integration
  ALLOWED_NETWORK_RULES = (git_network_rule)
  ENABLED = true;


GRANT USAGE ON INTEGRATION git_access_integration TO ROLE TECHUP_DEMO_ROLE;


USE ROLE TECHUP_DEMO_ROLE;


EXECUTE JOB SERVICE
IN COMPUTE POOL TECHUP_DEMO_COMPUTE_POOL
NAME=TECHUP_GIT_JOB_SERVICE
EXTERNAL_ACCESS_INTEGRATIONS = (GIT_ACCESS_INTEGRATION)
FROM @TECHUP_DEMO_STAGE
SPEC='techup_git_job.yaml';


SELECT SYSTEM$GET_SERVICE_STATUS('TECHUP_GIT_JOB_SERVICE');
SELECT SYSTEM$GET_SERVICE_LOGS('TECHUP_GIT_JOB_SERVICE', 0, 'main');

drop  SERVICE TECHUP_GIT_JOB_SERVICE;
```
