# Simple Greeting API — AWS Lambda + API Gateway

A beginner-friendly serverless project: one Python function on **AWS Lambda**, exposed through **Amazon API Gateway** as a REST endpoint. Call it with a name in the URL and it replies with a personalized greeting in JSON.

This is intentionally small — one function, one route — so you can fully understand and confidently explain every part of it, which matters more for a fresher's resume project than complexity does.

## What it does

Send a GET request to:
```
/hello?name=Riya
```
Get back:
```json
{ "message": "Hello, Riya! Welcome to your first Lambda-powered API." }
```

## How it works (in plain terms)

1. You (or anyone) opens the API URL in a browser or calls it with `curl`.
2. **API Gateway** receives that HTTP request and forwards it to your **Lambda function**.
3. The **Lambda function** (plain Python — `lambda_function.py`) reads the `name` from the request, builds a message, and returns it.
4. API Gateway sends that response back to you as JSON.

No servers to manage, nothing running 24/7 — AWS only runs your code for the split second it's needed, and you pay (practically nothing, at this scale — free tier covers it) only for that.

## Project structure

```
simple-lambda-api/
├── template.yaml           # Infrastructure as Code — defines the Lambda + API Gateway
└── src/
    └── lambda_function.py  # The actual function logic (20 lines)
```

## Prerequisites (install once)

1. **AWS account** (free tier is enough) — https://aws.amazon.com/free
2. **AWS CLI** — https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
3. **AWS SAM CLI** — https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
4. **Python 3.12**
5. Run once: `aws configure` — enter your AWS Access Key ID, Secret Access Key, and preferred region (e.g. `ap-south-1` for Mumbai).

(If you don't have AWS keys yet: AWS Console → your name (top right) → Security credentials → Create access key.)

## Deploy it — 2 commands

```bash
cd simple-lambda-api

# Step 1: package the code
sam build

# Step 2: deploy to AWS (asks a few simple questions the first time)
sam deploy --guided
```

When prompted, you can accept the defaults for everything except:
- **Stack Name** → type something like `simple-greeting-api`
- **AWS Region** → pick the one closest to you
- Everything else → press Enter to accept the default

At the end, SAM prints something like:
```
Key                 ApiUrl
Value                https://abc123xyz.execute-api.ap-south-1.amazonaws.com/Prod/hello
```
That URL is your live, working API.

## Test it

In your browser, just visit:
```
https://<your-api-url>?name=YourName
```

Or with curl:
```bash
curl "https://<your-api-url>?name=YourName"
```

## Clean up (so AWS doesn't keep the resources)

```bash
sam delete
```

## How to talk about this in an interview

- **"What does it do?"** → "It's a REST API with one endpoint. It takes a name and returns a greeting — built to learn the core serverless pattern: API Gateway routes a request to a Lambda function, which runs the code and returns a response."
- **"Why Lambda instead of a normal server?"** → "There's no server to keep running or patch. AWS only runs the code when a request comes in, and you're billed per request/millisecond, not for idle time."
- **"What's in the event object?"** → "API Gateway passes the whole HTTP request as a JSON object — I read `queryStringParameters` out of it to get the `name`."
- **"How did you deploy it?"** → "Using AWS SAM — I define the Lambda and the API route in one YAML file (`template.yaml`), and `sam deploy` provisions everything on AWS automatically. No manual clicking in the console."

## Resume bullet points (pick what applies)

> - Built and deployed a serverless REST API on AWS using Lambda (Python) and API Gateway, provisioned entirely through Infrastructure as Code (AWS SAM).
> - Learned and applied core serverless concepts: event-driven execution, pay-per-request pricing, and stateless function design.

## Natural next steps (good "what I'd add next" talking points)

- Add a second endpoint (e.g. `/goodbye`) to show you can extend the API.
- Connect it to a DynamoDB table to store and retrieve data (see the more advanced Task Management API version if you want to go further).
- Add input validation (e.g. reject empty names) and proper error responses.
- Write a simple unit test for the Lambda function using `pytest`.
