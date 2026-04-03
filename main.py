from src.preprocessing import load_data, preprocess_data
from src.model import train_kmeans, predict
from src.evaluation import elbow_method
from src.visualization import plot_clusters

# Step 1: Load data
df = load_data(r"C:\Customer Segmentation\data\Mall_Customers.csv")

# Step 2: Preprocess
X, X_scaled, scaler = preprocess_data(df)

# Step 3: Find best K (optional)
elbow_method(X_scaled)

# Step 4: Train model
model = train_kmeans(X_scaled, k=5)

# Step 5: Predict clusters
labels = predict(model, X_scaled)

# Step 6: Visualize
plot_clusters(X, labels)