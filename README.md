# MLOPs-Production-Ready-Machine-Learning-Project

#### Note: I am hiding all my personal credentials. If you are following my repository, please replace the dummy credentials with your actual credentials.

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login
- Data link: https://www.kaggle.com/datasets/moro23/easyvisa-dataset


## Git commands

```bash
git add .
```

```bash
git commit -m "Updated"
```

```bash
git push origin main
```


## How to run?

1. Craete virtual environment in VS Code terminal
```bash
python -m venv venv
```

2. Activate the virtual environment
```bash
venv\Scripts\activate
```

3. Install the required packages in the virtual environment
```bash
pip install -r requirements.txt
```

## Workflow:

1. constants
2. entity
3. components
4. pipeline
5. Main file



### Export the  environment variable
```bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."
```

```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
```

```bash
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```
### Alternatively, you can create a .env file and mention all the credentials and import it in your code. Please note that the .env file should be updated in the .gitignore file for secure your credentials.



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/visarepo

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO

    

