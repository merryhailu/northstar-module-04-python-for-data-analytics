FinFlow Customer Churn Analysis

1. What Is This?

This project was completed as part of a Northstar analytics engagement for FinFlow, led by Hannah Whitford, with findings prepared for Lina, VP of Product at FinFlow. The project analyzes customer churn patterns and delivers a Jupyter Notebook, an interactive six-chart HTML dashboard, and a product-focused memo with actionable retention recommendations.

2. What's in the Folder?

generate_finflow_data.py – Python script used to generate the synthetic customer dataset.

finflow-enriched-200k.csv – Faker-generated customer dataset modeled after the FinFlow schema.

finflow_churn_analysis_final.ipynb – Jupyter Notebook containing data preparation, exploratory analysis, visualizations, and findings.

finflow-churn-dashboard.html – Interactive dashboard combining six customer churn visualizations.

finflow_product_memo.md – Stakeholder memo summarizing key findings, recommendations, data limitations, and the AI Use Note.

3. How to Reproduce the Analysis

Activate the Conda environment: conda activate northstar.

Run generate_finflow_data.py to generate the synthetic customer dataset.

Open finflow_churn_analysis_final.ipynb in Jupyter Notebook or VS Code.

Run the notebook cells from top to bottom to reproduce the analysis and visualizations.

Open finflow-churn-dashboard.html in a web browser to explore the interactive dashboard.

Note: Keep the CSV, generation script, notebook, and dashboard in the expected project locations so that file paths resolve correctly.

4. Headline Findings

Basic-tier customers have the highest churn rate at 25.08%, compared with 14.86% for Pro and 4.96% for Enterprise. Enterprise customers demonstrate the strongest retention, with 95.04% remaining active. These findings highlight Basic-tier retention as the primary opportunity for FinFlow to improve customer retention.

AI Use Note: AI was used during this engagement. Full details live in the AI Use Note section of finflow_product_memo.md.
