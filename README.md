# Churn Analysis and Retention Offers App

This repository contains a project that predicts customer churn using machine learning and generates personalized retention offers. The project demonstrates the practical use of data analysis, machine learning, and business intelligence to address customer retention challenges in industries such as banking and retail.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)

## Introduction

Customer churn is a significant concern for businesses as it directly impacts revenue. This project uses machine learning to predict which customers are likely to churn and provides actionable recommendations through tailored retention offers.

The application is powered by:
- A **machine learning model** for churn prediction.
- A **Streamlit-based web app** for interactive predictions.
- A **Power BI dashboard** for visual insights into customer churn trends.

---

## Features

- **Churn Prediction**: Predict the likelihood of customer churn using a trained machine learning model.
- **Retention Strategies**: Generate personalized offers to retain high-value customers.
- **Data Visualization**: Analyze churn trends and customer behavior through a Power BI dashboard.
- **Interactive Interface**: User-friendly Streamlit app for real-time predictions.

---

## Project Structure

```plaintext
Churn-Analysis/
├── app.py                  # Streamlit app for predictions
├── Churn_Analysis.ipynb    # Jupyter notebook for data analysis and model training
├── Churn_Analysis.pbix     # Power BI dashboard file
├── scaler.pkl              # Pre-trained scaler for feature normalization
├── churn_predict_model     # Trained machine learning model
├── requirements.txt        # Dependencies for the project
├── README.md               # Documentation
└── Churn_Modelling.csv     # Dataset used for analysis
