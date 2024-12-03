from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# Abstract method class for bivariate analysis
# --------------------------------------------
# This classs defines an interface for bivariate analysis
# Subclasses must implement the analyze method.
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Perorms bivariate analyis on two features of the dataframe

        Parameters:
        df (pd.DataFrame): dataframe containing the data.
        feature1 (str): The name of the first feature/column to be analysed.
        feature2 (str): The name of the second feature/column to be analysed.

        Returns:
        None: This method visualizes the relationship between the two features
        """
        pass

# Concrete Strategy for Numerical vs Numerical Analysis
# -----------------------------------------------------
# Thsis strategy analyzes the relationship between two numerical features
class NumericalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df:pd.DataFrame, feature1: str, feature2: str):
        """
        Plots the relationship between two numerical features

        Parameters:
        df (pd.DataFrame): dataframe containing the data.
        feature1 (str): The name of the first feature/column to be analysed.
        feature2 (str): The name of the second feature/column to be analysed.

        Returns:
        None: Displays a scatter plot showing relationship between two features
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()


# Concrete Strategy for categorical vs Numerical Analysis
# -------------------------------------------------------
# This method analyzes the relationship between a categorical feature and a numerical feature
class CategoricalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Plots the relationship between a categorical and a Numerical features

        Parameters:
        df (pd.DataFrame): dataframe containing the data.
        feature1 (str): The name of the categorical feature/column to be analysed.
        feature2 (str): The name of the Numerical feature/column to be analysed.

        Returns:
        None: Displays a box plot showing relationship between two features
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()

# Context class that uses a DataInspectionStrategy
# ------------------------------------------------
# Allows you to switch between different data inspection strategies
class Bi_Analysis:
    def __init__(self, strategy: BivariateAnalysisStrategy):
        """
        Initialises the BivariateAnalysis with a specific inspection

        Parameters:
        strategy (BivariateAnalysisStrategyy): The strategy to be used

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: BivariateAnalysisStrategy):
        """
        Sets a new strategy for the Analysis.

        Parameters:
        Strategy (BivariateAnalysisStrategy): The new strategy to be implemented

        Returns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrames): The dataframe to be inspected.

        Returns:
        None: Executes the strategys inspection method.
        """
        self._strategy.analyze(df, feature1, feature2)

 # Example Usage
if __name__ == "__main__":
    # Example

    #load the data
    #df = pd.read_csv(...data/housing.csv)

    # Initialize the Data inspector with a specific strategy
    # inspector.set_strategy(CategoricalVsNumericalAnalysis)
    # inspector.execute_inspection(df)

    # Change strategy to summary Statistics and execute
    # inspector.set_strategy(NumericalVsNumericalAnalysis)
    # inspector.execute_inspection(df)
    pass       