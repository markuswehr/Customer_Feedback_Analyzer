# App Store Feedback Scraper

This repository contains a tool that scrapes feedback from the app store, analyzes it using topic modeling and semantic serach and displays the results in a streamlit app.

## Requirements

- pip
- python3

## Installation

To install the dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

From root run the following command:

```
streamlit run app.py
```

This will start the streamlit app on your local machine. You can then use the app to scrape reviews from the Apple App Store and analyze them.

## Repo structure

```
customer-feedback-analyzer/
├── app.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── lda_model.pkl
├── src/
│   ├── data/
│   ├── models/
│   └── visualization/
├── requirements.txt
├── README.md
└── LICENSE
```

## Contributing
If you want to contribute to this project, please fork the repository and create a pull request with your changes. All contributions are 
welcome!

## License
This project is licensed under the MIT License.
