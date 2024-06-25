import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample election data (features: age, income, education; target: voted or not)
data = {
    'age': [25, 35, 45, 30, 50, 40, 55, 20],
    'income': [50000, 70000, 60000, 80000, 90000, 75000, 100000, 45000],
    'education': ['High School', 'College', 'College', 'High School', 'Graduate', 'College', 'Graduate', 'High School'],
    'voted': [1, 0, 1, 1, 0, 1, 0, 1]  # 1 for voted, 0 for not voted
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert categorical 'education' column to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['education'], drop_first=True)

# Split the data into features (X) and target variable (y)
X = df.drop('voted', axis=1)
y = df['voted']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(conf_matrix)

