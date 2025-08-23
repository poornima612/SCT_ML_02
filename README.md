
🛒 Customer Segmentation using K-Means Clustering

This project demonstrates how to use **K-Means clustering** to group customers of a retail store based on their purchase history. By segmenting customers, businesses can better understand shopping behavior, identify high-value groups, and design targeted marketing strategies.

📊 Dataset

The sample dataset (`retail_customers.csv`) contains the following columns:

* **CustomerID** → Unique identifier for each customer
* **Annual\_Income** → Customer’s yearly income (in thousands)
* **Spending\_Score** → A score assigned based on customer spending behavior (1–100)

⚙️ Workflow

1. Load the dataset using **pandas**
2. Standardize features with **StandardScaler**
3. Apply **K-Means clustering** to group customers
4. Visualize clusters with **matplotlib**

🚀 Technologies Used

* Python 🐍
* pandas
* scikit-learn
* matplotlib

📌 Example Output

The clustering model divides customers into distinct groups, visualized on a scatter plot of **Annual Income vs Spending Score**.

💡 Future Enhancements

* Add more features (purchase frequency, product categories, recency)
* Use the **elbow method** or **silhouette score** to determine the optimal number of clusters
* Deploy as a web app with **Streamlit** or **Flask**
