# Dashboard Explorador Interactivo de Exoplanetas
Autora: Candelaria Blair Estrada

# Descripción
Aplicación web analítica e interactiva desarrollada para la exploración, visualización y análisis de exoplanetas confirmados. El dashboard busca responder a la pregunta de investigación: ¿Cómo evolucionan los descubrimientos de exoplanetas a lo largo del tiempo y de qué manera los sesgos observacionales de cada técnica de detección condicionan las características físicas (masa, radio, período orbital y ubicación espacial) de los planetas detectados?

# Dataset
- **Fuente**: NASA Exoplanet Archive - Planetary Systems Composite Parameters (`PSCompPars`)
- **Filas**: 6451 exoplanetas confirmados*
- **Columnas**: 325 variables astrofísicas y orbitales
- **Variables principales**:
    - `pl_name`: Nombre del planeta
    - `hostname`: Nombre de la estrella anfitriona
    - `discoverymethod`: Método de descubrimiento (Tránsito, Velocidad Radial, Imagen Directa,Microlente, etc.)
    - `disc_year`: Año de descubrimiento
    - `pl_orbper`: Período orbital (días)
    - `pl_rade`: Radio del planeta (en radios terrestres)
    - `pl_bmasse`: Masa del planeta (en masas terrestres)
    - `ra` / `dec`: Coordenadas celestes (Ascensión Recta y Declinación)
    - `sy_dist`: Distancia al sistema planetario (parsecs)

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
1. Clonar el repositorio e ingresar a la carpeta:
    ```bash
    git clone <https://github.com/candelariablair/dashboard-exoplanetas>
    cd Proyecto
    ```
2. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecutar la aplicación:
    ```bash
    python app.py
    ```
4. Abrir en el navegador:
    ```bash
    Accede a http://127.0.0.1:8050/
    ```

## Despliegue
- **URL**: https://dashboard-exoplanetas.onrender.com/
- **Plataforma**: Render

## Funcionalidades
- **Panel de Filtros Globales (`filtros`)**: Filtrado dinámico en tiempo real por método de descubrimiento, rango de años de descubrimiento, distancia, nombre del planeta y sistema planetario.
- **Pestaña 1 - Mapa del Cielo (`cielo`)**: Distribución espacial de los exoplanetas en coordenadas celestes (Ascensión Recta y Declinación) para identificar zonas de observación.
- **Pestaña 2 - Evolución Temporal (`evolucion`)**: Series de tiempo y gráficos acumulados de descubrimientos por año segmentados por técnica de detección.
- **Pestaña 3 - Sesgos Observacionales (`sesgos`)**: Gráficos de dispersión comparativos (Masa vs. Período Orbital, Radio vs. Masa) que evidencian las limitaciones instrumentales de cada método.
- **Pestaña 4 - Inspector de Sistemas (`sistema`)**: Vista dedicada para analizar la arquitectura individual de un sistema planetario específico, comparando órbitas y tamaños relativos entre los planetas que lo componen.

## Capturas de pantalla
<img width="1279" height="652" alt="image" src="https://github.com/user-attachments/assets/6a79dff1-00ab-4c87-a278-51054227b4d5" />

<img width="959" height="491" alt="image" src="https://github.com/user-attachments/assets/1230c454-d2a7-4d95-ae9c-878ab6ebf86c" />

<img width="945" height="487" alt="image" src="https://github.com/user-attachments/assets/c79dc389-0417-49bf-8fa0-3607fd67f82e" />

<img width="944" height="497" alt="image" src="https://github.com/user-attachments/assets/cdbad0aa-9bb2-4211-8ee8-12a463be2e17" />




## Tecnologías
- Python 3.11
- Pandas, Plotly, Dash
- CSS3 personalizado (`assets/estilo.css`)

## Conclusiones
- **Aprendizajes:** El análisis visual confirma que los métodos de detección presentan fuertes sesgos observacionales: la técnica de Tránsito domina en cantidad gracias a misiones espaciales (como Kepler y TESS) y favorece planetas cercanos a su estrella, mientras que la Velocidad Radial y la Imagen Directa detectan con mayor facilidad planetas masivos o lejanos. A nivel técnico, estructurar Dash de forma modular (`layouts/`, `callbacks/`, `utils/`) facilita enormemente el mantenimiento y escalabilidad del código.
- **Mejoras futuras:** Incorporar modelos predictivos o de agrupamiento (clustering) para clasificar tipos de planetas (supertierras, júpiteres calientes), añadir indicadores de zona de habitabilidad en el inspector de sistemas y conectar directamente con la API TAP de la NASA para actualizar los datos en tiempo real.

*Nota: La tabla únicamente incluye los exoplanetas confirmados hasta el 28/10/2026. Para datos más recientes visitar el NASA Exoplanet Archive.
