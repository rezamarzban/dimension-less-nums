# dimension-less-nums
Dimension less numbers in various engineering fields 



https://github.com/user-attachments/assets/a1b13fc6-5ff6-4ba4-9272-52e4e35763c5



1. **Reynolds Number (Re):**
   **$Re = \dfrac{\rho u L}{\mu}$**
   Characterizes flow regime (laminar or turbulent).

2. **Péclet Number (Pe):**
   **$Pe = \dfrac{u L}{D}$**
   **$Pe = Re \cdot Sc$**
   Ratio of advective to diffusive transport.

3. **Nusselt Number (Nu):**
   **$Nu = \dfrac{h L}{k}$**
   **$Nu = f(Re, Pr)$** (forced convection)  
   **$Nu = f(Ra, Pr)$** (free convection)  
   Describes the ratio of convective to conductive heat transfer.

4. **Prandtl Number (Pr):**
   **$Pr = \dfrac{\mu c_p}{k}$**
   Ratio of momentum diffusivity to thermal diffusivity.

5. **Schmidt Number (Sc):**
   **$Sc = \dfrac{\mu}{\rho D}$**
   **$Sc = \dfrac{\nu}{D}$**
   Ratio of momentum diffusivity to mass diffusivity.

6. **Sherwood Number (Sh):**
   **$Sh = \dfrac{k_m L}{D}$**
   **$Sh = f(Re, Sc)$**
   Mass transfer equivalent of the Nusselt number.

7. **Stanton Number (St):**
   **$St = \dfrac{h}{\rho c_p u}$**
   **$St = \dfrac{Nu}{Re \cdot Pr}$**
   Describes the heat transfer coefficient relative to the convective heat transfer.

8. **Froude Number (Fr):**
   **$Fr = \dfrac{u^2}{g L}$**
   Compares inertial forces to gravitational forces.

9. **Weber Number (We):**
   **$We = \dfrac{\rho u^2 L}{\sigma}$**
   Ratio of inertial forces to surface tension forces.

10. **Damköhler Number (Da):**
    **$Da = \dfrac{r_{\text{reaction}}}{r_{\text{diffusion}}}$**
    Describes the ratio of reaction rate to transport rate.

11. **Biot Number (Bi):**
    **$Bi = \dfrac{h L}{k}$**
    Ratio of internal thermal resistance to surface thermal resistance.

12. **Grashof Number (Gr):**
    **$Gr = \dfrac{g \beta \Delta T L^3}{\nu^2}$**
    Characterizes natural convection based on buoyancy and viscous forces.

13. **Rayleigh Number (Ra):**
    **$Ra = Gr \cdot Pr = \dfrac{g \beta \Delta T L^3}{\nu \alpha}$**
    **$Ra = f(Gr, Pr)$**
    Describes natural convection, indicating the transition from conduction to convection. **$\alpha$** is thermal diffusivity, **$\nu$** is kinematic viscosity.

14. **Lewis Number (Le):**
    **$Le = \dfrac{\alpha}{D} = \dfrac{Sc}{Pr}$**
    Ratio of thermal diffusivity to mass diffusivity.

15. **Euler Number (Eu):**
    **$Eu = \dfrac{p}{\rho u^2}$**
    Ratio of pressure forces to inertial forces.

16. **Eckert Number (Ec):**
    **$Ec = \dfrac{u^2}{c_p T}$**
    Relates kinetic energy to thermal energy, often used in compressible flow.

17. **Strouhal Number (St):**
    **$St = \dfrac{f L}{u}$**
    Describes oscillating flow, where **$f$** is the frequency of oscillation, **$L$** is characteristic length, and **$u$** is velocity.
    
## Nusselt number 

1. **Nusselt Number (Nu) for Forced Convection:**
   **$Nu = f(Re, Pr)$**
   - Common correlations:
     - For circular pipes:  
       **$Nu = 0.023 Re^{0.8} Pr^{n}$** (where **$n \approx 0.3$** for heating and **$n \approx 0.3$** for cooling).
     - For flow over a flat plate:  
       **$Nu = \dfrac{0.332 Re^{1/2} Pr^{1/3}}{L}$**.

2. **Nusselt Number (Nu) for Free Convection:**
   **$Nu = f(Ra, Pr)$**
   - Common correlations:
     - For vertical plates:  
       **$Nu = 0.68 + \dfrac{0.67 Ra^{1/4}}{(1 + (0.492/Pr)^{9/16})^{4/9}}$**.
     - For horizontal plates:  
       **$Nu = 0.54 Ra^{1/4}$** (for **$Ra < 10^9$**).

3. **Nusselt Number (Nu) for Combined Convection:**
   **$Nu = f(Re, Pr, Ra)$**
   - When both forced and free convection are present, correlations can become complex and may involve both **$Re$** and **$Ra$**.

4. **General Empirical Correlation:**
   - A general expression can be derived depending on the specific geometry and flow conditions.

## Sherwood number 

1. **Sherwood Number (Sh) for Forced Convection:**
   **$Sh = f(Re, Sc)$**
   - Common correlations:
     - For flow over a flat plate:  
       **$Sh = 0.332 Re^{1/2} Sc^{1/3}$**.
     - For circular pipes:  
       **$Sh = 0.023 Re^{0.8} Sc^{n}$** (where **$n \approx 0.3$**).

2. **Sherwood Number (Sh) for Free Convection:**
   **$Sh = f(Gr, Sc)$**
   - Common correlations:
     - For vertical plates:  
       **$Sh = 0.68 + \dfrac{0.67 Gr^{1/4}}{(1 + (0.492/Sc)^{9/16})^{4/9}}$**.
     - For horizontal plates:  
       **$Sh = 0.54 Gr^{1/4}$** (for **$Gr < 10^9$**).

3. **Sherwood Number (Sh) for Mass Transfer in Packed Beds:**
   **$Sh = f(Re, Sc)$**
   - A common correlation for packed beds:  
     **$Sh = 2 + 0.6 Re^{1/2} Sc^{1/3}$**.

4. **General Empirical Correlation:**
   - Depending on the specific geometry and flow conditions, various empirical correlations can be derived based on experimental data.

## Python Code

To calculating dimension less numbers with python, firstly clone the repository, then run below code in the repository directory:

```python
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
```

## Online available references 

Here are some online references that contain information about dimensionless numbers in chemical engineering and fluid mechanics:

1. **MIT OpenCourseWare - Introduction to Fluid Mechanics:**
   - [Fluid Mechanics](https://ocw.mit.edu/courses/mechanical-engineering/2-001-science-of-fluid-mechanics-fall-2004/)
   - This course includes lecture notes and resources discussing fluid mechanics principles, including dimensionless numbers like Reynolds and Nusselt numbers.

2. **Engineering Toolbox - Dimensionless Numbers:**
   - [Dimensionless Numbers](https://www.engineeringtoolbox.com/dimensionless-numbers-d_952.html)
   - This website provides a summary of various dimensionless numbers commonly used in engineering applications, including their definitions and relevance.

3. **University of Cambridge - Lecture Notes on Fluid Mechanics:**
   - [Lecture Notes](http://www.dspace.cam.ac.uk/handle/1810/324165)
   - These notes cover essential fluid mechanics concepts, including a section on dimensionless numbers.

4. **NPTEL - Heat Transfer:**
   - [Heat Transfer Course](https://nptel.ac.in/courses/103/105/103105135/)
   - The National Programme on Technology Enhanced Learning (NPTEL) offers a course that includes video lectures and materials discussing heat transfer and related dimensionless numbers.

5. **Wolfram Demonstrations Project - Dimensionless Numbers:**
   - [Dimensionless Numbers](http://demonstrations.wolfram.com/DimensionlessNumbers/)
   - This project provides interactive demonstrations related to various dimensionless numbers and their applications.

6. **Coursera - Fluid Mechanics for Engineers:**
   - [Fluid Mechanics for Engineers](https://www.coursera.org/learn/fluid-mechanics-engineers)
   - This course includes discussions on dimensionless numbers in the context of fluid mechanics.

7. **University of Florida - Chemical Engineering Courses:**
   - [Chemical Engineering Resources](https://www.che.ufl.edu/che-course-syllabi/)
   - This site provides links to various chemical engineering courses, some of which discuss dimensionless numbers relevant to transport phenomena.

8. **ResearchGate - Publications on Dimensionless Numbers:**
   - [ResearchGate](https://www.researchgate.net/)
   - A platform where you can search for academic papers and publications related to dimensionless numbers in chemical engineering and fluid mechanics.

These online resources can provide valuable insights and detailed explanations about dimensionless numbers and their applications in engineering.
