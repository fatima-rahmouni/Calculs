import numpy as np
import matplotlib.pyplot as plt

# Define constants
TARGET = 30  # G/cm
mu_0 = 4 * np.pi * 1e-7

def current_func(R_bob, N, distance_between_coils=200e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = TARGET * ((R_bob**2 + (distance_between_coils / 2)**2)**(5/2))
    b = (3 * mu_0 * R_bob**2 * distance_between_coils / 2)
    return 1e-4 * 1e2 * a / b / N

def Power_func(R_bob, N, r_fil, distance_between_coils=200e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    ro = 1.7 * 1e-8  # ohm*m
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = 2 * np.pi * ro * R_bob * (1e-4 * 1e2 * TARGET * (R_bob**2 + (distance_between_coils / 2)**2)**(5/2))**2
    b = (np.pi * r_fil**2) * (3 * mu_0 * R_bob**2 * distance_between_coils / 2)**2
    return a / b / N

# Arrays for R_bob and N
R_bob_array = np.linspace(50e-3, 200e-3, 50)  # Radius array
N_array = [100, 200, 300]  # Number of turns for the first and second plot

# Specific r_fil values
r_fil_array = [0.5e-3 / 2, 1e-3 / 2, 2e-3 / 2]  # Wire radii (r_fil) in meters

# Predefined line widths for the three r_fil values
line_widths = [1.5, 3, 4.5]  # Preset line widths for each wire radius

# Predefined colors: blue, orange, and green
colors = ['blue', 'orange', 'green']

# Create subplots for current and power
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=150)

# Plot Current vs Radius for different N with consistent colors
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    result = current_func(R_bob_array, N=N)
    ax1.plot(R_bob_array * 1e2, result.flatten(), label=f'N = {N}', color=color)
ax1.set_xlabel('Radius $R_{bob}$ [cm]')
ax1.set_ylabel('Current [A]')
ax1.set_title('Current vs Radius for Different Numbers of Turns (N) \n$x_0=10$ cm')
ax1.legend()

# Plot Power vs Radius for different N and use preset line widths for different r_fil
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    for j, r_fil in enumerate(r_fil_array):
        # Calculate the diameter (2 * r_fil)
        diameter_fil = 2 * r_fil
        # Calculate S_ec = 2 * sqrt(N) * r_fil
        S_ec = 2 * np.sqrt(N) * r_fil
        result_power = Power_func(R_bob_array, N=N, r_fil=r_fil)
        ax2.plot(R_bob_array * 1e2, result_power.flatten(), '-', 
                 label=f'N = {N}, $\\varnothing_{{fil}}$ = {diameter_fil*1e3:.2f} mm, $S_{{ec}}$ = {S_ec*1e3:.2f} mm x {S_ec*1e3:.2f} mm', 
                 linewidth=line_widths[j], color=color)  # Use predefined color

ax2.set_xlabel('Radius $R_{bob}$ [cm]')
ax2.set_ylabel('Power [W]')
ax2.set_yscale('log')  # Set logarithmic scale for y-axis on ax2
ax2.grid()
ax2.set_title('Power vs Radius for Different Numbers of Turns (N) and Wire Diameters \n$x_0=10$ cm')
ax2.legend()

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plots
plt.show()


#%%
import numpy as np
import matplotlib.pyplot as plt

# Define constants
TARGET = 30  # G/cm
mu_0 = 4 * np.pi * 1e-7

def current_func(R_bob, N, distance_between_coils=300e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = TARGET * ((R_bob**2 + (distance_between_coils / 2)**2)**(5/2))
    b = (3 * mu_0 * R_bob**2 * distance_between_coils / 2)
    return 1e-4 * 1e2 * a / b / N

def Power_func(R_bob, N, r_fil, distance_between_coils=300e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    ro = 1.7 * 1e-8  # ohm*m
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = 2 * np.pi * ro * R_bob * (1e-4 * 1e2 * TARGET * (R_bob**2 + (distance_between_coils / 2)**2)**(5/2))**2
    b = (np.pi * r_fil**2) * (3 * mu_0 * R_bob**2 * distance_between_coils / 2)**2
    return a / b / N

# Arrays for R_bob and N
R_bob_array = np.linspace(50e-3, 200e-3, 50)  # Radius array
N_array = [100, 200, 300]  # Number of turns for the first and second plot

# Specific r_fil values
r_fil_array = [0.5e-3 / 2, 1e-3 / 2, 2e-3 / 2]  # Wire radii (r_fil) in meters

# Predefined line widths for the three r_fil values
line_widths = [1.5, 3, 4.5]  # Preset line widths for each wire radius

# Predefined colors: blue, orange, and green
colors = ['blue', 'orange', 'green']

# Create subplots for current and power
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=150)

# Plot Current vs Radius for different N with consistent colors
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    result = current_func(R_bob_array, N=N)
    ax1.plot(R_bob_array * 1e2, result.flatten(), label=f'N = {N}', color=color)
ax1.set_xlabel('Radius $R_{bob}$ [cm]')
ax1.set_ylabel('Current [A]')
ax1.set_title('Current vs Radius for Different Numbers of Turns (N) \n$x_0=15$ cm')
ax1.legend()

# Plot Power vs Radius for different N and use preset line widths for different r_fil
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    for j, r_fil in enumerate(r_fil_array):
        # Calculate the diameter (2 * r_fil)
        diameter_fil = 2 * r_fil
        # Calculate S_ec = 2 * sqrt(N) * r_fil
        S_ec = 2 * np.sqrt(N) * r_fil
        result_power = Power_func(R_bob_array, N=N, r_fil=r_fil)
        ax2.plot(R_bob_array * 1e2, result_power.flatten(), '-', 
                 label=f'N = {N}, $\\varnothing_{{fil}}$ = {diameter_fil*1e3:.2f} mm, $S_{{ec}}$ = {S_ec*1e3:.2f} mm x {S_ec*1e3:.2f} mm', 
                 linewidth=line_widths[j], color=color)  # Use predefined color

ax2.set_xlabel('Radius $R_{bob}$ [cm]')
ax2.set_ylabel('Power [W]')
ax2.set_yscale('log')  # Set logarithmic scale for y-axis on ax2
ax2.grid()
ax2.set_title('Power vs Radius for Different Numbers of Turns (N) and Wire Diameters \n$x_0=15$ cm')
ax2.legend()

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plots
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt

# Define constants
TARGET = 30  # G/cm
mu_0 = 4 * np.pi * 1e-7

def current_func(R_bob, N, distance_between_coils=400e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = TARGET * ((R_bob**2 + (distance_between_coils / 2)**2)**(5/2))
    b = (3 * mu_0 * R_bob**2 * distance_between_coils / 2)
    return 1e-4 * 1e2 * a / b / N

def Power_func(R_bob, N, r_fil, distance_between_coils=400e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    ro = 1.7 * 1e-8  # ohm*m
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = 2 * np.pi * ro * R_bob * (1e-4 * 1e2 * TARGET * (R_bob**2 + (distance_between_coils / 2)**2)**(5/2))**2
    b = (np.pi * r_fil**2) * (3 * mu_0 * R_bob**2 * distance_between_coils / 2)**2
    return a / b / N

# Arrays for R_bob and N
R_bob_array = np.linspace(50e-3, 200e-3, 50)  # Radius array
N_array = [100, 200, 300]  # Number of turns for the first and second plot

# Specific r_fil values
r_fil_array = [0.5e-3 / 2, 1e-3 / 2, 2e-3 / 2]  # Wire radii (r_fil) in meters

# Predefined line widths for the three r_fil values
line_widths = [1.5, 3, 4.5]  # Preset line widths for each wire radius

# Predefined colors: blue, orange, and green
colors = ['blue', 'orange', 'green']

# Create subplots for current and power
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=150)

# Plot Current vs Radius for different N with consistent colors
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    result = current_func(R_bob_array, N=N)
    ax1.plot(R_bob_array * 1e2, result.flatten(), label=f'N = {N}', color=color)
ax1.set_xlabel('Radius $R_{bob}$ [cm]')
ax1.set_ylabel('Current [A]')
ax1.set_title('Current vs Radius for Different Numbers of Turns (N) \n$x_0=20$ cm')
ax1.legend()

# Plot Power vs Radius for different N and use preset line widths for different r_fil
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    for j, r_fil in enumerate(r_fil_array):
        # Calculate the diameter (2 * r_fil)
        diameter_fil = 2 * r_fil
        # Calculate S_ec = 2 * sqrt(N) * r_fil
        S_ec = 2 * np.sqrt(N) * r_fil
        result_power = Power_func(R_bob_array, N=N, r_fil=r_fil)
        ax2.plot(R_bob_array * 1e2, result_power.flatten(), '-', 
                 label=f'N = {N}, $\\varnothing_{{fil}}$ = {diameter_fil*1e3:.2f} mm, $S_{{ec}}$ = {S_ec*1e3:.2f} mm x {S_ec*1e3:.2f} mm', 
                 linewidth=line_widths[j], color=color)  # Use predefined color

ax2.set_xlabel('Radius $R_{bob}$ [cm]')
ax2.set_ylabel('Power [W]')
ax2.set_yscale('log')  # Set logarithmic scale for y-axis on ax2
ax2.grid()
ax2.set_title('Power vs Radius for Different Numbers of Turns (N) and Wire Diameters \n$x_0=20$ cm')
ax2.legend()

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plots
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

# Define constants
TARGET = 30  # G/cm
mu_0 = 4 * np.pi * 1e-7

def current_func(R_bob, N, distance_between_coils=100e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = TARGET * ((R_bob**2 + (distance_between_coils / 2)**2)**(5/2))
    b = (3 * mu_0 * R_bob**2 * distance_between_coils / 2)
    return 1e-4 * 1e2 * a / b / N

def Power_func(R_bob, N, r_fil, distance_between_coils=100e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    ro = 1.7 * 1e-8  # ohm*m
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = 2 * np.pi * ro * R_bob * (1e-4 * 1e2 * TARGET * (R_bob**2 + (distance_between_coils / 2)**2)**(5/2))**2
    b = (np.pi * r_fil**2) * (3 * mu_0 * R_bob**2 * distance_between_coils / 2)**2
    return a / b / N

# Arrays for R_bob and N
R_bob_array = np.linspace(20e-3, 200e-3, 60)  # Radius array
N_array = [100, 200, 300]  # Number of turns for the first and second plot

# Specific r_fil values
r_fil_array = [0.5e-3 / 2, 1e-3 / 2, 2e-3 / 2]  # Wire radii (r_fil) in meters

# Predefined line widths for the three r_fil values
line_widths = [1.5, 3, 4.5]  # Preset line widths for each wire radius

# Predefined colors: blue, orange, and green
colors = ['blue', 'orange', 'green']

# Create subplots for current and power
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=150)

# Plot Current vs Radius for different N with consistent colors
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    result = current_func(R_bob_array, N=N)
    ax1.plot(R_bob_array * 1e2, result.flatten(), label=f'N = {N}', color=color)
ax1.set_xlabel('Radius $R_{bob}$ [cm]')
ax1.set_ylabel('Current [A]')
ax1.set_title('Current vs Radius for Different Numbers of Turns (N) \n$x_0=5$ cm')
ax1.legend()

# Plot Power vs Radius for different N and use preset line widths for different r_fil
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    for j, r_fil in enumerate(r_fil_array):
        # Calculate the diameter (2 * r_fil)
        diameter_fil = 2 * r_fil
        # Calculate S_ec = 2 * sqrt(N) * r_fil
        S_ec = 2 * np.sqrt(N) * r_fil
        result_power = Power_func(R_bob_array, N=N, r_fil=r_fil)
        ax2.plot(R_bob_array * 1e2, result_power.flatten(), '-', 
                 label=f'N = {N}, $\\varnothing_{{fil}}$ = {diameter_fil*1e3:.2f} mm, $S_{{ec}}$ = {S_ec*1e3:.2f} mm x {S_ec*1e3:.2f} mm', 
                 linewidth=line_widths[j], color=color)  # Use predefined color

ax2.set_xlabel('Radius $R_{bob}$ [cm]')
ax2.set_ylabel('Power [W]')
ax2.set_yscale('log')  # Set logarithmic scale for y-axis on ax2
ax2.set_title('Power vs Radius for Different Numbers of Turns (N) and Wire Diameters \n$x_0=5$ cm')
ax2.grid()
ax2.legend()

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plots
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches  # Import the Rectangle module

# Define constants
TARGET = 30  # G/cm
mu_0 = 4 * np.pi * 1e-7

# Distance between coils
distance_between_coils = 120e-3  # Change this value for titles
x_0 = distance_between_coils / 2 * 1e3  # Convert to millimeters

def current_func(R_bob, N, distance_between_coils=120e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = TARGET * ((R_bob**2 + (distance_between_coils / 2)**2)**(5/2))
    b = (3 * mu_0 * R_bob**2 * distance_between_coils / 2)
    return 1e-4 * 1e2 * a / b / N

def Power_func(R_bob, N, r_fil, distance_between_coils=120e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    ro = 1.7 * 1e-8  # ohm*m
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = 2 * np.pi * ro * R_bob * (1e-4 * 1e2 * TARGET * (R_bob**2 + (distance_between_coils / 2)**2)**(5/2))**2
    b = (np.pi * r_fil**2) * (3 * mu_0 * R_bob**2 * distance_between_coils / 2)**2
    return a / b / N

# Arrays for R_bob and N
R_bob_array = np.linspace(20e-3, 50e-3, 60)  # Radius array
N_array = [100, 200, 300]  # Number of turns for the first and second plot

# Specific r_fil values
r_fil_array = [0.5e-3 / 2, 1e-3 / 2, 2e-3 / 2]  # Wire radii (r_fil) in meters

# Predefined line widths for the three r_fil values
line_widths = [1.5, 3, 4.5]  # Preset line widths for each wire radius

# Predefined colors: blue, orange, and green
colors = ['blue', 'orange', 'green']

# Create subplots for current and power
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=150)

# Plot Current vs Radius for different N with consistent colors
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    result = current_func(R_bob_array, N=N, distance_between_coils=distance_between_coils)
    ax1.plot(R_bob_array * 1e3, result.flatten(), label=f'N = {N}', color=color)
ax1.set_xlabel('Radius $R_{bob}$ [mm]')
ax1.set_ylabel('Current [A]')
ax1.set_title(f'Current vs Radius for Different Numbers of Turns (N) \n$x_0={x_0:.1f}$ mm (Gradient_target={TARGET} G/cm)')
ax1.legend()

# Create a blue rectangle for the R_bob range (25 mm to 45 mm)
rect1 = mpatches.Rectangle((25, 0), 20, 10, color='blue', alpha=0.3)  # Rectangle in blue (x=25 to 45, y=0 to 100)
ax1.add_patch(rect1)


# Plot Power vs Radius for different N and use preset line widths for different r_fil
for j, r_fil in enumerate(r_fil_array):
    for idx, N in enumerate(N_array):
        color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
        # Calculate the diameter (2 * r_fil)
        diameter_fil = 2 * r_fil
        # Calculate S_ec = 2 * sqrt(N) * r_fil
        S_ec = 2 * np.sqrt(N) * r_fil
        result_power = Power_func(R_bob_array, N=N, r_fil=r_fil)
        ax2.plot(R_bob_array * 1e2, result_power.flatten(), '-', 
                 label=f'N = {N}, $\\varnothing_{{fil}}$ = {diameter_fil*1e3:.2f} mm, $S_{{ec}}$ = {S_ec*1e3:.2f} mm x {S_ec*1e3:.2f} mm', 
                 linewidth=line_widths[j], color=color)  # Use predefined color

ax2.set_xlabel('Radius $R_{bob}$ [cm]')
ax2.set_ylabel('Power [W]')
ax2.set_yscale('log')  # Set logarithmic scale for y-axis on ax2
ax2.set_title('Power vs Radius for Different Numbers of Turns (N) and Wire Diameters \n$x_0=5$ cm')
ax2.grid()
ax2.legend()
# Blue rectangle for R_bob range (25 mm to 45 mm) and Power from 0 to 10^2 W
rect2 = mpatches.Rectangle((25, 10), 20, 10**2-10, color='blue', alpha=0.3)
ax2.add_patch(rect2)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plots
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define constants
TARGET = 30  # G/cm
mu_0 = 4 * np.pi * 1e-7

# Distance between coils
distance_between_coils = 150e-3  # Change this value for titles
x_0 = distance_between_coils / 2 * 1e3  # Convert to millimeters

def current_func(R_bob, N, distance_between_coils=150e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = TARGET * ((R_bob**2 + (distance_between_coils / 2)**2)**(5/2))
    b = (3 * mu_0 * R_bob**2 * distance_between_coils / 2)
    return 1e-4 * 1e2 * a / b / N

def Power_func(R_bob, N, r_fil, distance_between_coils=150e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    ro = 1.7 * 1e-8  # ohm*m
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = 2 * np.pi * ro * R_bob * (1e-4 * 1e2 * TARGET * (R_bob**2 + (distance_between_coils / 2)**2)**(5/2))**2
    b = (np.pi * r_fil**2) * (3 * mu_0 * R_bob**2 * distance_between_coils / 2)**2
    return a / b / N

def weight(wire_diameter, number_of_spirals, coil_radius):
    Density_of_pure_copper = 8960  # kg/m^3
    wire_section_area = np.pi * (wire_diameter / 2) ** 2
    Length = number_of_spirals * 2 * np.pi * coil_radius
    return Length * wire_section_area * Density_of_pure_copper

# Arrays for R_bob and N
R_bob_array = np.linspace(20e-3, 110e-3, 60)  # Radius array
N_array = [100, 200, 300]  # Number of turns for the first and second plot

# Specific r_fil values
r_fil_array = [0.5e-3 / 2, 1e-3 / 2, 2e-3 / 2]  # Wire radii (r_fil) in meters

# Predefined line widths for the three r_fil values
line_widths = [1.5, 3, 4.5]  # Preset line widths for each wire radius

# Predefined colors: blue, orange, and green
colors = ['blue', 'orange', 'green']

# Create subplots for current and power
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=150)
rect1 = mpatches.Rectangle((25, 0), 81, 10, color='blue', alpha=0.3)  # Rectangle in blue (x=25 to 45, y=0 to 100)
ax1.add_patch(rect1)

# Plot Current vs Radius for different N with consistent colors
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    result = current_func(R_bob_array, N=N, distance_between_coils=distance_between_coils)
    ax1.plot(R_bob_array * 1e3, result.flatten(), label=f'N = {N}', color=color)
ax1.set_xlabel('Radius $R_{bob}$ [mm]')
ax1.set_ylabel('Current [A]')
ax1.set_title(f'Current vs Radius for Different Numbers of Turns (N) \n$x_0={x_0:.1f}$ mm (Gradient_target={TARGET} G/cm)')
ax1.legend()

rect2 = mpatches.Rectangle((25, 10), 81, 10**2-10, color='blue', alpha=0.3)  # Rectangle in blue (x=25 to 45, y=0 to 100)
ax2.add_patch(rect2)

# Plot Power vs Radius for different N and use preset line widths for different r_fil
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    for j, r_fil in enumerate(r_fil_array):
        # Calculate the diameter (2 * r_fil)
        diameter_fil = 2 * r_fil
        # Calculate S_ec = 2 * sqrt(N) * r_fil
        S_ec = 2 * np.sqrt(N) * r_fil
        result_power = Power_func(R_bob_array, N=N, r_fil=r_fil, distance_between_coils=distance_between_coils)
        ax2.plot(R_bob_array * 1e3, result_power.flatten(), '-', 
                 label=f'N = {N}, $\\varnothing_{{fil}}$ = {diameter_fil*1e3:.2f} mm, $S_{{ec}}$ = {S_ec*1e3:.2f} mm x {S_ec*1e3:.2f} mm', 
                 linewidth=line_widths[j], color=color)  # Use predefined color
ax2.set_xlabel('Radius $R_{bob}$ [mm]')
ax2.set_ylabel('Power [W]')
ax2.set_yscale('log')  # Set logarithmic scale for y-axis on ax2
ax2.grid(True)  # Turn on the grid for better visibility
ax2.set_title(f'Power vs Radius for Different Numbers of Turns (N) and Wire Diameters \n$x_0={x_0:.1f}$ mm (Gradient_target={TARGET} G/cm)')
ax2.legend()

# Adjust layout for the first figure
plt.tight_layout()

# Create a new figure for weight
fig2, ax3 = plt.subplots(figsize=(8, 6), dpi=150)

# Plot Weight vs Radius for different N and r_fil
for idx, N in enumerate(N_array):
    color = colors[idx]  # Use blue, orange, and green for N = 100, 200, 300
    for j, r_fil in enumerate(r_fil_array):
        w = weight(r_fil * 2, N, R_bob_array)  # Calculate weight for given r_fil, N, and R_bob
        ax3.plot(R_bob_array * 1e3, w, '-', 
                 label=f'N = {N}, $r_{{fil}}$ = {r_fil*1e3:.2f} mm', 
                 linewidth=line_widths[j], color=color)  # Use predefined color
ax3.set_xlabel('Radius $R_{bob}$ [mm]')
ax3.set_ylabel('Weight [kg]')
ax3.set_title(f'Weight vs Radius for Different Numbers of Turns (N) \nand Wire Diameters')
ax3.grid(True)
ax3.legend()

# Adjust layout for the second figure
plt.tight_layout()

# Show plots
plt.show()

#%%
import magpylib as magpy

# Define constants
TARGET = 30  # G/cm
mu_0 = 4 * np.pi * 1e-7 #Newton.Ampere-2
def method_1_windings(radius_min, distance_between_coils, current, number_of_turns, wire_section):
    print('WAIT CORRECT DISTANCE')
    distance = radius  # distance between the centers of the loops
    r_fil=wire_section
    coil_thickness = np.ceil(np.sqrt(number_of_turns))*r_fil*2
   
    # Create the two coils 
    coil1 = magpy.Collection()
    coil2 = magpy.Collection()

    for radius_coil in np.linspace(radius_min, radius_min+ coil_thickness , int(np.ceil(np.sqrt(number_of_turns)))):
        for depth_coil in np.linspace(0, np.ceil(np.sqrt(number_of_turns))*r_fil, int(np.ceil(np.sqrt(number_of_turns)))):
            winding_1 = magpy.current.Circle(
            current=current,
            diameter=radius_coil*2,
            position=(0,0,depth_coil+distance_between_coils/2),
            )
            coil1.add(winding_1)

    for radius_coil in np.linspace(radius_min, (radius_min+ coil_thickness) , int(np.ceil(np.sqrt(number_of_turns)))):
        for depth_coil in np.linspace(0, np.ceil(np.sqrt(number_of_turns))*r_fil, int(np.ceil(np.sqrt(number_of_turns)))):
            winding_2 = magpy.current.Circle(
            current=-current,
            diameter=radius_coil*2,
            position=(0,0,-(depth_coil+distance_between_coils/2)),
            )
            coil2.add(winding_2)
    
    # Create a collection of the two coils
    anti_helmholtz_spirals = magpy.Collection(coil1, coil2)
   
    # Position the loops at +distance/2 and -distance/2 along the z-axis
    #loop1.move([0, 0, distance/2])
    #loop2.move([0, 0, -distance/2])
    
    anti_helmholtz_spirals.show()
    return anti_helmholtz_spirals

# def current_analytic(radius_min, distance_between_coils, current, number_of_turns, wire_section):
#     mu_0=1.256637*1e-6 #Newton.Ampere-2
#     for radius_coil in np.arange(radius_min, radius_min+ coil_thickness , int(r_fil)):
#         for distance_between_coils in np.arange(distance_between_coils_min,distance_between_coils_min+r_fil*2*N, int(r_fil)):
#             a  = radius_coil * distance_between_coils/2
#             b  = (radius_coil*radius_coil+(distance_between_coils/2)**2)**(5/2)
#             gradient = - (1e4/1e2)*mu_0*current*3*a/b
#     return gradient



def current_func(R_bob, N, distance_between_coils=300e-3):
    # Ensure that broadcasting works correctly by using np.newaxis
    R_bob = np.asarray(R_bob)[:, np.newaxis]
    N = np.asarray(N)
    
    a = TARGET * ((R_bob**2 + (distance_between_coils / 2)**2)**(5/2))
    b = (3 * mu_0 * R_bob**2 * distance_between_coils / 2)
    return 1e-4 * 1e2 * a / b / N


#Define Roymage parameters
radius_min = 25e-3 # in mm
radius = 300e-3  # in mm
distance_between_coils = 120e-3
distance_between_coils_150 = distance_between_coils + 30e-3
number_of_turns = 200
current = 10 # in A
wire_section = 1.7e-3 # in mm


for radius_coil in np.arange(radius_min, radius_min+ coil_thickness , int(r_fil)):
    for distance_between_coils in np.arange(distance_between_coils_min,distance_between_coils_min+r_fil*2*N, int(r_fil)):

# Calculate the gradien analyticaly
gradient_calcule_120=(1e4/1e2)*(3*mu_0*current*radius*radius*distance_between_coils/2)/(radius*radius+(distance_between_coils/2)**2)**(5/2)
gradient_calcule_150=(1e4/1e2)*(3*mu_0*current*radius*radius*distance_between_coils_150/2)/(radius*radius+(distance_between_coils_150/2)**2)**(5/2)
print('gradient calculé x0 120=',gradient_calcule_120)
print('gradient calculé x0 150=',gradient_calcule_150)

#Creat the coils with spirals
anti_helmholtz_spirals_x0_120=method_1_windings(radius_min, distance_between_coils, current, number_of_turns, wire_section)
anti_helmholtz_spirals_x0_150=method_1_windings(radius_min, distance_between_coils+30e-3, current, number_of_turns, wire_section)

Number_of_points = 500  # Increased grid resolution
view = np.linspace(-0.5, +0.5, Number_of_points)
ZEROS = np.zeros(Number_of_points)
# Define a 3D grid for calculation
mid = Number_of_points//2 
dr = view[1]-view[0]


positions_z = np.vstack([ZEROS, ZEROS, view]).T
Bz_120 = anti_helmholtz_spirals_x0_120.getB(positions_z)[:, 2]
Bz_150 = anti_helmholtz_spirals_x0_150.getB(positions_z)[:, 2]

positions_y = np.vstack([ZEROS, view, ZEROS]).T
By = anti_helmholtz_spirals_x0_120.getB(positions_y)[:, 1]
By_150 = anti_helmholtz_spirals_x0_150.getB(positions_y)[:, 1]

plt.plot(view, Bz_120)
plt.plot(view, By)

fig, ax = plt.subplots()
ax.plot(view, Bz_120, label='Bz')  
ax.plot(view, Bz_150, label='Bz_150') 
ax.plot(view, By, label='By')  
ax.legend()
ax.set_title('Magnetic Field Components')
ax.set_xlabel('View (m)')  
ax.set_ylabel('Magnetic Field ()')  
fig.tight_layout()