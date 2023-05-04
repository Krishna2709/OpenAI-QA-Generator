# :robot: OpenAI-QA-Generator
Generates questions and answers from the passage provided by the user. <br>
:point_right:<b>QA-Generator: </b>  https://chatgpt-translator-2b3f3.web.app

### ℹ️ Project Descripton: 
  - Q&A generator web app powered by OpenAIs ChatGPT, built on Streamlit and deployed on Google Cloud

### 🖥️ Setup
1. Install the required libraries
```
pip install -r requirements.txt
```
2. Create an OpenAI account and generate API key
3. Create an .env file to store the API key
4. Modify the inputs and prompt according to the usage
5. Deploy the app on Google Cloud (need to install GCloud SDK: https://cloud.google.com/sdk/docs/install)
  
  :point_right: login
  ```
  gcloud auth login
  ```
  :point_right: initialize (create/select a project)
  ```
  gcloud inti
  ```
  :point_right: build a container (need Docker)
  ```
  gcloud builds submit --tag gcr.io/<project-id>/<docker-container-name>
  ```
  :point_right: deploy the container
  ```
  gcloud run deploy --image gcr.io/<project-id>/<docker-container-name> --set-env-vars "Key=Value"
  ```
  
  🥳 Congratulations 👏
