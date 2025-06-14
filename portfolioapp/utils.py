import pandas as pd
from typing import Union, List

def format_time_series(data: pd.DataFrame, tickers: Union[str, List[str]],
                       col : str = "Close") -> pd.DataFrame:
    """
    Formats a time series DataFrame with MultiIndex columns to have two columns: 'Date' and the ticker name(s).

    Args:
        data (pd.DataFrame): Input DataFrame with MultiIndex columns.
        tickers (Union[str, List[str]]): Ticker or list of tickers to include in the formatted DataFrame.

    Returns:
        pd.DataFrame: Formatted DataFrame with 'Date' and ticker columns.
    """
    if isinstance(tickers, str):
        tickers = [tickers]

    formatted_data = pd.DataFrame()
    formatted_data = pd.concat([formatted_data, data.loc[:, ("Date", "")].rename("Date")], axis=1)

    for ticker in tickers:
        if (ticker, col) in data.columns:
            temp = data.loc[:, (ticker, col)].rename(ticker)
            formatted_data = pd.concat([formatted_data, temp], axis=1)
        else:
            print(f"Ticker {ticker} not found in the DataFrame.")
            
    formatted_data.set_index("Date", inplace=True)
    formatted_data.index = formatted_data.index.tz_localize(None)  # Remove timezone information if present
    
    return formatted_data
