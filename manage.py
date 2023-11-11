import sys

def main():
    if len(sys.argv) != 2:
        print("Please provide an argument: 'train' or 'classify'.")
        return
    
    action = sys.argv[1]
    
    if action == 'train':
        from email_training import train_email_model
        train_email_model()
    elif action == 'classify':
        from email_classifying import classify_email
        classify_email()
    else:
        print("Invalid argument. Please use 'train' or 'classify'.")

if __name__ == '__main__':
    main()
