# PRODIGY_ML_02
# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Project Overview

This project applies **K-Means Clustering** to group customers based on their purchasing behavior.
The goal is to identify patterns in customer data and visualize distinct customer segments.

---

## 🎯 Problem Statement

Understanding customer behavior is important for businesses.
This project groups customers based on:

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

1. Load dataset
2. Select relevant features
3. Apply feature scaling (StandardScaler)
4. Use Elbow Method to determine optimal clusters
5. Apply K-Means Clustering
6. Visualize the clusters

---

## 📉 Elbow Method

The Elbow Method is used to find the optimal number of clusters.
Based on the graph, **K = 5** is selected.

---

## 🤖 Model Used

* K-Means Clustering (Unsupervised Learning)

---

## 📈 Results

* Customers are grouped into 5 clusters
* Each cluster represents a group with similar income and spending behavior
* Clusters are visualized using a scatter plot

---

## 🧠 Insights

* Different customer groups can be observed visually
* Cluster interpretation (e.g., high spenders, low spenders) is done based on feature values

---

## 🖼️ Visualizations

* Elbow Method Graph
* Customer Segmentation Plot

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

This project demonstrates how clustering can be used to group customers and visualize patterns in data. It highlights the importance of data-driven approaches in understanding customer behavior.

---

## 👨‍💻 Author

Shashank Sharma
