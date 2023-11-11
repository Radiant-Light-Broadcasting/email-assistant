source myenv/bin/activate

sudo FLASK_APP=~/Projects/email-assistant/email_classifying_web_service.py ~/Projects/email-assistant/myenv/bin/flask run --host=0.0.0.0 --port=80



zip -r email_classifier.zip aws_lambda_email_classifying.py svm_model.joblib count_vectorizer.joblib joblib
pause(10)
aws s3 cp email_classifier.zip s3://svm-lambda-email-classifier/email_classifier.zip
aws s3 cp email_classifier.zip s3://svm-lambda-email-classifier/layer.zip
pause(10)
aws lambda update-function-code --function-name svmEmailClassification --s3-bucket svm-lambda-email-classifier --s3-key email_classifier.zip
aws lambda publish-layer-version --layer-name joblib-layer --zip-file fileb://layer.zip --compatible-runtimes python3.8 --region us-east-1
