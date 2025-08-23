Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import matplotlib.pyplot as plt
... from sklearn.cluster import KMeans
... from sklearn.preprocessing import StandardScaler
... 
... # Sample dataset (replace with your purchase history data)
... # Example: CustomerID, Annual Income, Spending Score
... data = {
...     "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
...     "Annual_Income": [15, 16, 17, 18, 20, 80, 85, 86, 87, 90],
...     "Spending_Score": [39, 81, 6, 77, 40, 76, 94, 3, 72, 10]
... }
... 
... df = pd.DataFrame(data)
... 
... # Select features for clustering
... X = df[["Annual_Income", "Spending_Score"]]
... 
... # Scale features
... scaler = StandardScaler()
... X_scaled = scaler.fit_transform(X)
... 
... # Apply KMeans
... kmeans = KMeans(n_clusters=3, random_state=42)
... df["Cluster"] = kmeans.fit_predict(X_scaled)
... 
... print(df)
... 
... # Plot Clusters
... plt.figure(figsize=(8,6))
... plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"], cmap="viridis", s=100)
... plt.xlabel("Annual Income (k$)")
... plt.ylabel("Spending Score (1-100)")
... plt.title("Customer Segmentation using K-Means")
... plt.show()
