# AI-based-user-risk-detection-system
---
Overview

This project is built around a simple but important idea — not all online behavior is safe, and small habits can sometimes lead to bigger risks. The system looks at basic user activities like password strength, login attempts, and interaction with unknown links, and tries to identify whether a user’s behavior falls into a safe or risky category.

Instead of just it as a theoretical concept, the project turns it into a working model using machine learning. The aim is to show how classroom concepts can actually be used to solve a real-world problem related to digital safety.

---

Problem Statement

Many users unknowingly follow unsafe practices online, such as using weak passwords or clicking suspicious links. These actions increase the chances of data theft, hacking, or fraud. The problem is to identify such risky behavior early and classify users accordingly so that preventive steps can be taken.

---
Objective

The main objective of this project is to build a system that can:

1. Analyze user activity data
2. Learn patterns from existing examples
3. Predict whether a user is safe or risky

---

How the System Works

The system follows a clear step-by-step process:

1. The dataset is loaded, which contains information about user behavior
2. Relevant features are selected (like password strength, failed logins, etc.)
3. The data is divided into training and testing parts
4. A machine learning model is trained using the training data
5. The model is tested on unseen data to check its performance
6. Finally, the system can take a new user’s data and predict their risk level

---
Machine Learning Approach

This project uses supervised learning, where the model learns from already labeled data.

The algorithm used is Logistic Regression, which is suitable for classification problems. It works by estimating the probability of a user being in a particular class (safe or risky) based on input features.

---

Features Used

The prediction is based on the following user attributes:

1. Password strength
2. Number of unknown links clicked
3. Failed login attempts
4. Use of public WiFi
5. Downloading unknown files

These features were selected because they directly relate to common unsafe digital practices.

---

Output

The system provides:

1. Model accuracy
2. Confusion matrix (to evaluate performance)
3. Prediction for a new user (Safe / Risky)

---
Data Visualization

To better understand the dataset, simple graphs are used:

1. Histogram to show password strength distribution
2. Bar graph to compare safe and risky users
3. Scatter plot to observe relation between link clicks and risk

These visualizations help in understanding patterns before and after model training.

---

Project Structure


project/
|    │── main.py        
|    │── model.py       
|    │── train.py      
|    │── user_data.csv 
|    │── README.md     
|───Output Screenshots
---

How to Run the Project

1. Install required libraries:

   ```
   pip install pandas scikit-learn matplotlib
   ```

2. Make sure all files are in the same folder

3. Run the program:

   ```
   python main.py
   ```

---

Code

---
main.py
---
from model import train_model, predict_user

model, X_test, y_test = train_model()

new_user = [[6, 3, 2, 1, 0]]
result = predict_user(model, new_user)

print("Prediction for new user:")
print("Risky" if result == 1 else "Safe")

---
model.py
---
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def train_model():
    data = pd.read_csv("user_data.csv")
    
    import matplotlib.pyplot as plt

    plt.hist(data['password_strength'])
    plt.title("Password Strength Distribution")
    plt.xlabel("Strength")
    plt.ylabel("Users")
    plt.show()

    data['risk_label'].value_counts().plot(kind='bar')
    plt.title("Safe vs Risky Users")
    plt.xlabel("Risk Label")
    plt.ylabel("Count")
    plt.show()

    plt.scatter(data['clicks_unknown_links'], data['risk_label'])
    plt.title("Unknown Links vs Risk")
    plt.xlabel("Clicks on Unknown Links")
    plt.ylabel("Risk")
    plt.show()
    X = data.drop(["risk_label", "user_id"], axis=1)
    y = data["risk_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:", confusion_matrix(y_test, y_pred))

    return model, X_test, y_test


def predict_user(model, user_data):
    return model.predict(user_data)[0]

---
train.py
---
from model import train_model

if __name__ == "__main__":
    print("Training the model...")
    model, X_test, y_test = train_model()
    print("Model training completed successfully!")

---
use_data.csv
---
user_id,password_strength,clicks_unknown_links,time_on_social_media,failed_logins,downloads_unknown_files,risk_label
1,2,5,6,3,1,1
2,8,0,2,0,0,0
3,3,4,7,2,1,1
4,6,1,3,0,0,0
5,1,6,8,4,2,1
6,7,0,2,0,0,0
7,4,3,5,1,1,1
8,9,0,1,0,0,0
9,2,7,9,5,3,1
10,6,1,4,1,0,0
11,3,5,6,2,1,1
12,8,0,3,0,0,0
13,2,6,7,3,2,1
14,7,1,2,0,0,0
15,5,2,4,1,0,0
16,1,8,9,6,3,1
17,9,0,1,0,0,0
18,4,4,6,2,1,1
19,6,1,3,0,0,0
20,2,7,8,4,2,1

---

Applications

This project can be extended or used in:

1. Cybersecurity systems
2. Fraud detection platforms
3. User behavior monitoring tools
4. Awareness tools for safe internet usage

---

Limitations

1. The dataset is small and simplified
2. Only basic features are considered
3. Real-world systems would require more complex data

---

Learning Outcome

Working on this project helped in understanding how machine learning actually works beyond theory. Concepts like training a model, testing accuracy, and making predictions became much clearer after implementing them practically.

It also showed that even a simple model can be useful when applied to the right problem.

---

Conclusion

This project demonstrates how machine learning can be used to identify risky user behavior in a simple and understandable way. It connects theoretical concepts with practical implementation and highlights the importance of safe digital practices.

---

Final Note

This project is a small step towards understanding how data and machine learning can contribute to solving real-world problems. The focus was kept on clarity, simplicity, and practical application rather than complexity.

