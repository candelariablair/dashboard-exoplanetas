import pandas as pd
import numpy as np

# Carga y selección de columnas
df0 = pd.read_csv('data/PSCompPars.tab', comment='#', sep='\t')

df = df0[['pl_name', 'hostname', 'pl_letter', 'hd_name', 'hip_name', 'tic_id', 'gaia_dr2_id', 'gaia_dr3_id',
          'sy_snum', 'sy_pnum', 'sy_mnum', 'cb_flag',
          'discoverymethod', 'disc_year', 'disc_refname', 'disc_pubdate', 'disc_locale', 'disc_facility', 'disc_telescope', 'disc_instrument',
          'pl_rade', 'pl_bmasse', 'pl_dens', 'pl_insol', 'pl_orbper', 'pl_orbeccen', 'pl_eqt', 'pl_orbsmax',
          'st_teff', 'st_rad', 'st_mass', 'st_dens', 'st_lum', 'st_met', 'st_age',
          'sy_dist', 'ra', 'dec']].copy()

# Limpieza de nulos
cols = ['disc_facility', 'disc_telescope', 'disc_instrument', 'disc_locale', 'disc_pubdate']
for col in cols:
    if col in df.columns:
        df[col] = df[col].fillna('Desconocido')

# Agregar columnas calculadas (pl_vol y ra_plot)
pl_vol = pd.DataFrame({'pl_vol' : df['pl_bmasse'] / df['pl_dens']})
df = pd.concat([df, pl_vol], axis = 1)

ra_plot = pd.DataFrame({'ra_plot' : -np.where(df['ra'] > 180, df['ra'] - 360, df['ra'])})
df = pd.concat([df, ra_plot], axis = 1)

# Función para aplicar los 5 filtros globales en cualquier página
def filtrar_datos(metodo, anio, distancia, planeta, sistema):
    df_filtrado = df.copy()
    if metodo:
        df_filtrado = df_filtrado[df_filtrado['discoverymethod'].isin(metodo)]
    if anio is not None:
        df_filtrado = df_filtrado[df_filtrado['disc_year'].between(anio[0], anio[1])]
    if distancia is not None:
        df_filtrado = df_filtrado[df_filtrado['sy_dist'].between(distancia[0], distancia[1])]
    if planeta:
        df_filtrado = df_filtrado[df_filtrado['pl_name'].isin(planeta)]
    if sistema:
        df_filtrado = df_filtrado[df_filtrado['hostname'].isin(sistema)]
    return df_filtrado

# Funcion para obtener los datos de un sistema planetario
def obtener_datos_sistema(hostname):
    if not hostname:
        return pd.DataFrame()

    datos = df[df['hostname'] == hostname].copy()
    datos = datos.dropna(subset=['pl_orbsmax'])

    # Ordenar por semieje mayor y luego por radio
    datos = datos.sort_values(
        by=['pl_orbsmax', 'pl_rade'], ascending=[True, True]
    )

    # Calcular tamaño visual proporcional al radio
    radios = datos['pl_rade'].fillna(datos['pl_rade'].median())
    if radios.isna().all():
        datos['tamano_plot'] = 12
    elif radios.min() == radios.max():
        datos['tamano_plot'] = 16
    else:
        datos['tamano_plot'] = np.interp(
            radios, (radios.min(), radios.max()), (9, 24)
        )

    # Calcular posición en el periastro (xp, yp)
    datos['pl_orbeccen'] = datos['pl_orbeccen'].fillna(0)
    datos['xp'] = datos['pl_orbsmax'] * (1 - datos['pl_orbeccen'])
    datos['yp'] = 0.0

    # Rellenar nulos para evitar "nan" en el hover
    datos['pl_rade_str'] = (
        datos['pl_rade'].map('{:.2f} R⊕'.format).fillna('Desconocido')
    )
    datos['pl_bmasse_str'] = (
        datos['pl_bmasse'].map('{:.2f} M⊕'.format).fillna('Desconocido')
    )
    datos['pl_orbper_str'] = (
        datos['pl_orbper'].map('{:.2f} días'.format).fillna('Desconocido')
    )

    return datos
