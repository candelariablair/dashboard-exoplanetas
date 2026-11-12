import pandas as pd
import numpy as np

# 1. Carga y selección de columnas (de tus primeras celdas del notebook)
df0 = pd.read_csv('data/PSCompPars.tab', comment='#', sep='\t')

df = df0[['pl_name', 'hostname', 'pl_letter', 'hd_name', 'hip_name', 'tic_id', 'gaia_dr2_id', 'gaia_dr3_id',
          'sy_snum', 'sy_pnum', 'sy_mnum', 'cb_flag',
          'discoverymethod', 'disc_year', 'disc_refname', 'disc_pubdate', 'disc_locale', 'disc_facility', 'disc_telescope', 'disc_instrument',
          'pl_rade', 'pl_bmasse', 'pl_dens', 'pl_insol', 'pl_orbper', 'pl_orbeccen', 'pl_eqt', 'pl_orbsmax',
          'st_teff', 'st_rad', 'st_mass', 'st_dens', 'st_lum', 'st_met', 'st_age',
          'sy_dist', 'ra', 'dec']].copy()

# 2. Limpieza de nulos
cols = ['disc_facility', 'disc_telescope', 'disc_instrument', 'disc_locale', 'disc_pubdate']
for col in cols:
    if col in df.columns:
        df[col] = df[col].fillna('Desconocido')

# 3. Columnas calculadas (pl_vol y ra_plot)
pl_vol = pd.DataFrame({'pl_vol' : df['pl_bmasse'] / df['pl_dens']})
df = pd.concat([df, pl_vol], axis = 1)

ra_plot = pd.DataFrame({'ra_plot' : -np.where(df['ra'] > 180, df['ra'] - 360, df['ra'])})
df = pd.concat([df, ra_plot], axis = 1)

# 4. Función auxiliar para aplicar los 5 filtros globales en cualquier página
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
