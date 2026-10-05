# Time-Series Forecasting

Forecast a univariate or small multivariate series with proper temporal validation.

**Points: 12**

---

## Task

1. **Data (3 pts)** — Public time series (energy, weather, finance sample, retail). Document frequency, missing timestamps, seasonality clues.
2. **Baselines (4 pts)** — Implement at least two of: naive/seasonal naive, ARIMA/ETS/Prophet, or an ML model with lag features.
3. **Validation (5 pts)** — Use **walk-forward** (rolling/expanding) validation — not a random shuffle. Report MAE/RMSE (and MAPE if scale-appropriate).
4. **Analysis (3 pts)** — Plot forecasts vs actuals; discuss residual patterns and when the model fails (regime changes, holidays, outliers).

## Deliverables

- Code + metrics table across folds
- Forecast plots
- Short model comparison conclusion
