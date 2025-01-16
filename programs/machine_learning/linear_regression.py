from sklearn.datasets import load_wine
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
wine = load_wine()

# Extract the data from wine variable
data = wine.data

# Turn data into a pandas DataFrame
df = pd.DataFrame(data)
df.columns = wine.feature_names

#esto no estaba ahí, lo voy a quitar df["grape"] = wine.target.astype("str")

#print(df.head())

# Select the features you will use.
# Tip: features should be a list of strings.

features = ["alcohol", "alcalinity_of_ash", "magnesium"]
df = df[features]

df["grape"] = wine.target.astype("str")

# Plot the data
# Tip: set parameter color="grape"
#fig = # Your code here
fig = px.scatter(df, x="alcalinity_of_ash", y="alcohol", color="grape", size="magnesium", color_discrete_sequence=px.colors.qualitative.D3)

#this will be shown as html file
fig.show()

# Split the data into features and target
X_wine, y_wine = df[features], wine.target
X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine, y_wine, test_size=0.2, random_state=42) # Your code here

# Use a logistic regression model
logreg = LogisticRegression(max_iter=5000)
# Fit the model
logreg.fit(X_train_wine, y_train_wine)

# Evaluate the model
wine_predictions = logreg.predict(X_test_wine)
wine_accuracy = accuracy_score(y_test_wine, wine_predictions)
print(f"wine Logistic Regression Accuracy: {wine_accuracy}")

# Calculate confusion matrix
cm = confusion_matrix(y_test_wine, wine_predictions)

# Create a DataFrame for confusion matrix
classes = ["Cabernet Sauvignon", "Merlot", "Malbec"]
# Alternative less describing class names:
# classes = wine.target_names
df_cm = pd.DataFrame(cm, index=classes, columns=classes)

# Visualize confusion matrix using Plotly Express
fig = px.imshow(df_cm, labels=dict(x="Predicted Class", y="True Class", color="Count"),
                x=classes, y=classes, color_continuous_scale="Blues", title="Confusion Matrix")
fig.update_layout(title="Confusion Matrix", xaxis_title="Predicted Class", yaxis_title="True Class")
fig.show()