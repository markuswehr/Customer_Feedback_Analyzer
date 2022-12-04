import json
import math
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def plot_keywords_per_topic(keywords: list):
    # load input data from json file
    with open(keywords, 'r') as j:
        keywords_list = json.loads(j.read())

    fig = make_subplots(rows=math.ceil(len(keywords_list)/2), cols=2)
    row=1
    col=1
    
    for topic in keywords_list:
        # create a bar chart using the current list of values
        fig.add_trace(
            go.Bar(x=list(range(1, len(topic) + 1)), y=topic,),
            row=row,
            col=col,
        )
        if col==1:
            col=2
        elif col==2:
            row=row+1
            col=1
    
    fig.update_layout(height=600, width=800, title_text="Topics from App Store")

    return fig
    