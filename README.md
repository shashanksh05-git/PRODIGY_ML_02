# PRODIGY_ML_02
# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Project Overview

This project focuses on segmenting customers based on their purchasing behavior using **K-Means Clustering**.
The goal is to identify distinct customer groups to help businesses make data-driven marketing decisions.

---

## 🎯 Problem Statement

Businesses often struggle to understand their customers.
This project solves that by grouping customers based on:

* Annual Income
* Spending Score

---

## 📊 Dataset

* Mall Customers Dataset
* Features used:

  * Annual Income (k$)
  * Spending Score (1-100)

---

## ⚙️ Approach

1. Data Loading and Cleaning
2. Feature Selection
3. Feature Scaling using StandardScaler
4. Finding optimal clusters using Elbow Method
5. Applying K-Means Clustering
6. Visualizing customer segments

---

## 📉 Elbow Method

Used to determine the optimal number of clusters (K).
The graph shows a clear bend at **K = 5**, which is selected for the model.

---

## 🤖 Model Used

* K-Means Clustering (Unsupervised Learning)

---

## 📈 Results & Insights

The model segmented customers into 5 distinct groups:

* 💰 High Income, High Spending → Target customers
* 📉 Low Income, Low Spending → Low priority
* ⚖️ Medium Income, Medium Spending → Regular customers
* 💡 High Income, Low Spending → Potential customers
* 🛍️ Low Income, High Spending → Impulsive buyers

---

## 🖼️ Visualizations

* Elbow Method Graph
* Customer Segmentation Scatter Plot

---

## 🚀 How to Run

```bash
git clone <your-repo-link>
cd customer-segmentation-kmeans
pip install -r requirements.txt
python main.py
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

## 🙌 Conclusion

This project demonstrates how unsupervised learning can be used to extract meaningful insights from customer data and support business decision-making.

---

## 👨‍💻 Author

Shashank Sharma
