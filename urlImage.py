import requests

# Set the URL of the image to be downloaded
def urlImage():
    url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-TlYHs7Ex3lp0xDaz2yIg9X1Y/user-YETnybKZzmG8BVOYbVkiJEIR/img-oyFfFx6WSUjUpIabVDd5AQKR.png?st=2023-01-08T07%3A20%3A22Z&se=2023-01-08T09%3A20%3A22Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-01-08T01%3A36%3A49Z&ske=2023-01-09T01%3A36%3A49Z&sks=b&skv=2021-08-06&sig=dYnTQkfM5zk1wDazPimQPm7qr0eN0XxWCaI8%2B7ZuBgI%3D"

    # Send a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the image
        with open("image.jpg", "wb") as f:
            f.write(response.content)
        print("Image saved!")
    else:
        print("Failed to download image")
