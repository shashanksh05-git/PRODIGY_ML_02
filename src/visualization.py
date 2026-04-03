import matplotlib.pyplot as plt

def plot_clusters(X, labels):
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels)
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segments")
    plt.show()