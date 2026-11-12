# Explorador Interactivo de Exoplanetas
Una aplicación web analítica e interactiva desarrollada en Python con Dash y Plotly para la exploración, visualización y análisis de sesgos observacionales en el catálogo de exoplanetas confirmados (Planetary Systems Composite Parameters - PSCompPars NASA).

## Características Principales

La aplicación está organizada en cuatro módulos principales de visualización, acompañados de un panel de filtros globales dinámicos:

- 🔭 Mapa del Cielo (cielo): Visualización espacial de las coordenadas celestes (Ascensión Recta y Declinación) de los exoplanetas.

- 📈 Evolución de Descubrimientos (evolucion): Análisis temporal del número de exoplanetas descubiertos por año, desglosado por método de detección (Tránsito, Velocidad Radial, Imagen Directa, Microlente gravitacional, etc.).

- ⚖️ Análisis de Sesgos Observacionales (sesgos): Gráficos comparativos (masa, radio, período orbital) diseñados para evidenciar las limitaciones instrumentales y los sesgos de selección de cada técnica de detección.

- 🪐 Inspector de Sistemas Planetarios (sistema): Vista detallada para explorar la arquitectura de sistemas específicos, comparando órbitas, tamaños relativos y parámetros estelares.

- 🎛️ Filtros Dinámicos (filtros): Controles interactivos para segmentar el dataset en tiempo real por método de descubrimiento, rango de años, distancia, nombre del planeta y sistema planetario.

## Estructura del Proyecto
```bash
Proyecto/
├── app.py                  # Punto de entrada principal e inicialización del servidor Dash
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Documentación del proyecto
├── assets/
│   └── estilo.css          # Estilo personalizado (tema oscuro/astronómico)
├── callbacks/              # Lógica reactiva e interactividad de cada vista
│   ├── __init__.py
│   ├── cielo_cb.py         # Callbacks para el mapa celeste
│   ├── evolucion_cb.py     # Callbacks para las series temporales de descubrimientos
│   ├── sesgos_cb.py        # Callbacks para los gráficos de sesgos observacionales
│   └── sistema_cb.py       # Callbacks para la inspección individual de sistemas
├── data/
│   └── PSCompPars.tab      # Dataset tabular con los parámetros compuestos de sistemas planetarios (NASA Exoplanet Archive)
├── layouts/                # Estructura visual y componentes UI de cada pestaña
│   ├── __init__.py
│   ├── cielo.py            # Diseño de la pestaña de distribución espacial
│   ├── evolucion.py        # Diseño de la pestaña de evolución temporal
│   ├── filtros.py          # Panel lateral/superior de controles y filtros globales
│   ├── sesgos.py           # Diseño de la pestaña de análisis de sesgos
│   └── sistema.py          # Diseño de la pestaña de detalle de sistemas
└── utils/                  # Funciones auxiliares y configuración compartida
    ├── __init__.py
    ├── colores.py          # Paletas de colores consistentes para métodos de detección y gráficos
    └── datos.py            # Carga, limpieza y preprocesamiento del archivo PSCompPars.tab
```

## Pasos para ejecutar localmente
1. Clonar el repositorio o descargar el proyecto:
    ```bash
    git clone <https://github.com/candelariablair/dashboard-exoplanetas>
    cd Proyecto
    ```
2. Crear y activar un entorno virtual (recomendado):
    - En Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    - En Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Ejecutar la aplicación:
    ```bash
    python app.py
    ```
5. Abrir en el navegador:
    ```bash
    Accede a http://127.0.0.1:8050/
    ```

## Fuente de Datos
Los datos utilizados provienen del archivo data/PSCompPars.tab, correspondiente a la tabla Planetary Systems Composite Parameters del NASA Exoplanet Archive. Esta tabla consolida un único conjunto de parámetros por planeta combinando mediciones de múltiples referencias bibliográficas para maximizar la completitud de los datos.

Nota: La tabla únicamente incluye los exoplanetas confirmados hasta el 28/10/2026. Para datos más recientes visitar el NASA Exoplanet Archive.