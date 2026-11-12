from dash import html, dcc
from utils.datos import df

anio_min = int(df["disc_year"].min())
anio_max = int(df["disc_year"].max())
dist_min = round(float(df["sy_dist"].min()), 0)
dist_max = round(float(df["sy_dist"].max()), 0)

layout = html.Div([
    # Fila 1: Los 3 Dropdowns lado a lado
    html.Div([
        html.Div([
            html.Label("Método de descubrimiento"),
            dcc.Dropdown(
                id="dropdown-metodo-descubrimiento",
                options=sorted(df['discoverymethod'].unique().tolist()),
                placeholder="Todos los métodos",
                multi=True
            )
        ], className="filtro-item"),

        html.Div([
            html.Label("Planeta"),
            dcc.Dropdown(
                id="dropdown-planeta",
                options=sorted(df['pl_name'].unique().tolist()),
                placeholder="Todos los planetas",
                multi=True
            )
        ], className="filtro-item"),

        html.Div([
            html.Label("Sistema planetario"),
            dcc.Dropdown(
                id="dropdown-sistema",
                options=sorted(df['hostname'].unique().tolist()),
                placeholder="Todos los sistemas",
                multi=True
            )
        ], className="filtro-item"),
    ], className="fila-dropdowns"),

    # Fila 2: Los 2 Sliders lado a lado con espacio arriba para los tooltips
    html.Div([
        html.Div([
            html.Label("Año de descubrimiento"),
            dcc.RangeSlider(
                id="slider-año-descubrimiento",
                min=anio_min,
                max=anio_max,
                step=1,
                value=[anio_min, anio_max],
                marks={anio_min: str(anio_min), 'style':{'color': '#F1F5FF'},
                       anio_max: str(anio_max), 'style':{'color': '#F1F5FF'}},
                tooltip={"placement": "bottom", "always_visible": False}
            )
        ], className="filtro-item slider-box"),

        html.Div([
            html.Label("Distancia al sistema (parsecs)"),
            dcc.RangeSlider(
                id="slider-distancia",
                min=dist_min,
                max=dist_max,
                step=1,
                value=[dist_min, dist_max],
                marks={round(dist_min): str(round(dist_min)), 'style':{'color': '#F1F5FF'},
                       round(dist_max): str(round(dist_max)), 'style':{'color': '#F1F5FF'}},
                tooltip={"bottom": "top", "always_visible": False}
            )
        ], className="filtro-item slider-box"),
    ], className="fila-sliders")

], className="contenedor-filtros")
