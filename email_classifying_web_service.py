from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

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
        return 'Label_6579016834950308909'
    else:
        prediction = model.predict(email_features)
        return prediction[0]

@app.route('/classify', methods=['POST'])
def classify_endpoint():
    email_text = request.json.get('email_text')
    if email_text:
        result = classify_email(email_text)
        return jsonify({'classification': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/classify_email', methods=['GET'])
def classify_email_get():
    email_text = request.args.get('email_text')
    if email_text:
        result = classify_email(email_text)
        return jsonify({'classification': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
