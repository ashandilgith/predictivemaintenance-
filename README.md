title: Predictive Maintenance for Turbofan Engines emoji: ✈️ colorFrom: blue colorTo: indigo sdk: gradio app_file: app.py pinned: false
Predictive Maintenance for Turbofan Engines
A complete MLOps project demonstrating an end-to-end workflow for a predictive maintenance solution. This application uses a machine learning model to predict the Remaining Useful Life (RUL) of a turbofan engine based on operational settings and sensor data.

The project is developed within a containerized GitHub Codespaces environment and features a CI/CD pipeline that automatically trains the model and deploys the application to this Hugging Face Space.

✨ Features
Interactive Demo: A user-friendly Gradio web interface to get real-time RUL predictions.

Automated CI/CD: The model is automatically retrained and the application is redeployed on every push to the main branch using GitHub Actions.

Reproducible Environment: A defined development environment using Codespaces ensures that the project can be run consistently by anyone.

⚙️ How It Works
This application is powered by a scikit-learn Linear Regression model trained on the NASA Turbofan Engine Degradation Simulation Data Set.

The CI/CD pipeline automates the following steps:

Prepare Data: Processes the raw dataset.

Train Model: Trains the linear model and creates a model.joblib artifact.

Deploy to Space: Pushes the entire application, including the newly trained model and this README, to this Hugging Face Space to make the app live.