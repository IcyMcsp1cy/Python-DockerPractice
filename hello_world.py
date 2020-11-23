import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(name)

app.layout = html.Div(children=[
    html.H1(children='Hello World'),

    html.Div(children='This is a test')
])

if name == 'main':
    app.run_server(debug=True)
