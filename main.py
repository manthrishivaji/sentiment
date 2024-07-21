from transformers import pipeline

# Initialize the sentiment analysis pipeline
model = pipeline("sentiment-analysis")
#########################################
# # Get user input
# user_input = input("User: ")

# # Generate a response
# response = model(user_input)

# # Print the response
# print("Response:", response[0]['label'])
##################################################

print("Sentiment Analysis Chatbot")
print("Type 'quit' to exit.")

while True:
    # Get user input
    user_input = input("User: ")

    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        print("Exiting the chatbot. Goodbye!")
        break

    # Generate a response
    response = model(user_input)

    # Extract the label from the response
    sentiment_label = response[0]['label']

    # Print the sentiment in a simplified format
    print("Response:",sentiment_label)
