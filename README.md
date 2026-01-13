# ⚽ TransferIQ  
## Dynamic Player Transfer Value Prediction using AI

TransferIQ is an end-to-end **machine learning system** that predicts the **market value of football players** by integrating **performance data, injury history, and public sentiment**.  
The goal is to make player valuation **objective, data-driven, and interpretable**, reducing reliance on subjective judgments.

---

## 📌 Problem Statement

Football player valuation is complex because:

- Player data is **scattered across multiple sources**
- Injury impact is often **ignored or underestimated**
- Public and media sentiment is rarely quantified
- Manual evaluation is **subjective and inconsistent**

**TransferIQ** addresses these challenges using AI and machine learning.

---

## 🎯 Project Objectives

- Integrate **multi-source football data** into a unified dataset  
- Engineer **business-relevant features**  
- Predict **player market value** using ML models  
- Build an **interpretable and optimized model**  
- Deploy the model via a web application  

---

## 🧠 System Architecture
Data Collection<br>
      ↓<br>Data Cleaning & Merging<br>
      ↓
<br>Feature Engineering<br>
      ↓
<br>EDA & Outlier Handling<br>
      ↓
<br>Model Training & Optimization<br>
      ↓
<br>Evaluation<br>
      ↓
<br>Deployment (Streamlit + FastAPI)<br>


---

## 📊 Data Sources

- **Player Profiles** – age, nationality, career information  
- **Match Performance** – goals, assists, minutes played  
- **Market Value History** – estimated transfer values  
- **Injury Records** – injury duration and frequency  
- **National Stats** – international experience  
- **Twitter Sentiment** – public and media perception  

---

## 🧹 Data Cleaning

- Converted date fields to **datetime format**
- Removed **player IDs and names** to prevent data leakage
- Handled missing values using **median imputation**
- Standardized numerical features
- One-hot encoded categorical features

---

## ⚙️ Feature Engineering

### 🔹 Basic Performance Features
- Age  
- Days Out (injury duration)  
- Goals per 90 minutes  
- Assists per 90 minutes  
- Goals + Assists per Match  

### 🔹 Advanced Features
- **Injury Impact Index** – injury severity combined with market value  
- **Value Efficiency Ratio** – performance relative to cost  
- **Log Injury Days** – reduced skewness in injury data  
- **Normalized Sentiment** – scaled public perception  

---

## 📈 Exploratory Data Analysis (EDA)

Key insights from EDA:
- Performance metrics strongly influence market value
- Forwards and midfielders command higher value
- Injury history affects long-term valuation
- Raw sentiment alone shows weak correlation

EDA guided feature selection and model choice.

---

## 🚨 Outlier Detection & Handling

- Outliers detected in:
  - Market value
  - Injury days
  - Performance metrics
- Used **IQR-based capping** instead of removal
- Preserved elite players while stabilizing model learning

---

## 🧠 Sentiment Feature Creation

- Processed Twitter data using **CountVectorizer**
- Generated **1000 sentiment features**
- Aggregated sentiment at **player level**
- Captured public perception beyond numerical statistics

---

## 🤖 Model Building

### Models Trained
- Linear Regression (baseline)
- Polynomial Regression (degree 1 & 2)
- Lasso Regression (overfitting control)
- Decision Tree Regressor ✅ (final model)
- Random Forest Regressor
- LightGBM Regressor

---

## 🔍 Data Leakage Handling

- Detected unrealistic performance (R² ≈ 1.0)
- Identified target leakage in features
- Removed leaked variables
- Rebuilt preprocessing pipeline
- Retrained models with clean data

---

## 🏆 Final Model Selection

**Decision Tree Regressor** was selected because:
- Captures non-linear relationships
- Highly interpretable
- Best performance after tuning

### 📊 Final Performance (Untouched Test Data)
- **R²:** 0.9842  
- **MAE:** 14,499  
- **RMSE:** 103,087  

---

## 🔧 Model Optimization

- Used **GridSearchCV** for hyperparameter tuning
- Tuned:
  - Tree depth
  - Split rules
- Improved generalization and model stability

---

## ⭐ Feature Importance

Top contributors to player market value:
- Age  
- Matches played  
- Goals & assists per 90  
- Injury Impact Index  
- Value Efficiency Ratio  
- Normalized sentiment  

---

## 🌐 Deployment

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- User inputs player details
- Model predicts market value in real time

---

## 🚀 Future Scope

- Live match and injury data integration
- Deep learning–based sentiment analysis
- Player comparison and transfer recommendations
- Cloud deployment for scalability
- Advanced dashboards and analytics

---

## 🧑‍💻 Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- NLP (CountVectorizer)  
- Streamlit  
- FastAPI  

---

## 🙌 Author

**Renu Kumari Prajapati**  
B.Tech IT | Machine Learning & Data Science  
Project: *TransferIQ – Dynamic Player Transfer Value Prediction*

