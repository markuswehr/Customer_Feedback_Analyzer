import requests
from bs4 import BeautifulSoup
import json


def scrape_reviews(url: str, save_file_path: str):
    # Make a request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all of the review elements on the page
    review_elements = soup.find_all(class_="we-customer-review__body")

    # Loop through each review element
    reviews_data = []
    for review in review_elements:
        text = review.get_text()
        review_data = {"text": text}
        reviews_data.append(review_data)

    with open(save_file_path, "w") as f:
        json.dump(reviews_data, f)

if __name__ == "__main__":
    scrape_reviews(
        url="https://apps.apple.com/de/app/ing-banking-to-go/id1176527145?see-all=reviews",
        save_file_path="../../data/raw/reviews.json",
    )
