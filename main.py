# main.py

from dimensional_analysis import DimensionlessNumbers

# Parameters for calculations
rho = 1.2  # Density (kg/m^3)
u = 3.0    # Velocity (m/s)
L = 0.5    # Characteristic length (m)
mu = 0.001 # Dynamic viscosity (Pa.s)
cp = 1005  # Specific heat capacity (J/(kg.K))
k = 0.025  # Thermal conductivity (W/(m.K))
beta = 0.003  # Thermal expansion coefficient (1/K)
delta_T = 30  # Temperature difference (K)
g = 9.81   # Acceleration due to gravity (m/s^2)
D = 0.01   # Diffusion coefficient (m^2/s)
k_m = 0.001 # Mass transfer coefficient (m/s)
sigma = 0.072 # Surface tension (N/m)
f = 1.0    # Frequency (Hz)
T = 300    # Temperature (K)
p = 101325 # Pressure (Pa)
r_reaction = 0.1  # Reaction rate (1/s)
r_diffusion = 0.01 # Diffusion rate (1/s)

# Calculate dimensionless numbers
Re = DimensionlessNumbers.reynolds_number(rho, u, L, mu)
Pe = DimensionlessNumbers.peclet_number(u, L, D)
Nu = DimensionlessNumbers.nusselt_number(10, L, k)  # Example heat transfer coefficient
Pr = DimensionlessNumbers.prandtl_number(mu, cp, k)
Sc = DimensionlessNumbers.schmidt_number(mu, rho, D)
Sh = DimensionlessNumbers.sherwood_number(k_m, L, D)
St = DimensionlessNumbers.stanton_number(10, rho, cp, u)  # Example h = 10 W/(m^2.K)
Fr = DimensionlessNumbers.froude_number(u, g, L)
We = DimensionlessNumbers.weber_number(rho, u, L, sigma)
Da = DimensionlessNumbers.damkohler_number(r_reaction, r_diffusion)
Bi = DimensionlessNumbers.biot_number(10, L, k)  # Example h = 10 W/(m^2.K)
Gr = DimensionlessNumbers.grashof_number(g, beta, delta_T, L, 0.01)  # Assuming nu = 0.01
Ra = DimensionlessNumbers.rayleigh_number(g, beta, delta_T, L, 0.01, 0.0001)  # nu = 0.01, alpha = 0.0001
Le = DimensionlessNumbers.lewis_number(0.0001, D, Sc, Pr)  # Assuming alpha = 0.0001
Eu = DimensionlessNumbers.euler_number(p, rho, u)
Ec = DimensionlessNumbers.eckert_number(u, cp, T)
Stn = DimensionlessNumbers.strouhal_number(f, L, u)

# Print results
print(f"Reynolds Number (Re): {Re}")
print(f"Péclet Number (Pe): {Pe}")
print(f"Nusselt Number (Nu): {Nu}")
print(f"Prandtl Number (Pr): {Pr}")
print(f"Schmidt Number (Sc): {Sc}")
print(f"Sherwood Number (Sh): {Sh}")
print(f"Stanton Number (St): {St}")
print(f"Froude Number (Fr): {Fr}")
print(f"Weber Number (We): {We}")
print(f"Damköhler Number (Da): {Da}")
print(f"Biot Number (Bi): {Bi}")
print(f"Grashof Number (Gr): {Gr}")
print(f"Rayleigh Number (Ra): {Ra}")
print(f"Lewis Number (Le): {Le}")
print(f"Euler Number (Eu): {Eu}")
print(f"Eckert Number (Ec): {Ec}")
print(f"Strouhal Number (Stn): {Stn}")
