import os, math#, xlsxwriter, openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# from openpyxl.styles import Font, PatternFill


import xarray as xr




df1 = pd.DataFrame({ "d":[1,2,3,4],
                      "S22":[10.1,20.1,30.1,40.1]},
                        index={"a", "b", "c", "d"})

df2 = pd.DataFrame({ "d":[1,2,3,4],
                     "S22":[10.2,20.2,30.2,40.2]},
                        index={"a", "b", "c", "d"})


df3 = pd.DataFrame({ "d":[1,2,3,4],
                     "S22":[10.3,20.3,30.3,40.3]},
                        index={"a", "b", "c", "d"})


# da = xr.DataArray([9, 0, 2, 1, 0],
#                   dims=['x'],
#                   coords={'x': [10, 20, 30, 40, 50]})
# da.to_netcdf("saved_on_disk.nc")
# ds_disk = xr.open_dataset("saved_on_disk.nc")
# df2.to_pickle("ee")
# proba = df3.to_xarray()






x1 = df1.to_xarray()
x2 = df2.to_xarray()
x3 = df3.to_xarray()









temp = 15 + 8 * np.random.randn(2, 2, 3)
precip = 10 * np.random.rand(2, 2, 3)
lon = [[-99.83, -99.32], [-99.79, -99.23]]
lat = [[42.25, 42.21], [42.63, 42.59]]

zaSad = xr.Dataset(
    {
        "temperature": (["x", "y", "time"], temp),
        "precipitation": (["x", "y", "time"], precip),
    },

    coords={
        "lon": (["x", "y"], lon),
        "lat": (["x", "y"], lat),
        "time": pd.date_range("2014-09-06", periods=3),
        "reference_time": pd.Timestamp("2014-09-05"),
    }

)


print(zaSad["temperature"])


















