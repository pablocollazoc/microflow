
Analysis results for sample-spring-microservices project
========================================================


This GitHub page shows the analysis results for the requested flow execution for sample-spring-microservicesproject
# **Quality gate status:**


***Not passed*** :x:

Quality gate conditions do not passed. Some of these conditions were not acquired: 
- Code coverage is less than 80% 
- 
Duplicated lines is greater than 3% 
- Maintainability rating is worse than A 
- Reliability rating is worse than A 
- 
Security hotspots reviewed is less than 100% 
- Security rating is worse than A 

# **Technical debt:** 0h 24min


{% include charts.html %}
# **Bugs found:**
  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |

# **Code smells found:**
  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:account-service/src/main/java/pl/piomin/microservices/account/api/Api.java|29|
|1|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:account-service/src/main/java/pl/piomin/microservices/account/api/Api.java|38|
|2|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:account-service/src/main/java/pl/piomin/microservices/account/api/Api.java|46|
|3|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:account-service/src/main/java/pl/piomin/microservices/account/api/Api.java|52|
|4|Replace "@RequestMapping(method = RequestMethod.POST)" with "@PostMapping"|MINOR|2min|project:account-service/src/main/java/pl/piomin/microservices/account/api/Api.java|61|
|5|Replace "@RequestMapping(method = RequestMethod.DELETE)" with "@DeleteMapping"|MINOR|2min|project:account-service/src/main/java/pl/piomin/microservices/account/api/Api.java|73|
|6|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:customer-service/src/main/java/pl/piomin/microservices/customer/api/Api.java|32|
|7|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:customer-service/src/main/java/pl/piomin/microservices/customer/api/Api.java|41|
|8|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:customer-service/src/main/java/pl/piomin/microservices/customer/api/Api.java|47|
|9|Replace "@RequestMapping(method = RequestMethod.POST)" with "@PostMapping"|MINOR|2min|project:customer-service/src/main/java/pl/piomin/microservices/customer/api/Api.java|59|
|10|Replace "@RequestMapping(method = RequestMethod.DELETE)" with "@DeleteMapping"|MINOR|2min|project:customer-service/src/main/java/pl/piomin/microservices/customer/api/Api.java|71|
|11|Replace "@RequestMapping(method = RequestMethod.GET)" with "@GetMapping"|MINOR|2min|project:customer-service/src/main/java/pl/piomin/microservices/customer/intercomm/AccountClient.java|15|

# **Vulnerabilities found:**
  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
