"""Main entry point for regulon_summary analysis."""

import pandas as pd


def main():
    """Main function to run the analysis."""
    # Load the TSV file
    df = pd.read_csv('NetworkRegulatorGene.tsv', sep='\t')
    
    print("Data loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print("\nFirst few rows:")
    print(df.head())


if __name__ == "__main__":
    main()
