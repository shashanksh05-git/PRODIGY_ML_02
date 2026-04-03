from sklearn.cluster import KMeans

def train_kmeans(X_scaled, k=5):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_scaled)
    return model

def predict(model, X_scaled):
    return model.predict(X_scaled)