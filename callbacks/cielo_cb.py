from dash import callback, Input, Output
import plotly.express as px
from utils.datos import filtrar_datos
from utils.colores import colores_metodos

@callback(
    Output('fig_cielo', 'figure'),
    Input('dropdown-metodo-descubrimiento', 'value'),
    Input('slider-año-descubrimiento', 'value'),
    Input('slider-distancia', 'value'),
    Input('dropdown-planeta', 'value'),
    Input('dropdown-sistema', 'value')
)
def actualizar_grafico_cielo(metodo, anio, distancia, planeta, sistema):
    df_filtrado = filtrar_datos(metodo, anio, distancia, planeta, sistema)

    fig_cielo = px.scatter_geo(
        df_filtrado, lon='ra_plot', lat='dec',
        projection='mollweide',
        color='discoverymethod',
        color_discrete_map=colores_metodos,
        hover_data=['pl_name'],
        title='Mapa celeste',
        labels={
            'pl_name': 'Nombre del planeta',
            'ra_plot': 'Ascensión recta (°)',
            'dec': 'Declinación (°)',
            'discoverymethod': 'Método de descubrimiento'
        }
    )

    fig_cielo.update_geos(
        visible=False, bgcolor='#090E1C',
        showframe=True, lataxis_showgrid=True, lonaxis_showgrid=True
    )
    fig_cielo.update_layout(paper_bgcolor='#090E1C', font_color='#F1F5FF')
    return fig_cielo
