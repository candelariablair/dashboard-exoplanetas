from dash import html, dcc

layout = html.Div([
    html.H2("Cielo Estrellado"),
    dcc.Graph(id="fig_cielo")
])
