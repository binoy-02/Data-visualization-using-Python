import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Sample data for states
data = {
    'state': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'value': [50, 30, 20, 40, 25]
}

df = pd.DataFrame(data)

# Load a map of the USA
usa = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
usa = usa[usa.name == "United States of America"]

# Merge the data with the geospatial data
states = gpd.read_file('path_to_states_shapefile')  # You need a shapefile for US states
states = states.merge(df, left_on='name', right_on='state')

# Plotting the choropleth map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
states.boundary.plot(ax=ax)
states.plot(column='value', ax=ax, legend=True, cmap='OrRd')
plt.title('Choropleth Map Example')
plt.show()
