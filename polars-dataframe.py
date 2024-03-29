import polars as pl
import pandas as pd
import streamlit as st
import pygwalker as pyg


df = pl.DataFrame(
    {
        'Modell': ['iPhone X','iPhone XS','iPhone 12','iPhone 13','Samsung S11','Samsung S12','Mi A1','Mi A2'],
        'Verkäufe': [80,170,130,205,400,30,14,8],     
        'Unternehmen': ['Apple','Apple','Apple','Apple','Samsung','Samsung','Xiao Mi','Xiao Mi'],
    }
)

df2 = pl.DataFrame(
    {
        "0" : [1,2,3],
        "1" : [80,170,130],
    }
)
df.dtypes
df.columns    # gibt ['Modell', 'Verkäufe', 'Unternehmen'] zurück
st.write(df.rows())
st.write(df.select('Modell'))
st.write(df.select(['Modell','Unternehmen']))
st.write(df.select(pl.col(pl.Int64)))
st.write(df.select(pl.col(['Modell','Verkäufe']).sort_by('Verkäufe')))
st.write(df.select([pl.col(pl.Utf8)]))
st.write(df.row(0))   # erste Zeile abrufen
st.write(df.filter(pl.col('Unternehmen') == 'Apple'))         
st.write(df.filter((pl.col('Unternehmen') == 'Apple') | (pl.col('Unternehmen') == 'Samsung')))
st.write(df.filter(pl.col('Unternehmen') == 'Apple').select('Modell'))
st.write(df.filter(pl.col('Unternehmen') == 'Apple').select(['Modell','Verkäufe']))

df = pl.read_csv('./For_Analysis_in_R.csv',try_parse_dates = True)
walker = pyg.walk(df)
