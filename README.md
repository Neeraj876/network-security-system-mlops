# Network Security - Malicious URL Detection using MLOps

A comprehensive end-to-end MLOps project designed to detect malicious URLs using XGBoost, ensuring user safety by identifying harmful links through machine learning. By combining data ingestion, model training, deployment, and monitoring, it provides a complete solution for real-time and batch URL safety assessments.

## Introduction

Malicious URLs are links that lead to harmful websites, often used by cybercriminals through phishing emails, social engineering, and other tactics. This project detects malicious URLs using machine learning and provides both single URL predictions and batch predictions through an interactive UI.

## Architecture
![Architecture](https://github.com/user-attachments/assets/2f1b37a7-d64e-40f4-9750-42ec43dcc972)

## Tech Stack 🛠️

| Category         | Tools/Technologies    | Description                                                                 |
|------------------|-----------------------|-----------------------------------------------------------------------------|
| Frontend         | Streamlit             | Provides a simple UI for real-time single URL predictions                   |
| Backend          | FastAPI               | Handles batch predictions and API endpoints                                 |
| Modeling         | RandomForest, Python       | Machine learning model for detecting malicious URLs                         |
| Database         | MongoDB               | Stores data records for ingestion and model training                         |
| Orchestration    | Apache Airflow        | Orchestrates training, retraining, and batch prediction pipelines            |
| Experiment Tracking| MLflow               | Tracks model metrics like F1-score, Precision, and Recall                   |
| CI/CD            | GitHub Actions        | Automates CI/CD pipelines, including Docker build and deployment            |
| Containerization | Docker, AWS ECR       | Docker images stored securely in ECR for consistent deployment              |
| Cloud Storage    | AWS S3                | Stores artifacts, trained models, and logs                                  |
| Cloud Hosting    | AWS EC2 Instance      | Serves as a self-hosted runner for GitHub Actions                           |

# Project Highlights 🌟

## ML Pipeline & Monitoring

- **End-to-End MLOps Pipeline**  
  From data ingestion to deployment, ensuring seamless integration and automated workflows.

- **Real-time Single URL Predictions**  
  Users can instantly interact with the model via a **Streamlit** app for real-time safety assessments on individual URLs.

- **Batch Predictions for Large Datasets**  
  Efficiently process multiple URLs at once using **FastAPI**, designed for bulk predictions and high-throughput scenarios.

- **Automated Model Retraining**  
  Ensure that the model stays up-to-date with new data through an **Apache Airflow** powered retraining pipeline, running at scheduled intervals or triggered manually.

- **Comprehensive Metrics Tracking**  
  All experiments are logged and tracked with **MLflow** in **AWS**, providing a centralized dashboard to compare and monitor model performance and facilitate easy experimentation.

## Infrastructure & Deployment

- **Containerized with Docker**  
  The entire application is containerized using **Docker**, ensuring consistent environments from development to production.

- **Artifact & Model Storage**  
  Models, artifacts, and other intermediate data are securely stored in **AWS S3**, ready for deployment at any stage.

- **Scalable Cloud Deployment on AWS EC2**  
  Deployed on **AWS EC2 instances**, enabling scalable cloud infrastructure for reliable performance under varying loads.

- **Multiple Deployment Options**  
  - **FastAPI** for efficient API endpoints. It includes two routes:  
    - **/train** for training the model with existing data.  
    - **/predict** for making batch predictions (bulk predictions) on input data.
  - **Streamlit** for an interactive web interface, enabling easy user interaction with the model for real-time predictions.

## CI/CD & Version Control

- **Automated CI/CD Pipeline**  
  Streamline testing, validation, and deployment with a fully automated **GitHub Actions** pipeline, integrating with **AWS EC2** and **Amazon ECR**.
  - **Automated Testing & Validation** ensures code quality and reduces errors.
  - **Docker Image Build & Push** to **Amazon ECR**, ensuring that every deployment is consistent and traceable.
  - **Deployment to Production** in **AWS EC2** with automated rollbacks and fail-safes for zero-downtime deployments.

- **Version Control for Code and Data**  
  - **Code Versioning** via **Git** and **GitHub** ensures your codebase is always up-to-date.
  - **Data Versioning** with tools for **schema tracking** and **drift detection**, ensuring high data quality and maintaining model integrity over time.


## Components

### 1. Frontend (Streamlit)
The Streamlit app provides URL safety predictions:

- Safe URL Example:
![Streamlit Safe URL](https://github.com/user-attachments/assets/5ad92508-b587-4e93-b581-d83a8cc397ae)

- Malicious URL Example:
![Streamlit Malicious URL](https://github.com/user-attachments/assets/9aa17086-4295-4624-b2ad-249de47a1b44)

### 2. Backend (FastAPI)
FastAPI handles model operations and batch predictions:

- API Documentation:
![FastAPI Docs](https://github.com/user-attachments/assets/07b06b78-b089-40af-9499-b71c0cb196d7)

- Training Route:
![Training Route](https://github.com/user-attachments/assets/c86a5761-d256-4ab8-b0ef-4a043a7f7ef7)

- Training Execution:
![Training Execution](https://github.com/user-attachments/assets/3b0477f5-0446-4937-b125-8944412108af)

### 3. MLOps Pipeline

#### Data Ingestion
- MongoDB integration for data retrieval
- Data cleaning and feature store export
![MongoDB Data](https://github.com/user-attachments/assets/ff806462-7b17-48a3-bad1-cd6f2186a72c)

#### Model Training and Evaluation
- XGBoost Classifier implementation
- Performance metrics tracking with MLflow
![MLflow Metrics](https://github.com/user-attachments/assets/33bd60a6-41c5-4d28-9bb2-d3006db91070)
![Model Performance](https://github.com/user-attachments/assets/48722274-17b6-40b3-8ce9-1923b0523718)

### 4. AWS Integration

#### S3 Storage
- Centralized artifact and model storage
![S3 Bucket Overview](https://github.com/user-attachments/assets/a2c504a7-1564-481a-8002-e5ae572b9f22)
![S3 Structure](https://github.com/user-attachments/assets/49c4a703-0cb6-4c1f-a3dd-d02bbfad4886)
![Artifacts](https://github.com/user-attachments/assets/a8b04213-43eb-472e-82f9-91c95060484c)
![Saved Models](https://github.com/user-attachments/assets/ef5f9516-4396-4f61-b5f1-c6d0395161ea)

### 5. CI/CD Pipeline with GitHub Actions

- Self-Hosted Runner Setup:
![EC2 Runner](https://github.com/user-attachments/assets/eda98175-f802-44be-b651-a41c93ad9003)
![Runner Status](https://github.com/user-attachments/assets/c95d5408-0f9e-43ac-97a9-0c020e340582)

- Pipeline Stages:
  - Continuous Integration:
    ![CI Stage](https://github.com/user-attachments/assets/d778a287-794d-456f-a9b2-68ac3362ac20)
  - Continuous Delivery:
    ![CD Stage](https://github.com/user-attachments/assets/8058ce67-127e-4de6-ac81-a6368da9198b)
  - Deployment:
    ![Deployment](https://github.com/user-attachments/assets/6ff3eb07-0a97-4980-9112-d3c56c8d381e)

- Successful Pipeline Execution:
![CI/CD Complete](https://github.com/user-attachments/assets/9ad3f8c5-9b85-4d89-8bf3-3662bbca22f1)

### 6. Docker Integration
- ECR Image Management
![Docker ECR](https://github.com/user-attachments/assets/50e4b4ac-0487-45df-91a7-d192b0b146ed)

### 7. Airflow Integration

- Airflow Login:
![Login](https://github.com/user-attachments/assets/7c8acf28-c723-4ea0-b92d-767357d3c0cf)
![Dashboard](https://github.com/user-attachments/assets/0d646c31-62e6-4597-b6c8-96652f94fc53)

- DAGs:
  - Network Prediction DAG:
    ![Prediction DAG](https://github.com/user-attachments/assets/94e497fe-9ffa-4c12-9dd8-ae57f833ffd3)
  - Network Training DAG:
    ![Training DAG](https://github.com/user-attachments/assets/974bfab6-2ff8-4efb-b3aa-8aa648451756)

- DAG Overview:
![DAGs List](https://github.com/user-attachments/assets/bb81b358-1f99-489e-83c6-b048eb0b4ebb)

- DAG Execution:
![DAG Running](https://github.com/user-attachments/assets/9d377e8d-dd74-476d-ac2e-1f7fbfca2443)

## Dataset and Features

![URL Features](https://github.com/user-attachments/assets/b31f05db-528b-452c-a97e-0aa64319dcce)

The dataset contains 30 features extracted from URLs to classify them as Malicious or Safe.

### Key Features

| Feature Name           | Description                                                            |
|------------------------|------------------------------------------------------------------------|
| `having_IP_Address`     | Checks if URL contains IP address instead of domain name               |
| `URL_Length`            | Measures URL length; longer URLs often hide malicious content          |
| `Shortening_Service`    | Detects use of URL shortening services like `bit.ly`                    |
| `having_At_Symbol`      | Flags presence of '@' in URL                                           |
| `double_slash_redirecting` | Identifies multiple slashes after protocol                            |

<details>
<summary>Click here to view all features</summary>

| Feature Name           | Description                                                            |
|------------------------|------------------------------------------------------------------------|
| `Prefix_Suffix`         | Checks for dashes in domain                                            |
| `having_Sub_Domain`     | Counts number of subdomains                                             |
| `SSLfinal_State`        | Analyzes SSL certificate                                               |
| `Domain_registration_length` | Measures domain registration duration                               |
| `Favicon`               | Checks favicon source                                                  |
| `port`                  | Detects unusual ports                                                  |
| `HTTPS_token`           | Flags 'HTTPS' in domain name                                           |
| `Request_URL`           | Checks resource loading domains                                        |
| `URL_of_Anchor`         | Analyzes anchor tag destinations                                       |
| `Links_in_tags`         | Measures links in HTML tags                                            |
| `SFH`                   | Checks form handler locations                                          |
| `Submitting_to_email`   | Flags form submission to email                                         |
| `Abnormal_URL`          | Identifies URL-domain mismatches                                       |
| `Redirect`              | Counts redirections                                                     |
| `on_mouseover`          | Detects JavaScript events                                              |
| `RightClick`            | Identifies right-click disabling                                        |
| `popUpWindow`           | Flags popup windows                                                    |
| `Iframe`                | Detects invisible iframes                                              |
| `age_of_domain`         | Analyzes domain age                                                    |
| `DNSRecord`             | Checks DNS records                                                     |
| `web_traffic`           | Measures website traffic                                               |
| `Page_Rank`             | Checks page rank                                                        |
| `Google_Index`          | Identifies Google indexing                                              |
| `Links_pointing_to_page`| Counts inbound links                                                    |
| `Statistical_report`    | Flags reported suspicious activity                                     |

</details>

---

## **How to Run the Project** 🚀

This section provides a step-by-step guide on how to set up and run the Malicious URL Detection project both locally and in a deployed environment.

### **Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/malicious-url-detection.git
   cd malicious-url-detection
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### **Local Setup**

1. **Start the Streamlit App:**
   - Launch the user interface for **single URL prediction**.
   ```bash
   streamlit run app.py
   ```
2. **Run the FastAPI Backend:**
   - Start the API for handling **batch predictions**.
   ```bash
   uvicorn main:app --reload
   ```

### **Deployment**

1. **Build and Push Docker Image:**
   - Build the Docker image and push it to **AWS ECR**.
   ```bash
   docker build -t your-docker-image .
   docker tag your-docker-image:latest <AWS_ECR_URI>
   docker push <AWS_ECR_URI>
   ```
2. **Run Docker Container on EC2 Instance:**
   - Start the **AWS EC2** instance and run the container.
   ```bash
   docker run -d -p 80:80 your-docker-image
   ```

### **Running the Project Components**

1. **Data Ingestion:**
   - Start by fetching data from **MongoDB** using the `data_ingestion` module.

2. **Pipeline Execution:**
   - Use **Airflow DAGs** (`network_training_dag.py` and `network_prediction_dag.py`) to orchestrate data ingestion, training, and prediction.

3. **Batch Prediction:**
   - Run the **FastAPI** server and use the `/predict` route to upload a CSV file and receive predictions in **JSON** format.

4. **Single Prediction:**
   - Launch the **Streamlit** app for real-time prediction of a single URL.

5. **Monitoring:**
   - Track all experiments, model metrics (e.g., F1-score, Precision), and logs via the **MLflow UI**.

---

