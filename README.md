# TAKE HOME TEST

## Task 1:
- We have the Dockerfile and a requirement.txt file to manage all the necessary dependencies. 
- Build the Docker image using the following command: docker build -t my-python-app .
- Run the Docker container using the following command: docker run -p 8080:8080 my-python-app
- Now, you can access your Python web application by opening a web browser and navigating to http://localhost:8080. You should see the "Hello World!" message displayed by your Flask application.

## Task 2:
- For this task, we have created a Python script “monitor-resources.py” to monitor server resources (CPU, memory, disk space) and send an alert if these resources exceed a predefined threshold.
- We also have a configuration file “config.json”  where users can define the necessary parameters such as email configurations and threshold values.

## Task 3:
- For this task, we have created a Terraform module “main.tf” to automate infrastructure provisioning on AWS Cloud.

## Task 4:
- For this task, we have configured a Jenkinsfile defining the steps for our pipeline and configuring the Jenkins web interface to create a new pipeline and configure it to use the Jenkinsfile from the GitHub repository.
- ![image](https://github.com/DhairyaC19/Home-test/assets/162068944/df89e07f-3ae1-4cd0-abed-a6ea23b3e403)


## Task 5:
- For this task, we have created a Python script “backup_restore.py” to automate the backup of the MySQL database and its periodic restoration for testing purposes.
