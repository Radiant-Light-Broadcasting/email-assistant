import sys
from email_training import train_email_model
from email_classifying import classify_email

if len(sys.argv) > 1:
    if sys.argv[1] == 'train':
        train_email_model()
    elif sys.argv[1] == 'classify':
        classify_email()
    else:
        print("Invalid argument. Use 'train' or 'classify'.")
else:
    print("Please provide an argument: 'train' or 'classify'.")
