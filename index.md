
Analysis results for spring-boot-microservices-series project
=============================================================


This GitHub page shows the analysis results for the requested flow execution for spring-boot-microservices-seriesproject

{% include charts.html %}

**Bugs found:**  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|A "NullPointerException" could be thrown; "getBody()" can return null.|MAJOR|10min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|67|
|1|Call "remove()" on "CORRELATION_ID".|MAJOR|10min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/MyThreadLocalsHolder.java|4|


**Code smells found:**  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|Remove this commented out code.|MAJOR|5min|Devops-API:shoppingcart-ui/pom.xml|53|
|1|This block of commented-out lines of code should be removed.|MAJOR|5min|Devops-API:shoppingcart-ui/src/main/java/com/sivalabs/shoppingcartui/ShoppingcartUiApplication.java|6|
|2|Remove this commented out code.|MAJOR|5min|Devops-API:catalog-service/pom.xml|26|
|3|Rename this local variable to match the regular expression '^[a-z][a-zA-Z0-9]*$'.|MINOR|2min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/web/controllers/ProductController.java|31|
|4|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:oauth2-server/src/test/java/com/sivalabs/oauth2server/Oauth2ServerApplicationTests.java|13|
|5|This block of commented-out lines of code should be removed.|MAJOR|5min|Devops-API:shoppingcart-ui/src/main/java/com/sivalabs/shoppingcartui/filters/AuthHeaderFilter.java|26|
|6|This block of commented-out lines of code should be removed.|MAJOR|5min|Devops-API:shoppingcart-ui/src/main/java/com/sivalabs/shoppingcartui/filters/AuthHeaderFilter.java|39|
|7|Remove this commented out code.|MAJOR|5min|Devops-API:zipkin-server/pom.xml|17|
|8|Remove this commented out code.|MAJOR|5min|Devops-API:zipkin-server/pom.xml|26|
|9|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:zipkin-server/src/test/java/com/sivalabs/zipkinserver/ZipkinServerApplicationTests.java|13|
|10|This block of commented-out lines of code should be removed.|MAJOR|5min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|59|
|11|Immediately return this expression instead of assigning it to the temporary variable "availableProducts".|MINOR|2min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/services/ProductService.java|31|
|12|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:order-service/src/test/java/com/sivalabs/orderservice/OrderServiceApplicationTests.java|13|
|13|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:shoppingcart-ui/src/test/java/com/sivalabs/shoppingcartui/ShoppingcartUiApplicationTests.java|13|
|14|Complete the task associated to this TODO comment.|INFO|-|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|23|
|15|Refactor your code to get this URI from a customizable parameter.|MINOR|20min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/services/InventoryServiceClient.java|24|
|16|Provide the parametrized type for this generic.|MAJOR|5min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/ContextCopyHystrixConcurrencyStrategy.java|20|
|17|Add a private constructor to hide the implicit public one.|MAJOR|5min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/MyThreadLocalsHolder.java|3|
|18|Provide the parametrized type for this generic.|MAJOR|5min|Devops-API:catalog-service/src/main/java/com/sivalabs/catalogservice/utils/MyThreadLocalsHolder.java|4|
|19|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:hystrix-dashboard/src/test/java/com/sivalabs/hystrixdashboard/HystrixDashboardApplicationTests.java|13|
|20|Provide the parametrized type for this generic.|MAJOR|5min|Devops-API:inventory-service/src/main/java/com/sivalabs/inventoryservice/web/controllers/InventoryController.java|33|
|21|Provide the parametrized type for this generic.|MAJOR|5min|Devops-API:inventory-service/src/main/java/com/sivalabs/inventoryservice/web/controllers/InventoryController.java|35|
|22|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:inventory-service/src/test/java/com/sivalabs/inventoryservice/InventoryServiceApplicationTests.java|13|
|23|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:service-registry/src/test/java/com/sivalabs/serviceregistry/ServiceRegistryApplicationTests.java|13|
|24|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:catalog-service/src/test/java/com/sivalabs/catalogservice/CatalogServiceApplicationTests.java|13|
|25|Add at least one assertion to this test case.|BLOCKER|10min|Devops-API:config-server/src/test/java/com/sivalabs/configserver/ConfigServerApplicationTests.java|13|


**Vulnerabilities found:**  

|Nº|Description|Severity|Estimated resolution time|File|Line|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|Replace this persistent entity with a simple POJO or DTO object.|CRITICAL|10min|Devops-API:order-service/src/main/java/com/sivalabs/orderservice/web/controllers/OrderController.java|21|
