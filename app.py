from dash import Dash, html, dcc

# Importar layouts
from layouts import filtros, cielo, evolucion, sesgos, sistema

# Importar callbacks para activarlos
from callbacks import cielo_cb, evolucion_cb, sesgos_cb

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Explorador de Exoplanetas"),
    
    # Tus 5 filtros globales arriba de las pestañas
    filtros.layout,
    
    # Tus 4 pestañas
    dcc.Tabs([
        dcc.Tab(label='1. Cielo', children=cielo.layout),
        dcc.Tab(label='2. Evolución', children=evolucion.layout),
        dcc.Tab(label='3. Sesgos', children=sesgos.layout),
        dcc.Tab(label='4. Sistema', children=sistema.layout),
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
