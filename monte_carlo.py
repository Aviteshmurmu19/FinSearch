import numpy as np
def monte_carlo_option_price(S, K, r, sigma, T, num_simulations):    
    option_price_sum = 0
    
    for _ in range(num_simulations):
        z = np.random.standard_normal()
        ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)
        option_price = max(ST - K, 0)
        option_price_sum += option_price
    
    option_price = option_price_sum / num_simulations
    return option_price

# Example usage
S = float(input("Current price of the underlying asset : ")) #100
K = float(input("Strike price of the option : ")) #110
r = float(input("Risk-free interest rate : ")) # 0.05
sigma = float(input("Volatility of the underlying asset : ")) # 0.2
T = int(input("Time to expiration of the option : ")) # 1
num_simulations = int(input("Number of simulations to run : ")) # 100000

option_price = monte_carlo_option_price(S, K, r, sigma, T, num_simulations)
print("Estimated option price:", option_price) # 6.3716403649401965
