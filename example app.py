from dash import Dash, dcc, html, Input, Output, callback,dash_table
import plotly.express as px

import pandas as pd

app = Dash(__name__)
df=pd.read_csv("C:\\Users\\vishwa\\Downloads\\Automobile_data.csv")
d=df.head()
app.layout=html.Div([html.H1(children='My app'),dcc.RadioItems(options=['stroke','horsepower','peak-rpm'],value='horsepower',id='drop-box'),dash_table.DataTable(data=d.to_dict('records')),dcc.Graph(figure={},id='graph'),dcc.Dropdown(options=['city-mpg','highway-mpg','price'],value='price',id='id2'),dcc.Graph(figure={},id='graph1')])
@app.callback(
    Output(component_id='graph',component_property='figure'),
    Output(component_id='graph1',component_property='figure'),
    Input(component_id='drop-box',component_property='value'),
    Input(component_id='id2',component_property='value'))

def update_graph(option,option1):
    fig=px.histogram(df,x='make',y=option)
    fig1=px.histogram(df,x='make',y=option1)
    return(fig,fig1)



if __name__ == '__main__':
    app.run(debug=True)
