import streamlit as st

from src.visualization.visuals import plot_keywords_per_topic
from src.models.semantic_search import semantic_search
from src.data.scraper import scrape_reviews
from src.models.topic_modelling import topic_modeling

# Create a function for each page
def page1():
    st.write("Topic Modeling")
    topic_modeling(
        input_data="data/raw/reviews.json",
        save_file_path="data/processed/keywords.json",
    )
    st.write(plot_keywords_per_topic("data/processed/keywords.json"))

def page2():
    st.write("Semantic Search")
    query = st.text_input("Enter a search query:")
    results = semantic_search("data/raw/reviews.json", query)
    st.write("Search results:")
    for idx, review in enumerate(results):
        st.write(f"Result {idx+1}:\n", review)

# Create a main function
def main():
    st.title("App Review Feedback Analyzer")
    st.sidebar.title("Navigation")

    # Create the menu items in the sidebar
    page = st.sidebar.radio("Go to", ["Topic Modeling", "Semantic Search"])
    url = st.sidebar.text_input("Enter url to App Store reviews: ")
    if st.sidebar.button("Scrape most recent reviews"):
        if url == None:
            scrape_reviews(
                url="https://apps.apple.com/de/app/ing-banking-to-go/id1176527145?see-all=reviews",
                save_file_path="data/raw/reviews.json",
            )
        else:
            scrape_reviews(
                url=url,
                save_file_path="data/raw/reviews.json",
            )

    # Use the page variable to determine which page to show
    if page == "Topic Modeling":
        page1()
    elif page == "Semantic Search":
        page2()

# Run the main function
if __name__ == '__main__':
    main()
