# spcs_emea_techup

## CREATE SERVICE

```sql
USE ROLE TECHUP_DEMO_ROLE;
USE DATABASE TECHUP_DEMO_DB;
USE SCHEMA DATA_SCHEMA;
USE WAREHOUSE TECHUP_DEMO_WH;

CREATE SERVICE TECHUP_DEMO_SERVICE
  IN COMPUTE POOL TECHUP_DEMO_COMPUTE_POOL
  FROM @TECHUP_DEMO_STAGE
  SPEC='techup_service.yaml'
  QUERY_WAREHOUSE =TECHUP_DEMO_WH
  MIN_INSTANCES=1
  MAX_INSTANCES=1;

show endpoints in service TECHUP_DEMO_SERVICE;
SELECT SYSTEM$GET_SERVICE_STATUS('TECHUP_DEMO_SERVICE');
SELECT SYSTEM$GET_SERVICE_LOGS('TECHUP_DEMO_SERVICE',0, 'techup-service');

select
  v.value:containerName::varchar container_name
  ,v.value:status::varchar status  
  ,v.value:message::varchar message
from (select parse_json(system$get_service_status('TECHUP_DEMO_SERVICE'))) t,
lateral flatten(input => t.$1) v;
```
