from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abstract base class for missing values Analysis
# -----------------------------------------------
# This class defines missing values analysis
#  Subclasses must implement the methods to Identify and visualise the missing values
class MissingValuesanalysis(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Performs a complete missing values analysis by Idenifying null vales

        Parameters:
        df (pd.DataFrame): The dataframe to be analysed

        Returns:
        None: This method performs Analysis and Visualysation
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self,df: pd.DataFrame):
        """
        Identifies missing values

        Parameters:
        df (pd.DataFrame): The dataframe to be analysed

        Returns:
        None: This method should prints the count of missing values
        """
        pass
    def  visualize_missing_values(self,df: pd.DataFrame):
        """
        Visualise missing values

        Parameters:
        df (pd.DataFrame): The dataframe to be analysed

        Returns:
        None: This method should prints the count of missing values
        """
        pass

    # Concrete class for Identifying missing values
    # ---------------------------------------------
    # This class implements methods to idenify and visualise missing values
class SimpleMissingValuesAnalysis(MissingValuesanalysis):
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Prints the count of missing values in each column in the dataframe

        Parameters:
        df (pd.DataFrame): The dataframe to be analysed

        Returns:
        None: This method should prints the count of missing values
        """
        print("\nMissing Values count by columns:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

    def visualize_missing_values(self, df: pd.DataFrame):
        """
        Creates  a heatmap to visualize the missing values

        Parameters:
        df (pd.DataFrame): The dataframe to be analysed

        Returns:
        None: Displays a heatmap of missing values
        """ 
        print("\nVisualizing Missing Values")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing values heatmap")
        plt.show()


# Example Usage
if __name__ == "__main___":
    # Exampe usage of the SimpleMissingValuesAnalysis class.

    #load data
    #df = pd.read_csv("..data/housing.csv")

    #Perfrm Missing values analysis
    pass
