# Resume and Job Description Matching Application

This project is a backend service designed to match resumes with job descriptions using a Large Language Model (LLM). The application parses uploaded resumes to extract key details and skills, then uses an LLM to compute a similarity score between the extracted resume details and the provided job descriptions. 

## Features

- Upload resumes and parse them to extract skills and a summary.
- Store resumes in AWS S3.
- Use LangChain and Llama 2 (via Ollama) for generating similarity scores.
- MongoDB as the database backend, running in a Docker container.
- GitHub Actions for CI/CD pipelines and Docker Hub integration.
- Multi-container Docker setup for production-ready deployment.

## Tech Stack

- **Programming Language**: Python(FastAPI)
- **Database**: MongoDB (Dockerized)
- **Cloud Storage**: AWS S3
- **Model**: Llama 2 using Ollama
- **Frameworks**: LangChain
- **CI/CD**: GitHub Actions
- **Containerization**: Docker

## Prerequisites

1. **Python**: Install Python 3.8 or higher.
2. **Docker**: Install Docker and Docker Compose.
3. **AWS**: Set up an AWS account and an S3 bucket for storing resumes.
4. **Ollama**: Set up and configure Ollama to run the Llama 2 model locally.
5. **MongoDB**: Install Docker Compose to run MongoDB as a container.

## Setup

### 2. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
S3_BUCKET_NAME=your_s3_bucket_name
```

### 3. Install Dependencies

```bash
$ pip install -r requirements.txt
```

### 4. Start MongoDB Container

```bash
$ docker-compose up -d
```


### 5. Test with Postman

Use Postman to interact with the API. Upload resumes, parse them, and retrieve similarity scores.

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment. Every push to the repository:

- Builds and tests the Docker image.
- Pushes the updated image to Docker Hub.



## Future Improvements

- Add support for multi-language resumes.
- Implement advanced analytics for skill matching.
- Extend the application with a frontend for better user interaction.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


