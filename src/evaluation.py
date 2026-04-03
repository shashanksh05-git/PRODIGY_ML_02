import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def elbow_method(X_scaled):
    inertia = []

    for k in range(1, 11):
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(X_scaled)
        inertia.append(model.inertia_)

    plt.plot(range(1, 11), inertia)
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.title("Elbow Method")
    plt.show()