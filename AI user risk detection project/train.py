from model import train_model

if __name__ == "__main__":
    print("Training the model...")
    model, X_test, y_test = train_model()
    print("Model training completed successfully!")