from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Abstract base class for multivariate Analysis
# ---------------------------------------------
# This class provides a template for performing multivariate analysison the dataframe
# Subclasses can override specific steps like correlation heatmap
class MultivariateAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        perform a comprehensive multivariate analysis by generating a correlation heatmap and pair plot.

        Parameters:
        df (pd.DataFrame): The datafrmae containing the data to be analyzed

        Returns:
        None: This method orchastrates the multivariate analysis process
        """
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)
    
    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """
        Generate and displays a heatmap of correlations beween the each numerical variable with the other in the data frame

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed

        Returns:
        None: This method should generate a display a correlation heatmap
        """
        pass
    @abstractmethod
    def generate_pairplot(self, df:pd.DataFrame):
        """
        Generate and display a pair plot of the selected features

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed

        Returns:
        None: This method should generate and display a pair plot
        """
        pass

# Concree class for Multivariate Analysis with Correlation Heatmap
# ----------------------------------------------------------------
# This method implements the methods to generate a correlation heatmap
class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """
        Generates and displays a correlation heatmap for the numerical features

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed

        Returns
        None: Displays a heatmap showing correlation between Numerical values
        """
        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("correlation heatmap")
        plt.show()
    def generate_pairplot(self, df: pd.DataFrame):
        """
        Generates and displays a pairplot for the selected features

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analysed

        Returns
        None: Displays a paiplot for the selected features
        """
        sns.pairplot(df)
        plt.suptitle("Pair plot of selected features", y=1.02)
        plt.show()

# Example Usage
if __name__ == "__main___":
    # Exampe usage of the SimpleMultivariateAnalysis class.

    #load data
    #df = pd.read_csv("..data/housing.csv")

    # Initialize ...
    # multivariate_analyzer = SimpleMultivariateAnalysis()
    # Execute the multivariate analysis
    # multivariate_analyzer.analyze(selected_features)
    pass
        