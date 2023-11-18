# intelligent_photo_album

The [Intelligent Photo Album](http://deployment-hw2cloudformationhostingbucket-l7tdoaxzw9nb.s3-website-us-east-1.amazonaws.com/) is a serverless, microservice-driven web application that enables users to upload photo, index it with label, then search for it using text or sends customers restaurant suggestions given a set of preferences that they provide the chatbot with through conversation.

## Architecture 
<img width="602" alt="Screenshot 2023-02-07 at 3 21 54 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/1c858004-aebb-43ca-a123-7530a105f28b">

## Stack
* [S3](https://aws.amazon.com/s3/) - hosts the frontend, ensures scalability, availability, and durability
* [API Gateway](https://aws.amazon.com/apigateway/) - deploys APIs, including POST and OPTIONS
* [Swagger](https://swagger.io/tools/swagger-ui/) - sets up integrated and documented APIs by being imported to API Gateway
* [Lambda](https://aws.amazon.com/lambda/) - takes care of infrastructure to provide serverless, event-driven computer services
  * LF0 - receives messages from the frontend user, send messages to Dining Chatbot in Lex
  * LF1 - integrates with Lex to validate user inputs and push them to SQS for further processing
  * LF2 - retrieves user inputs from SQS, interacts with ElasticSearch to get the restaurant information from DynamoDB, and sends message to user via email 
* [Lex V2](https://aws.amazon.com/lex/) - creates and deploys the dining chatbot with threes intents (GreetingIntent, DiningSuggestionsIntent, ThankYouIntent) 
* [Simple Queue Servive](https://console.aws.amazon.com/sqs/v2/home) - processes information in FIFO manner to realize asynchronous workflows
* [Simple Email Service](https://aws.amazon.com/tw/ses/) - sends emails
* [ElasticSearch](https://console.aws.amazon.com/es/home) - serves as the index for DynamoDB to find restaurant ID with cuisine
* [DynamoDB](https://console.aws.amazon.com/dynamodb/home?region=us-east-1) - stores 6400+ restaurants information scraped from Yelp API due to the unstructured data

## Use Cases
<img width="669" alt="Screenshot 2023-10-17 at 8 03 15 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/b29e6919-585f-41ab-b80f-6f62c1f68953">
<img width="661" alt="Screenshot 2023-10-17 at 8 03 28 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/aa21528e-298a-4be0-b242-81558d5e475d">
<img width="659" alt="Screenshot 2023-10-17 at 8 03 46 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/6ba7df7b-cff3-4f4b-8542-edeabbdcbc61">
<img width="657" alt="Screenshot 2023-10-17 at 8 03 53 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/d15f4043-0d41-4b27-9b9f-8302cf73ca78">
<img width="628" alt="Screenshot 2023-10-17 at 8 08 49 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/fd3778f8-7599-4017-9e3b-753adcb0131c">

## Note
* Would recommend 8 types of cuisines, including Taiwanese, Mexican, French, Italian, Japanese, Indian, Korean, Thai
* 6400+ restaurants are located in New York, including Manhattan, Brooklyn', Queens, Sunset Park, Edgewater, Bensonhurst, Jackson Heights, Union City, Fairview, Crown Heights, Staten Island, Astoria, Sunnyside, and Long Island City
* Could only recommend restaurants for 1 to 20 people considering restaurants' capacities

## Contributors
[Chia-Mei Liu](https://github.com/madiliu) (UNI: cl4424), [Josephine Chan](https://github.com/honey-grapes) (UNI: cc4799)
