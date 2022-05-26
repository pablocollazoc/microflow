---
layout: default
---
<section id="downloads"><a href="https://pablocollazoc.github.io/microflow/2022-05-26-19_55-spring-boot-microservices-series/checkstyle" class="btn">Checkstyle results</a><a href="https://pablocollazoc.github.io/microflow/2022-05-26-19_55-spring-boot-microservices-series/spotbugs" class="btn">Spotbugs results</a><a href="{{ site.github.repository_url }}" class="btn btn-github"><span class="icon"></span>View on GitHub</a></section>

 
Analysis results for spring-boot-microservices-series project
=============================================================


This GitHub page shows the analysis results for the requested flow execution for spring-boot-microservices-seriesproject
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

# **Technical debt:** 3h 29min


{% include 2022-05-26-19_55-charts.html%}
# **Bugs found:**
  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|A "NullPointerException" could be thrown; "getBody()" can return null.|MAJOR|10min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|67|
|1|Call "remove()" on "CORRELATION_ID".|MAJOR|10min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/MyThreadLocalsHolder.java|4|

# **Code smells found:**
  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|Remove this commented out code.|MAJOR|5min|project:catalog-service/pom.xml|26|
|1|Complete the task associated to this TODO comment.|INFO|-|project:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|23|
|2|Refactor your code to get this URI from a customizable parameter.|MINOR|20min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|24|
|3|This block of commented-out lines of code should be removed.|MAJOR|5min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|59|
|4|Immediately return this expression instead of assigning it to the temporary variable "availableProducts".|MINOR|2min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/services/ProductService.java|31|
|5|Provide the parametrized type for this generic.|MAJOR|5min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/ContextCopyHystrixConcurrencyStrategy.java|20|
|6|Add a private constructor to hide the implicit public one.|MAJOR|5min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/MyThreadLocalsHolder.java|3|
|7|Provide the parametrized type for this generic.|MAJOR|5min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/MyThreadLocalsHolder.java|4|
|8|Rename this local variable to match the regular expression '^[a-z][a-zA-Z0-9]*$'.|MINOR|2min|project:catalog-service/src/main/java/com/sivalabs/catalogservice/web/controllers/ProductController.java|31|
|9|Add at least one assertion to this test case.|BLOCKER|10min|project:catalog-service/src/test/java/com/sivalabs/catalogservice/CatalogServiceApplicationTests.java|13|
|10|Add at least one assertion to this test case.|BLOCKER|10min|project:config-server/src/test/java/com/sivalabs/configserver/ConfigServerApplicationTests.java|13|
|11|Add at least one assertion to this test case.|BLOCKER|10min|project:hystrix-dashboard/src/test/java/com/sivalabs/hystrixdashboard/HystrixDashboardApplicationTests.java|13|
|12|Provide the parametrized type for this generic.|MAJOR|5min|project:inventory-service/src/main/java/com/sivalabs/inventoryservice/web/controllers/InventoryController.java|33|
|13|Provide the parametrized type for this generic.|MAJOR|5min|project:inventory-service/src/main/java/com/sivalabs/inventoryservice/web/controllers/InventoryController.java|35|
|14|Add at least one assertion to this test case.|BLOCKER|10min|project:inventory-service/src/test/java/com/sivalabs/inventoryservice/InventoryServiceApplicationTests.java|13|
|15|Add at least one assertion to this test case.|BLOCKER|10min|project:oauth2-server/src/test/java/com/sivalabs/oauth2server/Oauth2ServerApplicationTests.java|13|
|16|Add at least one assertion to this test case.|BLOCKER|10min|project:order-service/src/test/java/com/sivalabs/orderservice/OrderServiceApplicationTests.java|13|
|17|Add at least one assertion to this test case.|BLOCKER|10min|project:service-registry/src/test/java/com/sivalabs/serviceregistry/ServiceRegistryApplicationTests.java|13|
|18|Remove this commented out code.|MAJOR|5min|project:shoppingcart-ui/pom.xml|53|
|19|This block of commented-out lines of code should be removed.|MAJOR|5min|project:shoppingcart-ui/src/main/java/com/sivalabs/shoppingcartui/ShoppingcartUiApplication.java|6|
|20|This block of commented-out lines of code should be removed.|MAJOR|5min|project:shoppingcart-ui/src/main/java/com/sivalabs/shoppingcartui/filters/AuthHeaderFilter.java|26|
|21|This block of commented-out lines of code should be removed.|MAJOR|5min|project:shoppingcart-ui/src/main/java/com/sivalabs/shoppingcartui/filters/AuthHeaderFilter.java|39|
|22|Add at least one assertion to this test case.|BLOCKER|10min|project:shoppingcart-ui/src/test/java/com/sivalabs/shoppingcartui/ShoppingcartUiApplicationTests.java|13|
|23|Remove this commented out code.|MAJOR|5min|project:zipkin-server/pom.xml|17|
|24|Remove this commented out code.|MAJOR|5min|project:zipkin-server/pom.xml|26|
|25|Add at least one assertion to this test case.|BLOCKER|10min|project:zipkin-server/src/test/java/com/sivalabs/zipkinserver/ZipkinServerApplicationTests.java|13|

# **Vulnerabilities found:**
  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|Replace this persistent entity with a simple POJO or DTO object.|CRITICAL|10min|project:order-service/src/main/java/com/sivalabs/orderservice/web/controllers/OrderController.java|21|
