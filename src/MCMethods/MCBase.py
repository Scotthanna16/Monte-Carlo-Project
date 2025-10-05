from abc import ABC, abstractmethod


class MCBase(ABC):
    """
    Abstract base class for Monte Carlo simulation methods.

    This class provides the common interface and functionality that all
    Monte Carlo methods must implement. It handles the setup and execution
    of simulations.
    """

    def __init__(self) -> None:
        """Initialize the Monte Carlo method with default parameters."""
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
