import polars as pl
 
df = pl.DataFrame(
    {
        'Modell': ['iPhone X','iPhone XS','iPhone 12','iPhone 13','Samsung S11','Samsung S12','Mi A1','Mi A2'],
        'Verkäufe': [80,170,130,205,400,30,14,8],     
        'Unternehmen': ['Apple','Apple','Apple','Apple','Samsung','Samsung','Xiao Mi','Xiao Mi'],
    }
)
#df
df2 = pl.DataFrame(
    {
        "0" : [1,2,3],
        "1" : [80,170,130],
    }
)
#df.dtypes
#df.columns 
df.select(['Modell','Unternehmen'])
#df.rows()
#df.select('Modell')
