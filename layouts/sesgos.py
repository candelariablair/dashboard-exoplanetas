from dash import html, dcc

layout = html.Div([
    html.H2("Sesgos de Detección"),
    dcc.Graph(id="fig_radio_masa"),
    html.Hr(),
    dcc.Graph(id="fig_periodo_masa")
])
