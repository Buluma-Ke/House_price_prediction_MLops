import os
import glob
import zipfile
from abc import ABC, abstractmethod

import pandas as pd


# Abstract class for Data ingestior
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a given file"""
        pass


# Implement a concrete class for ZIP Ingestion
class ZipDataIngestion(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extracts a .zip file and returns the contents as a pandas DataFrame."""
        # Ensure the file is a .zip
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file")
        
        # Extract the zip file 
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # find the extraxcted CSV file (assuming there is one CSV file inside the zip)
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found in the extracted data.")
        
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found. please specify which one to use")
        else:
            # Read the CSV into a DataFrame
            csv_file_path = os.path.join("extracted_data", csv_files[0])
            df = pd.read_csv(csv_file_path)


        # Return the DataFrame 
        return df
    

# Implement a Factory to create Data Ingestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on file extensions."""
        if file_extension == ".zip":
            return ZipDataIngestion
        else:
            raise ValueError(f"No ingestor for file extension: {file_extension}")
        

# Example usage:
if __name__ == "__main__":
    # # Specify the file path
    # file_path = "/Users/Buluma/Documents/house_price_predictions/prices-prediction"

    # # Determin file extension
    #file_extension = os.path.splitext(file_path)[1]

    # # Get appropriate data insgestor 
    #data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # # Now df contains DataFrame from the exracted csv
    # print(df.head()) # Display the first few rows of the DataFrame
    pass 