# 📊 Portfolio Management with Dynamic Allocation and Leverage Strategies

This repository presents a comprehensive approach to portfolio management, integrating classical Markowitz optimization with advanced techniques such as dynamic allocation, leverage strategies, and the inclusion of patrimonial assets for enhanced stability.

## 📁 Repository Structure

* **`Portfolio.ipynb`**: Main Jupyter Notebook encompassing the entire workflow, from data acquisition to portfolio optimization and performance evaluation.

## 🧠 Key Features

### 1. Data Acquisition and Preprocessing

* Utilizes `yfinance` to fetch historical data for equities and patrimonial assets.
* Calculates daily and log returns.
* Handles missing data and ensures data integrity.

### 2. Markowitz Portfolio Optimization

* Computes expected returns and the covariance matrix.
* Implements the Mean-Variance Optimization model to derive efficient frontiers.
* Identifies optimal portfolios maximizing the Sharpe ratio.

### 3. Dynamic Allocation Strategy

* Rebalances the portfolio every six months to adapt to market changes.
* Recomputes optimal weights based on updated data, ensuring the portfolio remains aligned with the desired risk-return profile.

### 4. Inclusion of Patrimonial Assets

* Incorporates non-equity assets (e.g., bonds, real estate) to construct a more stable and diversified portfolio.
* Aims to reduce volatility and enhance long-term returns.

### 5. Leverage Techniques

* Explores the impact of applying leverage to the portfolio to amplify returns.
* Analyzes the trade-offs between increased returns and heightened risk.

### 6. Dynamic Leverage Based on Portfolio Metrics

* Implements a dynamic leverage strategy that adjusts leverage levels based on portfolio performance metrics.
* Ensures that leverage is applied judiciously, enhancing returns without disproportionately increasing risk.

## 📈 Visualizations

* Efficient frontier plots illustrating the risk-return trade-off.
* Time series plots of portfolio cumulative returns.
* Bar charts depicting asset allocations over time.
* Visual representations of leverage effects on portfolio performance.


## 📦 Environment Setup

To facilitate easy setup of the project environment, two configuration files are provided:

### 🐍 Using `requirements.txt` (pip)

For users preferring `pip`, the `requirements.txt` file lists all necessary Python packages. To install the dependencies:

```bash
pip install -r requirements.txt
```

This will install packages such as:

* `jupyter`, `jupyterlab`, `ipykernel`, `ipywidgets`, `notebook`, `ipython`
* `numpy`, `pandas`, `ffn`, `yfinance`, `seaborn`, `scipy`
* `xgboost`, `scikit-learn`, `scikit-optimize`

### 🐍 Using `env.yml` (conda)

For users utilizing `conda`, the `env.yml` file defines the environment with all required dependencies. To create the environment:

```bash
conda env create -f env.yml
```

This approach ensures that all packages, including those not available through `conda`, are installed via `pip` as specified in the `env.yml` file.



## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/martinpasche/Portfolio-Management.git
   cd Portfolio-Management
   ```