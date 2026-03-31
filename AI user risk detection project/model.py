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