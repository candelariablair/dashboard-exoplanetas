from dash import callback, Input, Output
import plotly.express as px
from utils.datos import filtrar_datos
from utils.colores import colores_metodos

@callback(
    Output('fig_radio_masa', 'figure'),
    Output('fig_periodo_masa', 'figure'),
    Input('dropdown-metodo-descubrimiento', 'value'),
    Input('slider-año-descubrimiento', 'value'),
    Input('slider-distancia', 'value'),
    Input('dropdown-planeta', 'value'),
    Input('dropdown-sistema', 'value')
)
def actualizar_graficos_masa(metodo, anio, distancia, planeta, sistema):
    df_filtrado = filtrar_datos(metodo, anio, distancia, planeta, sistema)

    fig_radio_masa = px.scatter(
        df_filtrado, x='pl_bmasse', y='pl_rade',
        log_x=True, log_y=True,
        color='discoverymethod',
        color_discrete_map=colores_metodos,
        hover_data=['pl_name'],
        title='Radio vs Masa',
        labels={
            'pl_name': 'Nombre del planeta',
            'discoverymethod': 'Método de descubrimiento',
            'pl_bmasse': 'Masa en masas terrestres',
            'pl_rade': 'Radio en radios terrestres'
        }
    )

    fig_radio_masa.update_layout(paper_bgcolor='#090E1C', plot_bgcolor='#090E1C', font_color='#F1F5FF')

    fig_periodo_masa = px.scatter(
        df_filtrado, x='pl_bmasse', y='pl_orbper',
        log_x=True, log_y=True,
        color='discoverymethod',
        color_discrete_map=colores_metodos,
        hover_data=['pl_name'],
        title='Periodo vs Masa',
        labels={
            'pl_name': 'Nombre del planeta',
            'discoverymethod': 'Método de descubrimiento',
            'pl_bmasse': 'Masa en masas terrestres',
            'pl_orbper': 'Periodo orbital (dias)'
        }
    )

    fig_periodo_masa.update_layout(paper_bgcolor='#090E1C', plot_bgcolor='#090E1C', font_color='#F1F5FF')

    return fig_radio_masa, fig_periodo_masa
