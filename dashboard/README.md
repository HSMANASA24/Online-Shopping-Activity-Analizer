# 🛒 Real-Time E-commerce Analytics using Kafka

## 🚀 Overview

This project analyzes online shopping activity in real-time using Apache Kafka.

## 🧠 Architecture

Producer → Kafka → Processor → MongoDB → FastAPI → React Dashboard

## ⚙️ Tech Stack

* Apache Kafka
* MongoDB
* FastAPI
* React

## 📦 Setup Instructions

### 1. Start Kafka & MongoDB

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run project

Terminal 1:
python producer/producer.py

Terminal 2:
python processor/analytics.py

Terminal 3:
cd api
uvicorn app:app --reload

Terminal 4:
cd dashboard
npm start

## 📊 Features

* Real-time analytics
* Live dashboard
* Event streaming

## 🔥 Future Scope

* Recommendation system
* Fraud detection
* AI analytics

