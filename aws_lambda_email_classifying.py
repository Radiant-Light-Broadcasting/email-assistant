import joblib
import json

def lambda_handler(event, context):
    email_text = event['body']['email_text']
    threshold = 0.6

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
        return {
            'statusCode': 200,
            'body': json.dumps('other')
        }
    else:
        prediction = model.predict(email_features)
        return {
            'statusCode': 200,
            'body': json.dumps(prediction[0])
        }
