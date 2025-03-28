import numpy as np

# -------------------------------
# Constants
# -------------------------------
k_B = 1.380649e-23  # Boltzmann constant (J/K)
T_quantum = 1e12    # Effective temperature for quantum regime (K)
T_macro = 1e3       # Effective temperature for macro regime (K)

# -------------------------------
# Entropy Calculations
# -------------------------------
def entropy(probabilities, epsilon=1e-10):
    """
    Calculate entropy using the probability distribution.
    :param probabilities: Array of probabilities (should sum to 1).
    :param epsilon: Small constant to prevent divide-by-zero errors in log.
    :return: Entropy (in J/K).
    """
    probabilities = np.array(probabilities)
    probabilities += epsilon  # Add epsilon to prevent zero probabilities
    return -k_B * np.sum(probabilities * np.log(probabilities))

# -------------------------------
# Energy Cost Calculation
# -------------------------------
def determinism_cost(prob_stochastic, prob_deterministic, T):
    """
    Calculate the energy cost of determinism based on entropy change.
    :param prob_stochastic: Probability distribution in stochastic regime.
    :param prob_deterministic: Probability distribution in deterministic regime.
    :param T: Effective temperature of the system (K).
    :return: Energy cost (in J).
    """
    S_stochastic = entropy(prob_stochastic)
    S_deterministic = entropy(prob_deterministic)
    delta_S = S_stochastic - S_deterministic
    return T * delta_S

# -------------------------------
# Example Calculations
# -------------------------------
# Define probability distributions
prob_stochastic = [0.25, 0.25, 0.25, 0.25]  # Equal probabilities (high entropy)
prob_deterministic = [0.9, 0.1, 0.0, 0.0]   # Concentrated probabilities (low entropy)

# Calculate determinism costs for quantum and macro scales
E_cost_quantum = determinism_cost(prob_stochastic, prob_deterministic, T_quantum)
E_cost_macro = determinism_cost(prob_stochastic, prob_deterministic, T_macro)

print(f"Determinism Cost (Quantum Scale): {E_cost_quantum:.3e} J")
print(f"Determinism Cost (Macro Scale): {E_cost_macro:.3e} J")
