# Intelligent Photo Album

The [Intelligent Photo Album](http://deployment-hw2cloudformationhostingbucket-l7tdoaxzw9nb.s3-website-us-east-1.amazonaws.com/) is a serverless, microservice-driven web application that enables users to upload photos, index them with custom label, then search photos using text or microphone. 

## Architecture 
<img width="728" alt="Screenshot 2023-11-18 at 6 23 12 PM" src="https://github.com/madiliu/intelligent_photo_album/assets/90917906/6ef79273-7dd0-4a82-a9a3-723bfe306c83">

## Stack
* [S3](https://aws.amazon.com/s3/) - hosts the frontend and photos, ensures scalability, availability, and durability
* [API Gateway](https://aws.amazon.com/apigateway/) - deploys APIs using Swagger, generates SDK for frontend
* [Lambda](https://aws.amazon.com/lambda/) - takes care of infrastructure to provide serverless, event-driven computer services
  * index-photo - gets photo labels from AWS Rekognition and custom labels provided by users, inserts photos' indices to Open Search
  * search-photo - obtains user inputs through Lex, put them into Open Search to return the photo stored in S3
* [Rekognition](https://aws.amazon.com/tw/rekognition/) - extract photo information using machine learning and computer vision technologies
* [OpenSearch](https://console.aws.amazon.com/es/home) - serves as the index for user to store and find photo with labels 
* [Lex V2](https://aws.amazon.com/lex/) - extracts keywords from users' inputs, supports two labels at most
* [CodePipeline](https://aws.amazon.com/codepipeline/) - automates continuous delivery pipelines should any code updates
* [CloudFormation](https://aws.amazon.com/tw/cloudformation/) - represents all the infrastructure resources and permission, allows quick deployment

## Contributors
[Chia-Mei Liu](https://github.com/madiliu) (UNI: cl4424), [Josephine Chan](https://github.com/honey-grapes) (UNI: cc4799)
