from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Abstract class for univariate analysis method
# ---------------------------------------------
# This class defines a common interface for univariate anaysis strategies
# Subclasses must implement the Analyze method
class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Performs univariate analysis on a specific feature of the dataframe

        Parameters:
        df (pd.DataFrame): The dataframe containing the data
        Feature (str) : The name of the feature/ column to be analysed
        
        Returns:
        None: This method visualises the distribution of the feature
        """
        pass


# concrete strategy for numerical features
# ----------------------------------------
# This strategy analyses numerical features by plotting their Distribution
class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Plots the distribution of numerical features using Histogram and KDE

        Parameters:
        df (pd.DataFrame): The dataframe containing the data
        Feature (str) : The name of the numerical feature/ column to be analysed
        
        Returns:
        None: Displays a histogram with a KDE plot.
        """

        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()

# concrete strategy for categorical features
# ----------------------------------------
# This strategy analyses categorical features by plotting their  frequency Distribution
class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Plots distribution of a categorical feature using a bar plot

        Parameters:
        df (pd.DataFrame): The dataframe containing the data
        Feature (str) : The name of the categorical feature/column to be analysed
        
        Returns:
        None: Displays a bar plot showing the frequency of each category 
        """

        plt.figure(figsize=(10, 6))
        sns.countplot(x=feature, data=df, palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("count")
        plt.xticks(rotation=45)
        plt.show()

# Context class that uses a DataInspectionStrategy
# ------------------------------------------------
# Allows you to switch between different data inspection strategies
class Analysis:
    def __init__(self, strategy: UnivariateAnalysisStrategy):
        """
        Initialises the Analysis with a specific inspection

        Parameters:
        strategy (UnvariateAnalysisStrategyy): The strategy to be used

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        """
        Sets a new strategy for the Analysis.

        Parameters:
        Strategy (UnvariateAnalysisStrategy): The new strategy to be implemented

        Returns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrames): The dataframe to be inspected.

        Returns:
        None: Executes the strategys inspection method.
        """
        self._strategy.analyze(df, feature)

# Example Usage
if __name__ == "__main__":
    # Example

    #load the data
    #df = pd.read_csv(...data/housing.csv)

    # Initialize the Data inspector with a specific strategy
    # inspector.set_strategy(CategoricalUnivariateAnalysis)
    # inspector.execute_inspection(df)

    # Change strategy to summary Statistics and execute
    # inspector.set_strategy(NumericalUnivariateAnalysis)
    # inspector.execute_inspection(df)
    pass
