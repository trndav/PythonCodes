#  JSONPlaceholder API

import requests

# Base URL of the API
BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_posts():
    """Fetch and display all post titles."""
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        #print(f"{posts}")
        print("Posts:\n")
        for post in posts:
            print(f"ID: {post['id']} - Title: {post['title']}")
        return posts
    else:
        print("Failed to fetch posts.")
        return []

def fetch_post_details(post_id):
    """Fetch and display details of a specific post."""
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        post = response.json()
        #print(f"{post}")
        print("\nPost Details:")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
    else:
        print("Post not found!")

def main():
    """Main function to drive the program."""
    posts = fetch_posts()
    if posts:
        while True:
            try:
                choice = input("\nEnter a Post ID to view details (or 'exit' to quit): ")
                if choice.lower() == "exit":
                    print("Goodbye!")
                    break
                fetch_post_details(int(choice))
            except ValueError:
                print("Invalid input. Please enter a valid Post ID.")

if __name__ == "__main__":
    main()
