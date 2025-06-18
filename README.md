title: Predictive Maintenance for Turbofan Engines emoji: ✈️ colorFrom: blue colorTo: indigo sdk: gradio sdk_version: 4.20.0 app_file: app.py pinned: false

Predictive Maintenance for Turbofan Engines
A complete MLOps project demonstrating an end-to-end workflow for a predictive maintenance solution. This application uses a machine learning model to predict the Remaining Useful Life (RUL) of a turbofan engine based on operational settings and sensor data.

The project is developed within a containerized GitHub Codespaces environment and features a CI/CD pipeline that automatically trains the model and deploys the application to a Hugging Face Space.

✨ Features
Interactive Demo: A user-friendly Gradio web interface to get real-time RUL predictions.

Automated CI/CD: The model is automatically retrained and the application is redeployed on every push to the main branch using GitHub Actions.

Reproducible Environment: A defined development environment using Codespaces ensures that the project can be run consistently by anyone.

Extensible Framework: While this demo uses a turbofan engine dataset, the principles can be customized for any machinery that relies on sensor data to predict performance or potential faults.

🛠️ Technology Stack
Backend: Python

ML Model: Scikit-learn (Linear Regression)

Web App: Gradio

Dev Environment: GitHub Codespaces (Docker)

CI/CD & Hosting: GitHub Actions, Hugging Face Spaces

🚀 How to Run Locally
To run this project on your own machine or Codespace, follow these steps.

Prerequisites
Python 3.9 or higher

Git

1. Clone the Repository
git clone [https://github.com/ashandilgith/predictivemaintenance-.git](https://github.com/ashandilgith/predictivemaintenance-.git)
cd predictivemaintenance-

2. Set Up a Virtual Environment (Recommended)
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

3. Install Dependencies
Install all the required Python libraries from the requirements.txt file.

pip install -r requirements.txt

4. Prepare the Data
Run the script to process the raw dataset. This will create processed_train_data.csv in the data/ directory.

python prepare_data.py

5. Train the Model
Run the training script to create the model.joblib file.

python train.py

6. Launch the Gradio App
Run the application file. The app will be available at a local URL shown in your terminal.

python app.py

⚙️ CI/CD Pipeline
This project uses a GitHub Actions workflow defined in .github/workflows/main.yml. The pipeline automates the following steps on every push to the main branch:

Checkout Code: Clones the repository onto a fresh virtual machine.

Install Dependencies: Installs all necessary libraries.

Prepare Data: Runs the data preparation script.

Train Model: Trains the linear model and creates the model.joblib artifact.

Deploy to Space: Pushes the entire application, including the newly trained model, to the designated Hugging Face Space, making the updated app live.

📊 Dataset
This project uses the Turbofan Engine Degradation Simulation Data Set provided by NASA.

Source: NASA Prognostics Data Repository

Subset Used: FD001