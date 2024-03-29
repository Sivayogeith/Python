import json
import requests
import random

def downloadImageFromUrl(url):
    # Send a request to the URL
    response = requests.get(url)

    random_number = random.randint(100, 10000)
    filename = f"images/image_{random_number}.jpg"

    # Check if the request was successful
    if response.status_code == 200:
        # Save the image
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved as {filename}!")
    else:
        print("Failed to download image")

def invokeOpenAiAPI(keywords):
    # Set the API key

    api_key = "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"
    if not api_key:
        raise Exception("api key is: " + str(api_key))
    # Set the API endpoint
    endpoint = "https://api.openai.com/v1/images/generations"
    # Set the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    # Set the data
    data = {
        "model": "image-alpha-001",
        "prompt": keywords,
        "size": "1024x1024",
        "response_format": "url"
    }

    # Make the request
    return requests.post(endpoint, headers=headers, json=data)

def main():
    keywords = input("Enter the keywords for the image:")
    print("Invoking the api...")
    response = invokeOpenAiAPI(keywords)
    print("Image generation done...")
    res = json.loads(response.content.decode("utf8"))
    url = res["data"][0]["url"]
    print("Saving the image...")
    downloadImageFromUrl(url)

main()