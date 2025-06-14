import numpy as np
import pandas as pd
import yfinance as yf
from typing import Union


def get_monthly_sharpe(prices: Union[pd.DataFrame, pd.Series], 
                       years : int = 10) -> float:
    
    if isinstance(prices, pd.DataFrame):
        if len(prices.columns) > 1:
            raise ValueError("Input must be a single time series, not a DataFrame with multiple columns.")
    
    
    prices_filter = prices.loc[prices.index >= (pd.Timestamp.now() - pd.DateOffset(years=years))].dropna()
    sharpe = prices_filter.calc_stats().stats.get("monthly_sharpe", None)
    
    return sharpe if sharpe is not None else np.nan


def get_annualized_sharpe(prices: Union[pd.DataFrame, pd.Series], 
                       years : int = 10) -> float:
    
    if isinstance(prices, pd.DataFrame):
        if len(prices.columns) > 1:
            raise ValueError("Input must be a single time series, not a DataFrame with multiple columns.")
    
    prices_filter = prices.loc[prices.index >= (pd.Timestamp.now() - pd.DateOffset(years=years))].dropna()
    sharpe = prices_filter.calc_stats().stats.get("yearly_sharpe", None)
    
    return sharpe if sharpe is not None else np.nan



def get_annualized_volatility(prices: Union[pd.DataFrame, pd.Series], 
                       years : int = 10) -> float:
    
    if isinstance(prices, pd.DataFrame):
        if len(prices.columns) > 1:
            raise ValueError("Input must be a single time series, not a DataFrame with multiple columns.")
    
    prices_filter = prices.loc[prices.index >= (pd.Timestamp.now() - pd.DateOffset(years=years))].dropna()
    sharpe = prices_filter.calc_stats().stats.get("yearly_vol", None)
    
    return sharpe if sharpe is not None else np.nan




def get_max_drawdown(prices: Union[pd.DataFrame, pd.Series], 
                       years : int = 10) -> float:
    
    if isinstance(prices, pd.DataFrame):
        if len(prices.columns) > 1:
            raise ValueError("Input must be a single time series, not a DataFrame with multiple columns.")
    
    prices_filter = prices.loc[prices.index >= (pd.Timestamp.now() - pd.DateOffset(years=years))].dropna()
    sharpe = prices_filter.calc_stats().stats.get("max_drawdown", None)
    
    return sharpe if sharpe is not None else np.nan




def get_all_stats_annualized(prices: Union[pd.DataFrame, pd.Series], years: int = 10) -> pd.DataFrame:
    """
    Calculates all performance stats for a given time series or DataFrame.

    Args:
        prices (Union[pd.DataFrame, pd.Series]): Input time series or DataFrame.
        years (int): Number of years to filter the data.

    Returns:
        pd.DataFrame: DataFrame containing all calculated stats.
    """
    if isinstance(prices, pd.DataFrame):
        if len(prices.columns) > 1:
            raise ValueError("Input must be a single time series, not a DataFrame with multiple columns.")

    # Filter data for the specified number of years
    prices_filter = prices.loc[prices.index >= (pd.Timestamp.now() - pd.DateOffset(years=years))].dropna()

    # Calculate stats using ffn
    stats = prices_filter.calc_stats().stats

    # Extract stats based on the `_stats` structure
    stats_structure = [
        ("start", "Start"),
        ("end", "End"),
        #("rf", "Risk-free rate"),
        ("total_return", "Total Return"),
        ("cagr", "CAGR"),
        ("max_drawdown", "Max Drawdown"),
        ("calmar", "Calmar Ratio"),
        ("yearly_sharpe", "Yearly Sharpe"),
        ("yearly_sortino", "Yearly Sortino"),
        ("yearly_mean", "Yearly Mean"),
        ("yearly_vol", "Yearly Vol"),
        ("yearly_skew", "Yearly Skew"),
        ("yearly_kurt", "Yearly Kurt"),
        ("best_year", "Best Year"),
        ("worst_year", "Worst Year"),
        ("avg_drawdown", "Avg. Drawdown"),
        ("avg_drawdown_days", "Avg. Drawdown Days"),
        ("avg_up_month", "Avg. Up Month"),
        ("avg_down_month", "Avg. Down Month"),
        ("win_year_perc", "Win Year %"),
        ("twelve_month_win_perc", "Win 12m %"),
    ]

    # Create a DataFrame to store the stats
    stats_data = {label: stats.get(key, np.nan) for key, label in stats_structure}
    return pd.DataFrame([stats_data])




def get_all_stats_monthly(prices: Union[pd.DataFrame, pd.Series], years: int = 10) -> pd.DataFrame:
    """
    Calculates all performance stats for a given time series or DataFrame.

    Args:
        prices (Union[pd.DataFrame, pd.Series]): Input time series or DataFrame.
        years (int): Number of years to filter the data.

    Returns:
        pd.DataFrame: DataFrame containing all calculated stats.
    """
    if isinstance(prices, pd.DataFrame):
        if len(prices.columns) > 1:
            raise ValueError("Input must be a single time series, not a DataFrame with multiple columns.")

    # Filter data for the specified number of years
    prices_filter = prices.loc[prices.index >= (pd.Timestamp.now() - pd.DateOffset(years=years))].dropna()

    # Calculate stats using ffn
    stats = prices_filter.calc_stats().stats

    # Extract stats based on the `_stats` structure
    stats_structure = [
        ("start", "Start"),
        ("end", "End"),
        #("rf", "Risk-free rate"),
        ("total_return", "Total Return"),
        ("cagr", "CAGR"),
        ("max_drawdown", "Max Drawdown"),
        ("calmar", "Calmar Ratio"),
        ("monthly_sharpe", "Monthly Sharpe"),
        ("monthly_sortino", "Monthly Sortino"),
        ("monthly_mean", "Monthly Mean"),
        ("monthly_vol", "Monthly Vol"),
        ("monthly_skew", "Monthly Skew"),
        ("monthly_kurt", "Monthly Kurt"),
        ("best_month", "Best Month"),
        ("worst_month", "Worst Month"),
        ("avg_drawdown", "Avg. Drawdown"),
        ("avg_drawdown_days", "Avg. Drawdown Days"),
        ("avg_up_month", "Avg. Up Month"),
        ("avg_down_month", "Avg. Down Month"),
        ("win_year_perc", "Win Year %"),
        ("twelve_month_win_perc", "Win 12m %"),
    ]

    # Create a DataFrame to store the stats
    stats_data = {label: stats.get(key, np.nan) for key, label in stats_structure}
    return pd.DataFrame([stats_data])



def get_all_stats_daily(prices: Union[pd.DataFrame, pd.Series], years: int = 10) -> pd.DataFrame:
    """
    Calculates all performance stats for a given time series or DataFrame.

    Args:
        prices (Union[pd.DataFrame, pd.Series]): Input time series or DataFrame.
        years (int): Number of years to filter the data.

    Returns:
        pd.DataFrame: DataFrame containing all calculated stats.
    """
    if isinstance(prices, pd.DataFrame):
        if len(prices.columns) > 1:
            raise ValueError("Input must be a single time series, not a DataFrame with multiple columns.")

    # Filter data for the specified number of years
    prices_filter = prices.loc[prices.index >= (pd.Timestamp.now() - pd.DateOffset(years=years))].dropna()

    # Calculate stats using ffn
    stats = prices_filter.calc_stats().stats

    # Extract stats based on the `_stats` structure
    stats_structure = [
        ("start", "Start"),
        ("end", "End"),
        #("rf", "Risk-free rate"),
        ("total_return", "Total Return"),
        ("cagr", "CAGR"),
        ("max_drawdown", "Max Drawdown"),
        ("calmar", "Calmar Ratio"),
        ("daily_sharpe", "Daily Sharpe"),
        ("daily_sortino", "Daily Sortino"),
        ("daily_mean", "Daily Mean"),
        ("daily_vol", "Daily Vol"),
        ("daily_skew", "Daily Skew"),
        ("daily_kurt", "Daily Kurt"),
        ("best_day", "Best Day"),
        ("worst_day", "Worst Day"),
        ("avg_drawdown", "Avg. Drawdown"),
        ("avg_drawdown_days", "Avg. Drawdown Days"),
        ("avg_up_month", "Avg. Up Month"),
        ("avg_down_month", "Avg. Down Month"),
        ("win_year_perc", "Win Year %"),
        ("twelve_month_win_perc", "Win 12m %"),
    ]

    # Create a DataFrame to store the stats
    stats_data = {label: stats.get(key, np.nan) for key, label in stats_structure}
    return pd.DataFrame([stats_data])



def get_all_stats_annualized_df(prices: pd.DataFrame, years: int = 10) -> pd.DataFrame:
    """
    Generates a DataFrame containing stats for each ticker in the input DataFrame.

    Args:
        prices (pd.DataFrame): Input DataFrame with tickers as columns.
        years (int): Number of years to filter the data.

    Returns:
        pd.DataFrame: DataFrame containing stats for each ticker.
    """
    all_stats = []

    for ticker in prices.columns:
        try:
            ticker_stats = get_all_stats_annualized(prices[ticker], years=years)
            ticker_stats["Ticker"] = ticker
            all_stats.append(ticker_stats)
        except Exception as e:
            print(f"Error processing stats for {ticker}: {e}")

    table = pd.concat(all_stats, ignore_index=True)
    table.set_index("Ticker", inplace=True)
    return table



def get_all_stats_monthly_df(prices: pd.DataFrame, years: int = 10) -> pd.DataFrame:
    """
    Generates a DataFrame containing stats for each ticker in the input DataFrame.

    Args:
        prices (pd.DataFrame): Input DataFrame with tickers as columns.
        years (int): Number of years to filter the data.

    Returns:
        pd.DataFrame: DataFrame containing stats for each ticker.
    """
    all_stats = []

    for ticker in prices.columns:
        try:
            ticker_stats = get_all_stats_monthly(prices[ticker], years=years)
            ticker_stats["Ticker"] = ticker
            all_stats.append(ticker_stats)
        except Exception as e:
            print(f"Error processing stats for {ticker}: {e}")

    table = pd.concat(all_stats, ignore_index=True)
    table.set_index("Ticker", inplace=True)
    return table



def get_all_stats_daily_df(prices: pd.DataFrame, years: int = 10) -> pd.DataFrame:
    """
    Generates a DataFrame containing stats for each ticker in the input DataFrame.

    Args:
        prices (pd.DataFrame): Input DataFrame with tickers as columns.
        years (int): Number of years to filter the data.

    Returns:
        pd.DataFrame: DataFrame containing stats for each ticker.
    """
    all_stats = []

    for ticker in prices.columns:
        try:
            ticker_stats = get_all_stats_daily(prices[ticker], years=years)
            ticker_stats["Ticker"] = ticker
            all_stats.append(ticker_stats)
        except Exception as e:
            print(f"Error processing stats for {ticker}: {e}")

    table = pd.concat(all_stats, ignore_index=True)
    table.set_index("Ticker", inplace=True)
    return table