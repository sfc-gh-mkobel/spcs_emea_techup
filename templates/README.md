

## CREATE GIT JOB SERVICE 

```sql
USE ROLE TECHUP_DEMO_ROLE;
USE DATABASE TECHUP_DEMO_DB;
USE SCHEMA DATA_SCHEMA;
USE WAREHOUSE TECHUP_DEMO_WH;


EXECUTE JOB SERVICE
IN COMPUTE POOL TECHUP_DEMO_COMPUTE_POOL
using(git_repo_url=>'https://github.com/sfc-gh-mkobel/python-code.git',repo_name=>'python-code',main_file_name=>'main.py')
NAME=TECHUP_TEMPLATE_GIT_JOB_SERVICE
EXTERNAL_ACCESS_INTEGRATIONS = (GIT_ACCESS_INTEGRATION)
FROM @TECHUP_DEMO_STAGE
SPEC='techup_template_git_job.yaml';


SELECT SYSTEM$GET_SERVICE_STATUS('TECHUP_TEMPLATE_GIT_JOB_SERVICE');
SELECT SYSTEM$GET_SERVICE_LOGS('TECHUP_TEMPLATE_GIT_JOB_SERVICE', 0, 'main');



drop  SERVICE TECHUP_TEMPLATE_GIT_JOB_SERVICE;
```
