import requests
from bs4 import BeautifulSoup

def get_github_profile_image(github_url):
    try:
        response = requests.get(github_url)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the image tag with alt text like 'Avatar' or class
        image_tag = soup.find('img', {'alt': 'Avatar'}) or \
                    soup.find('img', class_='avatar-user')

        if image_tag and image_tag['src']:
            return image_tag['src']
        else:
            return "Profile image not found."

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    github_url = input("Enter a GitHub profile URL (e.g. https://github.com/octocat): ").strip()
    image_link = get_github_profile_image(github_url)
    print("Profile Image Link:", image_link)
