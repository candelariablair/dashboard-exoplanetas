from dash import callback, Input, Output
import plotly.express as px
from utils.datos import filtrar_datos
from utils.colores import colores_metodos

@callback(
    Output('fig_evolucion', 'figure'),
    Input('dropdown-metodo-descubrimiento', 'value'),
    Input('slider-año-descubrimiento', 'value'),
    Input('slider-distancia', 'value'),
    Input('dropdown-planeta', 'value'),
    Input('dropdown-sistema', 'value')
)
def actualizar_grafico_evolucion(metodo, anio, distancia, planeta, sistema):
    df_filtrado = filtrar_datos(metodo, anio, distancia, planeta, sistema)

    df_evolucion = df_filtrado.groupby(['discoverymethod', 'disc_year']).agg('pl_name').count().reset_index(name='count')
    orden_metodos = df_evolucion.groupby('discoverymethod')['count'].sum().sort_values(ascending=False).index.tolist()

    fig_evolucion = px.bar(
        df_evolucion, x='disc_year', y='count',
        color='discoverymethod',
        color_discrete_map=colores_metodos,
        category_orders={'discoverymethod': orden_metodos},
        title='Evolución',
        labels={
            'disc_year': 'Año de descubrimiento',
            'discoverymethod': 'Método de descubrimiento',
            'count': 'Número de planetas'
        }
    )

    fig_evolucion.update_layout(paper_bgcolor='#090E1C', plot_bgcolor='#090E1C', font_color='#F1F5FF')
    
    return fig_evolucion
