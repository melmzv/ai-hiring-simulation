# AI-Based Job Matching Simulation for Labor Market Research

This repository contains a fully reproducible Python-based prototype that simulates AI-assisted job matching in the labor market. It is designed as the empirical foundation for a seminar paper on **AI and management practices** as part of the course Advanced Topics in Management.

The simulation is motivated by recent work on algorithmic recommendations and labor market frictions (e.g., Le Barbanchon et al., 2023). It is adaptable to both synthetic and real-world data (e.g., O*NET, unemployment or wage statistics) and provides a flexible foundation for research into modern hiring practices, job seeker inequality, and the effectiveness of AI in search and matching.

# 🧠 What Does This Repo Do?

- Generates synthetic job seekers and job postings with skill profiles
- Simulates AI-driven vs. manual job recommendation systems
- Assigns applications and job outcomes based on match quality
- Stores outcome data in tidy `.parquet` format
- Can be extended to include real data from O*NET, unemployment statistics, or wage surveys

# 🧱 Simulation Results

This section presents the simulation results from the Python prototype that models the impact of AI-driven job recommendations on labor market outcomes. The aim is to explore whether personalized recommendations can lead to improved job matching, retention, and wage outcomes.

Inspired by Le Barbanchon et al. (2023), the simulation mimics a two-sided market where job seekers and vacancies are randomly assigned to control or treatment groups. The treatment group receives AI-generated recommendations based on cosine similarity scores across skill profiles. Each simulation run is stochastic by design: job offers and acceptance decisions depend on probabilistic matching scores and preference alignment. As a result, you may observe slightly different outcomes across multiple executions — this is expected and part of the experiment's flexible nature.

The simulation also allows for subgroup analysis by distinguishing between low-skilled and high-skilled workers, revealing heterogeneous treatment effects.

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

The effect is particularly pronounced among low-skilled individuals — AI recommendations help them catch up in terms of match quality, stability, and wage. These findings are consistent with the heterogeneity insights reported in Le Barbanchon et al. (2023).

## 📈 Visual Output

<p align="center">
  <img src="figures/Screenshot 2025-06-18 at 21.56.13.png" alt="Bar Chart: Retention and Wage (Single Run)" width="700"/>
  <br><em><strong>Figure 1:</strong> Bar chart comparing retention rate and average wage in a single simulation run. Individuals who received AI-generated job recommendations (treated group) had a substantially higher retention rate (≈92.9%) than those in the control group (≈78.4%). Their average wage was also significantly higher (≈€47,911 vs. €44,048). This illustrates the expected direction of the AI treatment effect on both job stability and economic reward—even though the magnitude can vary across runs.</em>
</p>

<p align="center">
  <img src="figures/Screenshot 2025-06-18 at 21.56.40.png" alt="Box Plot: 100 Simulations" width="900"/>
  <br><em><strong>Figure 2:</strong> Box plots comparing the distribution of three key metrics—match score, retention, and wage—across 100 independent simulation runs. Treated individuals consistently outperform the control group across all dimensions. Notably, the interquartile ranges of the treated group are tighter for match scores, suggesting more reliable targeting by the AI. Retention and wage distributions also show favorable medians and reduced lower-end outliers in the treated group, indicating that AI not only improves outcomes on average but also reduces downside risk.</em>
</p>

## Summary

This simulation shows that the prototype behaves as designed: it successfully captures AI recommendation effects on job matching outcomes. The results replicate core insights from Le Barbanchon et al. (2023) in a stylized setting and can be extended further. The flexible simulation design also enables subgroup comparisons, robustness checks, and further customization for research purposes.

# How to Reproduce the Simulation Output

To reproduce the simulation results for this project, follow these steps:
1. Clone the repository
2. Create a virtual environment
3. Install dependencies by running `pip install -r requirements.txt` in the terminal
4. Run `make all` in the terminal

# 📚 Suggested Readings
	•	Cowgill, B., & Perkowski, P. (2024). Delegation in hiring: Evidence from a two-sided audit. Journal of Political Economy Microeconomics, 2(4), 852–882. https://doi.org/10.1086/732127
	•	Le Barbanchon, T., Hensvik, L., & Rathelot, R. (2023). How can AI improve search and matching? Evidence from 59 million personalized job recommendations. SSRN Working Paper No. 4604814. https://ssrn.com/abstract=4604814
	•	Miklós-Thal, J., & Tucker, C. (2019). Collusion by algorithm: Does better demand prediction facilitate coordination between sellers? Management Science, 65(4), 1552–1561. https://doi.org/10.1287/mnsc.2019.3287