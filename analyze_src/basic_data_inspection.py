from abc import ABC, abstractmethod

import numpy as np
import pandas as pd


# Absract Base Class for Data Inspection Strategies
# -------------------------------------------------
# This class defines a common interface for data inspection strategies
# Subclasses must implement the inspect method.
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is to be performed

        Returns:
        None: This method prints the inspection results directly
        """
        pass


# Data types inspection
# ---------------------
# This strategy inspects the data types of each column and count of null values
class DataTypesInspection(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        inpectS and prints the data types and non-null couns for every column

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the data types and non-null counts of the data frame
        """
        print("\nData Types and Non-null Counts:")
        print(df.info())


# Summary Statistics Inspection
# -----------------------------
# This strategy provides summary statistics for both numerical and categorical data
class SummaryStatisticsInspection(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical values

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected

        Returns:
        None: Prints summary statistics console
        """
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features)")
        print(df.describe(include=[object]))


# Context class that uses a DataInspectionStrategy
# ------------------------------------------------
# Allows you to switch between different data inspection strategies
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initialises the DataInspector with a specific inspection

        Parameters:
        strategy (DataInspectionstratey): The strategy to be used

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        Strategy (DataInspectionStrategy): The new strategy to be implemented

        Returns:
        None
        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrames): The dataframe to be inspected.

        Returns:
        None: Executes the strategys inspection method.
        """
        self._strategy.inspect(df)

# Example Usage
if __name__ == "__main__":
    # Example

    #load the data
    #df = pd.read_csv()

    # Initialize the Data inspector with a specific strategy
    # inspector.set_strategy(DataTypeInspection)
    # inspector.execute_inspection(df)

    # Change strategy to summary Statistics and execute
    # inspector.set_strategy(SummaryStatisticsInspection)
    # inspector.execute_inspection(df)
    pass