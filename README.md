# CDBv4 AWS Doorbell Lambda

This repository contains the code for the Cat Doorbell Version 4 (CDBv4), implemented as an AWS Lambda function. The main purpose of this project is to manage notifications when the cat doorbell is activated and to log heartbeats for monitoring purposes.

## Table of Contents

- [Architecture](#architecture)
- [Setup](#setup)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The CDBv4 AWS Doorbell Lambda function handles HTTP POST requests for two endpoints:
- `/ring`: Triggered when the cat doorbell is activated. It sends a notification via Amazon SNS.
- `/heartbeat`: Logs a heartbeat message for monitoring purposes.

The architecture consists of the following components:
- **AWS Lambda**: Executes the main logic for handling the doorbell and heartbeat events.
- **Amazon SNS**: Used to send notifications when the doorbell is activated.

## Setup

### Prerequisites

- Python 3.8+
- AWS account with necessary permissions for Lambda and SNS
- AWS CLI configured with your account

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/CDBv4-aws-doorbell-lambda.git
   cd CDBv4-aws-doorbell-lambda
   ```

2. Install the required Python packages:

   ```bash
   pip install -r lambda/requirements.txt
   ```

## Deployment

1. Package the Lambda function:

   ```bash
   zip -r lambda_function.zip lambda/
   ```

2. Create an AWS Lambda function and upload the `lambda_function.zip` package.

3. Set the following environment variables for the Lambda function:
   - `SNS_TOPIC_ARN`: The ARN of the SNS topic to which notifications will be sent.

4. Create an API Gateway with two POST endpoints:
   - `/ring`
   - `/heartbeat`

5. Integrate the API Gateway with the Lambda function.

## Usage

### Ring Endpoint

Trigger the doorbell notification by sending a POST request to the `/ring` endpoint:

```bash
curl -X POST https://your-api-endpoint/ring -d '{"message": "Cat at the door!"}'
```

### Heartbeat Endpoint

Log a heartbeat message by sending a POST request to the `/heartbeat` endpoint:

```bash
curl -X POST https://your-api-endpoint/heartbeat -d '{"status": "ok"}'
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
