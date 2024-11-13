# Solar Energy Efficiency Analysis

This repository contains materials and code for the project titled **"Optimizing Solar Farm Efficiency: An Analysis of Geographic, Technological, and Temporal Influences."** The project explores various factors influencing solar energy efficiency, including geographic location, technological advancements, and time-based trends, with a focus on solar farms in Southern China and the United States.

## Project Overview

Inspired by large-scale sustainability efforts, such as the 2024 Super Bowl powered entirely by renewable energy, this study aims to uncover patterns and insights into the effectiveness of solar farms. By examining geographic distributions, environmental conditions, and technological variables, we aim to optimize solar farm performance and enhance predictive capabilities for future solar energy trends.

## Repository Structure

- **Distributed PV Operation Data**: Datasets containing sunshine, temperature, and wind data for distributed PV systems.
- **EV Dataset**: Data related to electric vehicles, including general electric vehicle population and specific vehicle dataset for trend comparison.
- **Photovoltaic Power Generation Data**: Data from Southern China solar farms, including figures and explanations of key parameters.
- **Renewable Energy Worldwide**: Global renewable energy statistics (1965-2022), including solar energy consumption, production, and installed capacity.
- **United States Large-Scale Solar Photovoltaic Database**: A detailed dataset on large-scale solar installations in the United States.

## Analysis Components

1. **Geospatial Analysis**: Using `GeoPandas` to examine spatial distribution of solar farms and their proximity to coastlines and urban centers.
2. **Predictive Modeling**: Built using linear regression and Ordinary Least Squares (OLS) models to forecast solar efficiency trends based on historical data.
3. **Temporal Trends**: Analysis of changes in solar farm area, capacity growth, and efficiency from 1986 to present, highlighting key developments and future projections.
4. **Technological Insights**: Evaluating the impact of technical parameters like panel orientation, material type, and the integration of battery storage on performance.
5. **Policy Impact**: Exploration of how supportive policy frameworks contribute to solar energy expansion and efficiency improvements.

## Key Results

- **Solar Farm Trends**: Notable fluctuations in solar farm area and efficiency ratios over time, with a significant rise in efficiency predicted for 2026.
- **Geographic Influence**: Location plays a critical role in efficiency, with coastal and high-sunlight areas showing improved energy output.
- **Technological Optimization**: Advances in solar panel materials and battery integration correlate with enhanced energy output per unit area.

## Future Directions

- **Enhanced Data Sources**: Leveraging satellite imagery, IoT sensors, and big data for more accurate energy forecasting.
- **Advanced Modeling Techniques**: Integration of machine learning models for predicting long-term solar efficiency trends.
- **Location Selection Optimization**: Using sophisticated geospatial tools for selecting solar farm locations with optimal sunlight exposure and environmental conditions.

## Getting Started

To get started with the code, open the `gear.ipynb` notebook, which includes a step-by-step implementation of the analysis described in the poster presentation.

## Dependencies

- `Python 3.x`
- `pandas`
- `matplotlib`
- `GeoPandas`

Install dependencies with:

```bash
pip install pandas matplotlib geopandas
```

## Authors

- Haohui Zheng
- Shentong Li
