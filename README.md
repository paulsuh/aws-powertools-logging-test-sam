# Example of the Actual Logger in AWS Lambda Powertools
 
This shows the effect of setting the log level on the apparent 
powertools logger vs. the underlying actual logger. 

(Level 20 = INFO, Level 10 = DEBUG)

## Cloudwatch Logs Output
| timestamp     | message                                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | # Default logging levels                                                                                                                                                                                             |
| 1680237900023 | powertools_logger level = 20                                                                                                                                                                                         |
| 1680237900023 | actual_logger level = 20                                                                                                                                                                                             |
| 1680237900024 | {"level":"INFO","location":"lambda_handler:23","message":"info-level log output","timestamp":"2023-03-31 04:45:00,023+0000","service":"service_undefined","xray_trace_id":"1-6426654b-d009bd1ba059909921f4a486"}     |
|               | # Set log level of powertools_logger to DEBUG                                                                                                                                                                        |
| 1680237900024 | powertools_logger level = 10                                                                                                                                                                                         |
| 1680237900024 | actual_logger level = 20                                                                                                                                                                                             |
|               | # Note that only the INFO-level log statement runs                                                                                                                                                                   |
| 1680237900024 | {"level":"INFO","location":"lambda_handler:30","message":"info-level log output 2","timestamp":"2023-03-31 04:45:00,024+0000","service":"service_undefined","xray_trace_id":"1-6426654b-d009bd1ba059909921f4a486"}   |
|               | # Set log level of actual_logger to DEBUG                                                                                                                                                                            |
| 1680237900024 | powertools_logger level = 10                                                                                                                                                                                         |
| 1680237900024 | actual_logger level = 10                                                                                                                                                                                             |
|               | # Note that the DEBUG-level log statement runs as well                                                                                                                                                               |
| 1680237900024 | {"level":"INFO","location":"lambda_handler:37","message":"info-level log output 3","timestamp":"2023-03-31 04:45:00,024+0000","service":"service_undefined","xray_trace_id":"1-6426654b-d009bd1ba059909921f4a486"}   |
| 1680237900024 | {"level":"DEBUG","location":"lambda_handler:38","message":"debug-level log output 3","timestamp":"2023-03-31 04:45:00,024+0000","service":"service_undefined","xray_trace_id":"1-6426654b-d009bd1ba059909921f4a486"} |
