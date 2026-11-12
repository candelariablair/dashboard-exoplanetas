from dash import Dash, html, dcc, Input, Output
from layouts import filtros, cielo, evolucion, sesgos, sistema
from callbacks import cielo_cb, evolucion_cb, sesgos_cb, sistema_cb

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Explorador de Exoplanetas"),
    
    # Contenedor de filtros globales (se ocultará en la pestaña 4)
    html.Div(filtros.layout, id="contenedor-filtros-globales"),
    
    # Pestañas con id y value inicial
    dcc.Tabs(id="tabs-principales", value="tab-cielo", children=[
        dcc.Tab(label='1. Cielo', value="tab-cielo", children=cielo.layout),
        dcc.Tab(label='2. Evolución', value="tab-evolucion", children=evolucion.layout),
        dcc.Tab(label='3. Sesgos', value="tab-sesgos", children=sesgos.layout),
        dcc.Tab(label='4. Sistema', value="tab-sistema", children=sistema.layout),
    ])
])

# Callback para ocultar los filtros globales solo en la pestaña 4
@app.callback(
    Output("contenedor-filtros-globales", "style"),
    Input("tabs-principales", "value")
)
def mostrar_ocultar_filtros(tab_activa):
    if tab_activa == "tab-sistema":
        return {"display": "none"}
    return {"display": "block"}

if __name__ == '__main__':
    app.run(debug=True)
