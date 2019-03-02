import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

x = list(range(1,101,1))
y = [x_val**2 for x_val in x]

app.layout = html.Div(children=[
    html.H1(children='Welcome to my first Dash Dashboard'),
    html.Div(children='''
    Demo of Dash Graphing
    '''
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}
                    ],
            'layout':{
                'title':'Dash Data Visualization'
            }
        }
    ),

    dcc.Graph(
        id='x_vs_x_squared',
        figure={
            'data':[
                go.Scatter(
                    x=x,
                    y=y,
                    mode='markers',
                    marker={'size':10, 'line':{'width':0.5, 'color':'black'}}
                    )
                # {'x': x, 'y': y, 'type': 'scatter', 'name': 'Scatter'}
                ],
            'layout':
                go.Layout(
                xaxis={'type': 'linear', 'title': 'X'},
                yaxis={'title': 'X^2'},
                margin={'l': 40, 'b': 40, 't': 50, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest',
                title='X vs X^2'
                )
            # 'title':'Dash Data Visualization'
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
