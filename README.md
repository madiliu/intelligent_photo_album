# Intelligent Photo Album

The [Intelligent Photo Album](http://deployment-hw2cloudformationhostingbucket-l7tdoaxzw9nb.s3-website-us-east-1.amazonaws.com/) is a serverless, microservice-driven web application that enables users to upload photos, index them with label, then search photos using text or microphone. 

## Architecture 
<img width="731" alt="Screenshot 2023-11-18 at 5 04 18 PM" src="https://github.com/madiliu/intelligent_photo_album/assets/90917906/b794a381-b83a-451b-9a4c-c75e6fd99d40">

## Stack
* [S3](https://aws.amazon.com/s3/) - hosts the frontend and photos, ensures scalability, availability, and durability
* [API Gateway](https://aws.amazon.com/apigateway/) - deploys APIs using Swagger, generates SDK for frontend
* [Lambda](https://aws.amazon.com/lambda/) - takes care of infrastructure to provide serverless, event-driven computer services
  * index-photos
  * LF1 - integrates with Lex to validate user inputs and push them to SQS for further processing
  * LF2 - retrieves user inputs from SQS, interacts with ElasticSearch to get the restaurant information from DynamoDB, and sends message to user via email 
* [Lex V2](https://aws.amazon.com/lex/) - extracts keywords from users' inputs, supports two labels at most
* [CloudFormation](https://aws.amazon.com/tw/cloudformation/) - 
* [OpenSearch](https://console.aws.amazon.com/es/home) - serves as the index for DynamoDB to find restaurant ID with cuisine

## Use Cases
<img width="669" alt="Screenshot 2023-10-17 at 8 03 15 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/b29e6919-585f-41ab-b80f-6f62c1f68953">
<img width="661" alt="Screenshot 2023-10-17 at 8 03 28 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/aa21528e-298a-4be0-b242-81558d5e475d">
<img width="659" alt="Screenshot 2023-10-17 at 8 03 46 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/6ba7df7b-cff3-4f4b-8542-edeabbdcbc61">
<img width="657" alt="Screenshot 2023-10-17 at 8 03 53 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/d15f4043-0d41-4b27-9b9f-8302cf73ca78">
<img width="628" alt="Screenshot 2023-10-17 at 8 08 49 PM" src="https://github.com/madiliu/dining_concierge_chatbot/assets/90917906/fd3778f8-7599-4017-9e3b-753adcb0131c">

## Contributors
[Chia-Mei Liu](https://github.com/madiliu) (UNI: cl4424), [Josephine Chan](https://github.com/honey-grapes) (UNI: cc4799)
