import json

def semantic_search(data_path: str, query: str):
  # load input data from json file
  with open(data_path, 'r') as j:
    data = json.loads(j.read())

  # create a list of texts from the input data
  texts = [item["text"] for item in data]
  
  # initialize an empty list to store the search results
  results = []

  # iterate over the list of lists
  for review in texts:
      # check if the query is contained in the current item
      if query.lower() in review.lower():
        # if the query is contained in the current item, add it to the results list
        results.append(review)

  # display the search results
  return results
