# dimensional_analysis.py

class DimensionlessNumbers:
    @staticmethod
    def reynolds_number(rho, u, L, mu):
        """Calculate Reynolds Number."""
        return (rho * u * L) / mu

    @staticmethod
    def peclet_number(u, L, D):
        """Calculate Péclet Number."""
        return u * L / D

    @staticmethod
    def nusselt_number(h, L, k):
        """Calculate Nusselt Number."""
        return (h * L) / k

    @staticmethod
    def prandtl_number(mu, cp, k):
        """Calculate Prandtl Number."""
        return (mu * cp) / k

    @staticmethod
    def schmidt_number(mu, rho, D):
        """Calculate Schmidt Number."""
        return mu / (rho * D)

    @staticmethod
    def sherwood_number(k_m, L, D):
        """Calculate Sherwood Number."""
        return (k_m * L) / D

    @staticmethod
    def stanton_number(h, rho, cp, u):
        """Calculate Stanton Number."""
        return h / (rho * cp * u)

    @staticmethod
    def froude_number(u, g, L):
        """Calculate Froude Number."""
        return (u ** 2) / (g * L)

    @staticmethod
    def weber_number(rho, u, L, sigma):
        """Calculate Weber Number."""
        return (rho * u ** 2 * L) / sigma

    @staticmethod
    def damkohler_number(r_reaction, r_diffusion):
        """Calculate Damköhler Number."""
        return r_reaction / r_diffusion

    @staticmethod
    def biot_number(h, L, k):
        """Calculate Biot Number."""
        return (h * L) / k

    @staticmethod
    def grashof_number(g, beta, delta_T, L, nu):
        """Calculate Grashof Number."""
        return (g * beta * delta_T * L ** 3) / (nu ** 2)

    @staticmethod
    def rayleigh_number(g, beta, delta_T, L, nu, alpha):
        """Calculate Rayleigh Number."""
        return (g * beta * delta_T * L ** 3) / (nu * alpha)

    @staticmethod
    def lewis_number(alpha, D, Sc, Pr):
        """Calculate Lewis Number."""
        return alpha / D  # or Sc / Pr

    @staticmethod
    def euler_number(p, rho, u):
        """Calculate Euler Number."""
        return p / (rho * u ** 2)

    @staticmethod
    def eckert_number(u, cp, T):
        """Calculate Eckert Number."""
        return (u ** 2) / (cp * T)

    @staticmethod
    def strouhal_number(f, L, u):
        """Calculate Strouhal Number."""
        return (f * L) / u
