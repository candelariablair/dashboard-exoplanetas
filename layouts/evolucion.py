from dash import html, dcc

layout = html.Div([
    html.H2("Evolución de Descubrimientos"),
    dcc.Graph(id="fig_evolucion")
])
