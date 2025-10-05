from abc import ABC, abstractmethod
import numpy as np
from numpy import random


class MCBase(ABC):
    """
    Abstract base class for Monte Carlo simulation methods.

    This class provides the common interface and functionality that all
    Monte Carlo methods must implement. It handles the setup and execution
    of simulations.
    """

    def __init__(self, S0, r, sigma, T, n_steps, payoff, seed=None) -> None:
        """Initialize the Monte Carlo method with default parameters."""
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.n_steps = n_steps
        self.payoff = payoff
        self.dt = T / n_steps
        if seed:
            self.rng = np.random.default_rng(seed)
        self.simulation_results = []

    @abstractmethod
    def run_simulation(self, num_simulations: int) -> None:
        """
        Run the Monte Carlo simulation.

        This method must be implemented by all concrete Monte Carlo method classes.
        It executes the simulation for a specified number of iterations.

        Args:
            num_simulations: Number of simulations to run

        Raises:
            NotImplementedError: If not implemented by subclass
        """
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def get_results(self) -> list:
        """
        Retrieve the results of the Monte Carlo simulation.

        This method must be implemented by all concrete Monte Carlo method classes.
        It returns the results collected from the simulations.

        Returns:
            List of simulation results

        Raises:
            NotImplementedError: If not implemented by subclass
        """
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def get_average_result(self) -> float:
        """
        Calculate the average result from the simulation results.

        This method computes the mean of the results obtained from the simulations.

        Returns:
            The average of the simulation results
        """
        raise NotImplementedError("Subclasses must implement this method")
