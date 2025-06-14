from typing import List, Dict, Any

import os
import pandas as pd
import yfinance as yf
import ffn


def _fetch_stock_data(ticker : str) -> Dict[str, Any]:
    
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        history = stock.history(period="max")
        return info, history
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None, None
        
        

def _fetch_fundamentals(ticker: str) -> Dict[str, Any]:
     
    """
    Fetches fundamental data for a given stock ticker.
    Args:
        ticker (str): Stock ticker symbol.    
    Returns:
        Dict[str, Any]: Dictionary containing fundamental data.
    """
    
    info, _ = _fetch_stock_data(ticker)
    if info is None:
        return None
    
    # Extract relevant fundamental data
    try:
        result = {
            "EPS": info.get("trailingEps"),
            "P/E Ratio": info.get("trailingPE"),
            "P/B Ratio": info.get("priceToBook"),
            "EV/EBITDA": info.get("enterpriseToEbitda"),
            "ROE (%)": info.get("returnOnEquity", 0) * 100 if info.get("returnOnEquity") else None,
            "Dividend Yield (%)": info.get("dividendYield", 0) * 100 if info.get("dividendYield") else 0,
            "Debt-to-Equity": info.get("debtToEquity")
        }
        return result
    except KeyError as e:
        print(f"Key error for {ticker}: {e}")
        return None
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
    
    
    
    
    

def get_fundamentals_stock_data_batch(tickers : List[str], industries : List[str]) -> pd.DataFrame:
    """ 
    Fetches stock data for a list of tickers and adds the respective industry column.
    """
    # Fetch stock data
    results = []
    for ticker in tickers:
        data = _fetch_fundamentals(ticker)
        if data:
            data['Ticker'] = ticker
            results.append(data)   
        else:
            print(f"No data found for {ticker}")
    
    # Create a DataFrame for stock data
    stock_data_df = pd.DataFrame(results)
    
    industry_df = pd.DataFrame({
        "Ticker": tickers,
        "Industry": industries  
    })
    
    # Merge stock data with industry data
    merged_df = pd.merge(stock_data_df, industry_df, on="Ticker", how="left")
    
    return merged_df




def get_price_series(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """
    Efficiently fetches historical price series for a list of tickers within a specified date range using batch download.

    Returns a long-form DataFrame with columns ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume', ...].
    """
    # Batch download all tickers at once
    raw = yf.download(
        tickers,
        start=start,
        end=end,
        group_by='ticker',
        threads=True,
        auto_adjust=True,
        progress=False
    )

    # If only one ticker, wrap columns to match multi-index structure
    if isinstance(raw.columns, pd.Index):
        # Single ticker case
        df = raw.reset_index()
        df['Ticker'] = tickers[0]
    else:
        # Multiple tickers: raw has MultiIndex columns (type, ticker)
        df = raw.stack(level=1).reset_index().rename(columns={'level_1': 'Ticker'})

    return df