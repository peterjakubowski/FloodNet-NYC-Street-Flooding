import pandas as pd


def get_IQR(df: pd.DataFrame) -> pd.Index:
    """Get the indices of the interquartile range (IQR) and remove outliers from a data frame."""
    
    features = []
    for f in df.columns:
        lower = df[f].quantile(0.25)
        upper = df[f].quantile(0.75)
        iqr = upper - lower
        if iqr > 0:
            features.append(f)
        outliers = df[((df[f] < (lower - 1.5 * iqr)) | (df[f] > (upper + 1.5 * iqr)))]
        
        print(f"Found {outliers.shape[0]} outliers in variable {f}.")
        
    n = df[features].shape[0]
    Q1 = df[features].quantile(0.25)
    Q3 = df[features].quantile(0.75)
    IQR = Q3 - Q1
    
    IQR_idx = df[~((df[features] < (Q1 - 1.5 * IQR)) | (df[features] > (Q3 + 1.5 * IQR))).any(axis=1)].index
    
    print(f"Removed {n - len(IQR_idx)} outliers from {n} records, {len(IQR_idx)} records remain.")
    
    return IQR_idx

