---
title: Predictive Maintenance for Turbofan Engines
emoji: ✈️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.25.0
app_file: app.py
pinned: false
---

# Predictive Maintenance for Turbofan Engines

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/ashandilgith/predictive_maintenance)
[![CI/CD Status](https://github.com/ashandilgith/predictivemaintenance-/actions/workflows/main.yml/badge.svg)](https://github.com/ashandilgith/predictivemaintenance-/actions)

A complete MLOps project demonstrating an end-to-end workflow for a predictive maintenance solution. This application uses a machine learning model to predict the Remaining Useful Life (RUL) of a turbofan engine based on operational settings and sensor data.

The project is developed within a containerized GitHub Codespaces environment and features a CI/CD pipeline that automatically trains the model and deploys the application to this Hugging Face Space.

## ✨ Features

- **Interactive Demo:** A user-friendly Gradio web interface to get real-time RUL predictions.
- **Automated CI/CD:** The model is automatically retrained and the application is redeployed on every push to the `main` branch using GitHub Actions.
- **Reproducible Environment:** A defined development environment using Codespaces ensures that the project can be run consistently by anyone.
- **Extensible Framework:** While this demo uses a turbofan engine dataset, the principles can be customized for any machinery that relies on sensor data to predict performance or potential faults.

## 🛠️ Technology Stack

- **Backend:** Python
- **ML Model:** Scikit-learn (Linear Regression)
- **Web App:** Gradio
- **Dev Environment:** GitHub Codespaces (Docker)
- **CI/CD & Hosting:** GitHub Actions, Hugging Face Spaces

## 🚀 How to Run Locally

To run this project on your own machine or Codespace, follow these steps.

### Prerequisites

- Python 3.9 or higher
- Git

### 1. Clone the Repository

```bash
git clone [https://github.com/ashandilgith/predictivemaintenance-.git](https://github.com/ashandilgith/predictivemaintenance-.git)
cd predictivemaintenance-