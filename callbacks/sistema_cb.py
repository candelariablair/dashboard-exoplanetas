from dash import callback, Input, Output, html
import plotly.express as px
import pandas as pd
import numpy as np
from utils.datos import df, filtrar_datos, obtener_datos_sistema
from utils.colores import colores_metodos
from layouts.sistema import crear_tarjeta, crear_tarjeta_estrella

@callback(
    Output('fig_arquitectura', 'figure'),
    Output('contenedor-info-sistema', 'children'),
    Input('dropdown-zoom-sistema', 'value'),
)
def actualizar_pestana_sistema(hostname):
    datos = obtener_datos_sistema(hostname)

    fila = datos.iloc[0]

    n_planetas = int(fila['sy_pnum'])
    n_estrellas = int(fila['sy_snum'])
    n_lunas = int(fila['sy_mnum'])
    distancia = f"{fila['sy_dist']:.1f}" if pd.notna(fila['sy_dist']) else 'N/A'

    bloque_info_sistema = html.Div(
        [
            html.H3(
                f'Información del sistema: {hostname}',
                style={
                    'color': '#F1F5FF',
                    'fontSize': '18px',
                    'fontWeight': '600',
                    'marginTop': '0',
                    'marginBottom': '16px',
                },
            ),

            html.Div(
                [
                    crear_tarjeta(n_planetas, 'N.º planetas'),
                    crear_tarjeta(n_estrellas, 'N.º estrellas'),
                    crear_tarjeta(n_lunas, 'N.º lunas'),
                    crear_tarjeta(distancia,'Distancia (pc)'),
                ],
                style={
                    'display': 'flex',
                    'gap': '16px',
                    'flexWrap': 'wrap',  # Se adaptan si la pantalla es pequeña
                },
            ),
            crear_tarjeta_estrella(fila, hostname)
        ]
    )

    fig = px.scatter(
        datos,
        x='xp',
        y='yp',
        size='tamano_plot',
        size_max=24,
        color='discoverymethod',
        color_discrete_map=colores_metodos,
        text='pl_name',
        hover_name='pl_name',
        custom_data=[
            'pl_rade_str',
            'pl_bmasse_str',
            'pl_orbper_str',
            'pl_orbsmax',
            'pl_orbeccen'
        ],
        title=f'Arquitectura Orbital de {hostname}',
        labels={'discoverymethod': 'Método'},
    )

    fig.update_traces(
        marker=dict(line=dict(color='#F1F5FF', width=1)),
        textposition='top center',
        textfont=dict(color='#F1F5FF', size=11),
        hovertemplate=(
            '<b>%{hovertext}</b><br>'
            'Radio: %{customdata[0]}<br>'
            'Masa: %{customdata[1]}<br>'
            'Periodo: %{customdata[2]}<br>'
            'Semieje mayor: %{customdata[3]:.3f} UA<br>'
            'Excentricidad: %{customdata[4]:.3f}'
            '<extra></extra>'
        ),
    )

    theta = np.linspace(0, 2 * np.pi, 200)
    for _, planeta in datos.iterrows():
        a = planeta['pl_orbsmax']
        e = planeta['pl_orbeccen']
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        fig.add_scatter(
            x=r * np.cos(theta),
            y=r * np.sin(theta),
            mode='lines',
            line=dict(color='rgba(241, 245, 255, 0.25)', width=1, dash='dot'),
            showlegend=False,
            hoverinfo='skip',
        )

    fig.add_scatter(
        x=[0],
        y=[0],
        mode='markers',
        marker=dict(
            size=22,
            color='#FDB813',
            line=dict(color='#F1F5FF', width=1.5),
        ),
        name='Estrella anfitriona',
        hovertemplate=f'<b>Estrella {hostname}</b><extra></extra>',
    )

    apoastro_max = (
        datos['pl_orbsmax'] * (1 + datos['pl_orbeccen'])
    ).max()
    limite = apoastro_max * 1.25

    fig.update_layout(
        height=650,
        paper_bgcolor='#090E1C',
        plot_bgcolor='#090E1C',
        font_color='#F1F5FF',
        xaxis=dict(
            title='Distancia (UA)',
            range=[-limite, limite],
            zeroline=False,
            gridcolor='rgba(241, 245, 255, 0.1)',
        ),
        yaxis=dict(
            title='Distancia (UA)',
            range=[-limite, limite],
            scaleanchor='x',
            scaleratio=1,
            zeroline=False,
            gridcolor='rgba(241, 245, 255, 0.1)',
        ),
    )

    return fig, bloque_info_sistema
