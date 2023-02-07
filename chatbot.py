import openai
import os
import questionary

# Set the OpenAI API key
openai.api_key = os.getenv("API_KEY", default=None)

def write_to_file(data, x = "a"):
    with open("chatbot_data.txt", x) as f:
        f.write(data)

def generate_response(prompt):
    # Use OpenAI's gpt-3 model to generate a response
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5).choices[0].text
    return response

def start_conversation(user_input):
    # Process user input and generate response
    response = generate_response(user_input)

    # Write response to file
    write_to_file(response)

    # Print response
    print(response)
def chat_bot():
    # Use questionary to prompt the user for input
    user_input = questionary.text("What do you want today? :").ask()
    while True:
        start_conversation(user_input)
        # Use questionary to prompt the user for input
        user_input = questionary.text("Do you want to ask anything else? :").ask()
        if user_input.lower() in ['no', 'n', 'done', 'nope', 'are you a fool no!']:
            write_to_file("", 'w')
chat_bot()