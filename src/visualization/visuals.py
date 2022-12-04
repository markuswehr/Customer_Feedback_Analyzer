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

    # create the figure
    #fig = px.bar(
        # specify the data for the bar charts
    #    keywords_list,
        # use the 'group' barmode to arrange the bars in columns
    #    barmode='group',
    #    subplot_titles=[str(f"Topic {x}") for x in range(1, len(keywords_list))]
    #)

    # create a figure object
    #fig = go.Figure()

    # iterate over the list of lists
    #for topic in keywords_list:
        # create a bar chart using the current list of values
    #    bar = go.Bar(x=list(range(1, len(topic) + 1)), y=topic)
        
        # add the bar chart to the figure
    #    fig.add_trace(bar)
        
    
    # create a plotly bar chart that shows the top keywords for each topic
    #fig = px.bar(keywords_list[0], x=list(range(1, len(keywords_list[0]) + 1)), y=keywords_list[0], orientation="h")

    return fig