import numpy as np
import matplotlib.pyplot as plt

# Load the data
input_surface = np.load('output_data/output_surface.npy')
input_upper = np.load('output_data/output_upper.npy')

def show_surface():
    # Define the surface variables names for labeling
    surface_vars = ['MSLP', 'U10', 'V10', 'T2M']

    # Generate latitude and longitude arrays based on the given dimensions 721 and 1440
    lat = np.linspace(90, -90, 721)
    lon = np.linspace(0, 359.75, 1440)

    # Create a meshgrid for latitude and longitude
    Lon, Lat = np.meshgrid(lon, lat)

    # Loop through each surface variable and plot
    for i, var in enumerate(surface_vars):
        plt.figure(figsize=(15, 5))
        plt.title(f"{var} Surface Data")
        plt.pcolormesh(Lon, Lat, input_surface[i, :, :], shading='auto', cmap='jet')
        plt.colorbar(label=var)
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()

def show_upper():
    # Define variable names and pressure levels
    # variables = ['Z', 'Q', 'T', 'U', 'V']
    variables = ['T']
    pressure_levels = [1000, 925, 850, 700, 600, 500, 400, 300, 250, 200, 150, 100, 50]

    # Create latitude and longitude grids based on given dimensions of 721 and 1440
    lat = np.linspace(90, -90, 721)
    lon = np.linspace(0, 359.75, 1440)
    Lon, Lat = np.meshgrid(lon, lat)

    # Select a specific pressure level for demonstration (e.g., index 0 corresponds to 1000hPa)
    pressure_level_idx = 0

    # Loop through each variable to create a plot at the selected pressure level
    for i, var in enumerate(variables):
        plt.figure(figsize=(15, 5))
        plt.title(f"{var} at {pressure_levels[pressure_level_idx]}hPa")
        plt.pcolormesh(Lon, Lat, input_upper[i, pressure_level_idx, :, :], shading='auto', cmap='jet')
        plt.colorbar(label=var)
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()
    
show_upper()