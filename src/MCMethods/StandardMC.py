from MCBase import MCBase
import numpy as np


class StandardMC(MCBase):
    def __init__(self, S0, r, sigma, T, n_steps, payoff, seed=None) -> None:
        super().__init__(S0, r, sigma, T, n_steps, payoff, seed)

    def run_simulation(self, num_simulations: int) -> None:
        self.simulation_results = []
        for _ in range(num_simulations):
            S = self.S0
            for _ in range(self.n_steps * self.T):
                Z = self.rng.normal()
                S *= np.exp(
                    (self.r - 0.5 * self.sigma**2) * self.dt
                    + self.sigma * np.sqrt(self.dt) * Z
                )
            self.simulation_results.append(self.payoff(S))

    def get_results(self) -> list:
        return self.simulation_results

    def get_average_result(self):
        return np.mean(self.simulation_results)


# Simple test
# mc = StandardMC(100, 0.05, 0.2, 1, 100, lambda S: max(S - 100, 0), 42)
# mc.run_simulation(100)
# results = mc.get_results()
# average = mc.get_average_result()
# print(f"Results: {results}")
# print(f"Average Result: {average}")
