# Api

import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]:  # Display only the first 5 posts
            print(f"Title: {post['title']}")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

fetch_posts()


def fetch_post_by_id(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        post = response.json()
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
    else:
        print(f"Post with ID {post_id} not found.")

fetch_post_by_id(1)  # Change the number to fetch a different post

def comments(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    response = requests.get(url)

    if response.status_code == 200:
        comments = response.json()
        for comment in comments:
            print(f"Post {post_id} comment is: {comment['body']}")

    else:
        print(f"There are no comments for post {post_id}")

comments(1)