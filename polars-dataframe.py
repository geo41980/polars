import polars as pl
import streamlit as st

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
st.write(df.select('Modell'))
df.columns    # gibt ['Modell', 'Verkäufe', 'Unternehmen'] zurück
st.write(df.rows(0))
