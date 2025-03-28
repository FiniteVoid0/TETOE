# Constants
c = 3e8  # Speed of light (m/s)
GeV_to_kg = 1.78266192e-27  # Conversion factor from GeV to kg
GeV_to_J = 1.60218e-10  # Conversion factor from GeV to Joules

# Yang-Mills mass gaps from TETOE model (in GeV)
mass_gap_SU2_TETOE = 1.23e16  # GeV
mass_gap_SU3_TETOE = 8.53e15  # GeV

# Determinism costs from previous calculation (in J)
determinism_cost_quantum = 1.465e-11  # J
determinism_cost_macro = 1.465e-20  # J

# Function to calculate corrected mass gap
def corrected_mass_gap(mass_gap_TETOE, E_cost):
    """
    Calculate the corrected Yang-Mills mass gap with determinism cost.
    :param mass_gap_TETOE: Mass gap from TETOE model (in GeV).
    :param E_cost: Determinism cost (in Joules).
    :return: Corrected mass gap (in GeV).
    """
    mass_gap_kg = mass_gap_TETOE * GeV_to_kg  # Convert mass gap to kg
    correction_kg = E_cost / c**2  # Convert energy cost to kg
    corrected_mass_gap_kg = mass_gap_kg - correction_kg  # Apply correction
    return corrected_mass_gap_kg / GeV_to_kg  # Convert back to GeV

# Corrected mass gaps
mass_gap_SU2_corrected = corrected_mass_gap(mass_gap_SU2_TETOE, determinism_cost_quantum)
mass_gap_SU3_corrected = corrected_mass_gap(mass_gap_SU3_TETOE, determinism_cost_quantum)

# Output results
print(f"Corrected Mass Gap (SU(2)): {mass_gap_SU2_corrected:.3e} GeV")
print(f"Corrected Mass Gap (SU(3)): {mass_gap_SU3_corrected:.3e} GeV")
