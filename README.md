# AI-Based Job Matching Simulation for Labor Market Research
The project extends the theoretical and empirical foundations laid out in recent academic work - most notably **Le Barbanchon et al. (2023)** - on the use of algorithmic job recommendation systems to mitigate search frictions in two-sided labor markets. The simulation approximates a stylized version of a randomized controlled trial in which AI-based job recommendations are evaluated against traditional search mechanisms.

The motivation behind this prototype is twofold: first, to critically examine how AI tools reshape managerial decision-making and hiring practices; second, to explore their implications for job seekers, especially future graduates, navigating increasingly complex, tech-mediated labor markets. In line with the seminar’s learning goals, this prototype not only simulates algorithmic impact on match quality, retention, and wages, but also provides an extendable framework for analyzing equity and effectiveness in digital recruitment ecosystems.

The simulation is designed to be modular and adaptable: it runs on synthetic data but can easily be extended to integrate real-world datasets (e.g., **O\*NET**, **LEHD**, or wage records). The aim is to equip management researchers with a transparent, replicable foundation to investigate how data-driven matching technologies alter employment dynamics - whether for efficiency, fairness, or both.

# 🧠 What Does This Repo Do?

- Generates synthetic job seekers and job postings with skill profiles
- Simulates AI-driven vs. manual job recommendation systems
- Assigns applications and job outcomes based on match quality
- Stores outcome data in tidy `.parquet` format
- Can be extended to include real data from O*NET, unemployment statistics, or wage surveys

# 🧱 Simulation Results

This section presents the simulation results from the Python prototype that models the impact of AI-driven job recommendations on labor market outcomes. The aim is to explore whether personalized recommendations can lead to improved job matching, retention, and wage outcomes.

Inspired by Le Barbanchon et al. (2023), the simulation mimics a two-sided market where job seekers and vacancies are randomly assigned to control or treatment groups. The treatment group receives AI-generated recommendations based on cosine similarity scores across skill profiles. Each simulation run is stochastic by design: job offers and acceptance decisions depend on probabilistic matching scores and preference alignment. As a result, you may observe slightly different outcomes across multiple executions - this is expected and part of the experiment's flexible nature.

The simulation also allows for subgroup analysis by distinguishing between low-skilled and high-skilled workers, revealing heterogeneous treatment effects. Simulated wages are denominated in USD, reflecting typical U.S. labor market conditions.

## 📊 Outcome Comparison

The table below compares average outcomes between the control and treated groups across three dimensions:

- `match_score`: the cosine similarity between the worker’s skill profile and the job.
- `retained`: whether the match resulted in a long-term placement.
- `wage`: the simulated annual wage in USD.

| Treated Group | Match Score | Retained | Wage (USD) |
|---------------|-------------|----------|------------|
| Control       | 0.7656      | 0.7843   | 44,048     |
| Treated       | 0.9193      | 0.9286   | 47,911     |

Treated individuals receive better matches (higher similarity), are more likely to be retained, and earn higher wages. This supports the idea that AI recommendations enhance job alignment and career outcomes.

## 📊 Subgroup Comparison

Subgroup-level results help unpack heterogeneity in treatment effects:

| Skill Group | Treated Group | Match Score | Retained | Wage (USD) |
|-------------|----------------|-------------|----------|------------|
| High Skill  | Control        | 0.7957      | 0.8462   | 45,001     |
| High Skill  | Treated        | 0.9244      | 0.9565   | 48,111     |
| Low Skill   | Control        | 0.7342      | 0.7200   | 43,057     |
| Low Skill   | Treated        | 0.9148      | 0.9038   | 47,734     |

The low-skilled group experienced the largest **relative gains**, especially in retention and wage outcomes. This supports the hypothesis developed in the seminar paper: AI recommendations are particularly effective for job seekers facing greater frictions. These results align with the heterogeneity patterns observed in Le Barbanchon et al. (2023), suggesting that personalized algorithmic tools can mitigate disadvantages in job matching for vulnerable groups.

## 📈 Visual Output

<p align="center">
  <img src="data/generated/Figure_1.png" alt="Bar Chart: Retention and Wage (Single Run)" width="700"/>
  <br><em><strong>Figure 1:</strong> Bar chart comparing retention rate and average wage in a single simulation run. Individuals who received AI-generated job recommendations (treated group) had a substantially higher retention rate (≈92.9%) than those in the control group (≈78.4%). Their average wage was also significantly higher (≈$47,911 vs. $44,048). This illustrates the expected direction of the AI treatment effect on both job stability and economic reward - even though the magnitude can vary across runs.</em>
</p>

<p align="center">
  <img src="data/generated/Figure_2.png" alt="Box Plot: 100 Simulations" width="900"/>
  <br><em><strong>Figure 2:</strong> Box plots comparing the distribution of three key metrics - match score, retention, and wage - across 100 independent simulation runs. Treated individuals consistently outperform the control group across all dimensions. Notably, the interquartile ranges of the treated group are tighter for match scores, suggesting more reliable targeting by the AI. Retention and wage distributions also show favorable medians and reduced lower-end outliers in the treated group, indicating that AI not only improves outcomes on average but also reduces downside risk.</em>
</p>

## Summary

This simulation shows that the prototype behaves as designed: it successfully captures AI recommendation effects on job matching outcomes. The results replicate core insights from Le Barbanchon et al. (2023) in a stylized setting and can be extended further. The flexible simulation design also enables subgroup comparisons, robustness checks, and further customization for research purposes.

Having ideas or fixes? Contributions are welcome! :raised_hands:

# How to Reproduce the Simulation Output

To reproduce the simulation results for this project, follow these steps:
1. Clone the repository
2. Create a virtual environment with `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies by running `pip install -r requirements.txt` in the terminal
4. Run `make all` in the terminal


# 📚 Suggested Readings & References
-	Cowgill, B., & Perkowski, P. (2024). Delegation in hiring: Evidence from a two-sided audit. Journal of Political Economy Microeconomics, 2(4), 852–882. https://doi.org/10.1086/732127
-	Le Barbanchon, T., Hensvik, L., & Rathelot, R. (2023). How can AI improve search and matching? Evidence from 59 million personalized job recommendations. SSRN Working Paper No. 4604814. https://ssrn.com/abstract=4604814
-	Miklós-Thal, J., & Tucker, C. (2019). Collusion by algorithm: Does better demand prediction facilitate coordination between sellers? Management Science, 65(4), 1552–1561. https://doi.org/10.1287/mnsc.2019.3287

# Licensing
The repository is licensed under the MIT license.