# API Post

import requests

# API endpoint for posts
api_url = "https://jsonplaceholder.typicode.com/posts"

# Data to send (this will mimic creating a blog post)
data_to_send = {
    "title": "Learning Python API",
    "body": "This is a simple post to learn how to use APIs in Python!",
    "userId": 1
}

# 1. Sending data with POST
response_post = requests.post(api_url, json=data_to_send)

# Check if the POST request was successful
if response_post.status_code == 201:  # 201 = Created
    print("Data successfully sent!")
    print("Response:", response_post.json())
else:
    print("Failed to send data. Status code:", response_post.status_code)

# 2. Verifying data with GET
post_id = response_post.json().get("id")  # Extract the ID of the created post
if post_id:
    response_get = requests.get(f"{api_url}/{post_id}")

    if response_get.status_code == 200:  # 200 = OK
        print("\nRetrieved Data:")
        print(response_get.json())
    else:
        print("Failed to retrieve data. Status code:", response_get.status_code)
else:
    print("Could not verify the data because the post ID was not returned.")
