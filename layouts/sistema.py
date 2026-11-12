from dash import Input, Output, callback, dcc, html
import numpy as np
import pandas as pd
import plotly.express as px
from utils.colores import colores_metodos
from utils.datos import df, obtener_datos_sistema

sistemas_disponibles = sorted(df['hostname'].dropna().unique())

layout = html.Div(
    [
        html.H2(
            'Arquitectura del Sistema Planetario',
            style={'color': '#F1F5FF', 'marginBottom': '15px'},
        ),
        # Selector de sistema (Dropdown)
        html.Div(
            [
                html.Label(
                    'Selecciona una estrella anfitriona:',
                    style={
                        'color': '#F1F5FF',
                        'marginBottom': '8px',
                        'display': 'block',
                    },
                ),
                dcc.Dropdown(
                    id='dropdown-zoom-sistema',
                    options=sistemas_disponibles,
                    value='TRAPPIST-1',
                    multi=False,
                    clearable=False,
                    placeholder='Busca o selecciona un sistema...',
                    style={'width': '350px', 'color': '#090E1C'},
                ),
            ],
            style={'marginBottom': '20px'},
        ),
        # Tarjeta dinámica con los datos de la estrella seleccionada
    html.Div(
        id='contenedor-info-sistema',
        style={
            'backgroundColor': '#0D1326',
            'border': '1px solid rgba(241, 245, 255, 0.12)',
            'borderRadius': '12px',
            'padding': '20px',
            'marginBottom': '24px',
        },
    ),
    # Gráfico de arquitectura orbital
    dcc.Graph(id='fig_arquitectura'),
    ],
    style={'padding': '20px', 'backgroundColor': '#090E1C'},
)

def crear_tarjeta(valor, etiqueta):
    return html.Div(
        [
            html.Div(
                str(valor),
                style={
                    'color': '#F1F5FF',
                    'fontSize': '36px',
                    'fontWeight': '700',
                    'lineHeight': '1.1',
                    'marginBottom': '6px',
                },
            ),
            # Subtítulo inferior
            html.Div(etiqueta, style={'color': '#94A3B8', 'fontSize': '14px'}),
        ],
        style={
            'backgroundColor': '#111827',
            'borderRadius': '10px',
            'padding': '20px 24px',
            'border': '1px solid rgba(241, 245, 255, 0.08)',
            'flex': '1',
            'minWidth': '180px',
        },
    )

def crear_tarjeta_estrella(fila, hostname):
    # Lista con las propiedades de la estrella
    propiedades = [
        ('Temperatura efectiva', 'st_teff', '°K', 0),
        ('Radio estelar', 'st_rad', 'R☉', 2),
        ('Masa estelar', 'st_mass', 'M☉', 2),
        ('Densidad estelar', 'st_dens', 'g/cm³', 2),
        ('Luminosidad', 'st_lum', 'log(L☉)', 2),
        ('Metalicidad [Fe/H]', 'st_met', 'dex', 2),
        ('Edad estimada', 'st_age', 'Gyr', 2),
    ]

    items_grid = []
    for etiqueta, col, unidad, decimales in propiedades:
        valor_raw = fila.get(col)

        # Mostrar 'Desconocido' cuando es NaN
        if pd.notna(valor_raw):
            valor_str = f'{valor_raw:.{decimales}f} {unidad}'
        else:
            valor_str = 'Desconocido'

        items_grid.append(
            html.Div(
                [
                    html.Div(
                        etiqueta,
                        style={
                            'color': '#94A3B8',
                            'fontSize': '13px',
                            'marginBottom': '4px',
                        },
                    ),
                    html.Div(
                        valor_str,
                        style={
                            'color': '#F1F5FF',
                            'fontSize': '18px',
                            'fontWeight': '600',
                        },
                    ),
                ],
                style={
                    'backgroundColor': '#090E1C',
                    'padding': '12px 16px',
                    'borderRadius': '8px',
                    'border': '1px solid rgba(241, 245, 255, 0.05)',
                },
            )
        )

    return html.Div(
        [
            html.H4(
                f'Propiedades de la estrella anfitriona ({hostname})',
                style={
                    'color': '#FBBF24',
                    'fontSize': '16px',
                    'fontWeight': '600',
                    'marginTop': '0',
                    'marginBottom': '14px'
                },
            ),
            html.Div(
                items_grid,
                style={
                    'display': 'grid',
                    'gridTemplateColumns': 'repeat(auto-fit, minmax(170px, 1fr))',
                    'gap': '12px',
                },
            ),
        ],
        style={
            'backgroundColor': '#111827',
            'borderRadius': '10px',
            'padding': '20px 24px',
            'border': '1px solid rgba(241, 245, 255, 0.08)',
            'marginTop': '16px',
        },
    )

