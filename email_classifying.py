import joblib
import argparse

def classify_email(email_text, threshold=0.6):
    # Load the model and the text conversion tool from disk
    model = joblib.load('svm_model.joblib')
    vectorizer  = joblib.load('count_vectorizer.joblib')

    # Convert the cleaned email text into numbers
    email_features = vectorizer.transform([email_text])

    # Use the model to predict the category of the email and get prediction probabilities
    prediction_proba = model.predict_proba(email_features)
    max_proba = max(prediction_proba[0])

    # If the highest probability is below the threshold, return 'other'
    if max_proba < threshold:
        return 'other'
    else:
        prediction = model.predict(email_features)
        return prediction[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classify an email text.')
    parser.add_argument('email_text', type=str, help='The email text to classify.')

    args = parser.parse_args()
    email_text = args.email_text

    # Classify the email and show the result
    result = classify_email(email_text)
    print(result)
