from model import train_model, predict_user

model, X_test, y_test = train_model()

new_user = [[6, 3, 2, 1, 0]]
result = predict_user(model, new_user)

print("Prediction for new user:")
print("Risky" if result == 1 else "Safe")