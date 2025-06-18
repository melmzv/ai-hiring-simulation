import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
import random

# Cell 1: Set random seed for reproducibility: ensures consistent simulation results across runs
np.random.seed(42)

# Cell 2: Generate Synthetic Job Seekers
n_users = 200
skills = ['Python', 'Excel', 'Sales', 'Writing', 'Data Analysis', 'Marketing', 'Machine Learning', 'SQL', 'Communication', 'Management']

user_profiles = pd.DataFrame({
    'user_id': range(n_users),
    'treated': np.random.binomial(1, 0.5, n_users)  # 50% treated
})

# Assign random skill ratings (0-1)
for skill in skills:
    user_profiles[skill] = np.random.rand(n_users)

# Cell 3: Generate Synthetic Job Listings
n_jobs = 50
job_profiles = pd.DataFrame({
    'job_id': range(n_jobs)
})

for skill in skills:
    job_profiles[skill] = np.random.rand(n_jobs)

# Cell 4: Recommendation Function Using Cosine Similarity
user_skill_matrix = user_profiles[skills].values
job_skill_matrix = job_profiles[skills].values

# Normalize for cosine similarity
user_skill_matrix = normalize(user_skill_matrix)
job_skill_matrix = normalize(job_skill_matrix)

similarity_matrix = cosine_similarity(user_skill_matrix, job_skill_matrix)

# Recommend top-1 job to each treated user
user_profiles['recommended_job'] = -1
for i in range(n_users):
    if user_profiles.loc[i, 'treated'] == 1:
        recommended_job = np.argmax(similarity_matrix[i])
        user_profiles.loc[i, 'recommended_job'] = recommended_job

# Cell 5: Simulate Applications and Outcomes
def simulate_outcomes(user, recommended_job_id):
    # Application probability is higher if job is recommended and similar
    job_pool = list(range(n_jobs))
    if user['treated'] == 1 and recommended_job_id != -1:
        applied_job = recommended_job_id
        job_match_score = similarity_matrix[int(user['user_id']), int(applied_job)]
    else:
        applied_job = random.choice(job_pool)
        job_match_score = similarity_matrix[int(user['user_id']), int(applied_job)]
    
    # Higher match score → better retention and wage
    retention = np.random.binomial(1, job_match_score)
    wage = 25000 + job_match_score * 25000 + np.random.normal(0, 2000)
    
    return pd.Series([applied_job, job_match_score, retention, wage])

user_profiles[['applied_job', 'match_score', 'retained', 'wage']] = user_profiles.apply(
    lambda u: simulate_outcomes(u, u['recommended_job']), axis=1
)

# Cell 6: Results Overview
grouped = user_profiles.groupby('treated').agg({
    'match_score': 'mean',
    'retained': 'mean',
    'wage': 'mean'
}).rename(index={0: 'Control', 1: 'Treated'})

print("Outcome Comparison:\n")
print(grouped)

# Cell 6.1: Subgroup Analysis (Low Skill vs High Skill)

# Sum total skill score
user_profiles['skill_total'] = user_profiles[skills].sum(axis=1)

# Define subgroup: arbitrary threshold, e.g. total skill < 5 = low skill
user_profiles['skill_group'] = np.where(user_profiles['skill_total'] < 5, 'Low Skill', 'High Skill')

# Analyze outcomes by skill group and treatment
subgroup_results = user_profiles.groupby(['skill_group', 'treated']).agg({
    'match_score': 'mean',
    'retained': 'mean',
    'wage': 'mean'
}).rename(index={0: 'Control', 1: 'Treated'})

print("\nSubgroup Comparison:\n")
print(subgroup_results)

# Save simulated outcomes
user_profiles.to_parquet("data/generated/simulated_outcomes.parquet", index=False)

# Cell 7: Visualization
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Retention
axs[0].bar(['Control', 'Treated'], grouped['retained'], color=['gray', 'green'])
axs[0].set_title('Retention Rate')
axs[0].set_ylim(0, 1)

# Wage
axs[1].bar(['Control', 'Treated'], grouped['wage'], color=['gray', 'green'])
axs[1].set_title('Average Wage')

plt.tight_layout()
plt.show()

# Cell 8: Multiple Simulation Runs
n_runs = 100
results = []

for _ in range(n_runs):
    # Re-generate treatment assignment
    user_profiles['treated'] = np.random.binomial(1, 0.5, n_users)

    # Recompute recommendations
    user_profiles['recommended_job'] = -1
    for i in range(n_users):
        if user_profiles.loc[i, 'treated'] == 1:
            recommended_job = np.argmax(similarity_matrix[i])
            user_profiles.loc[i, 'recommended_job'] = recommended_job

    # Re-simulate outcomes
    user_profiles[['applied_job', 'match_score', 'retained', 'wage']] = user_profiles.apply(
        lambda u: simulate_outcomes(u, u['recommended_job']), axis=1
    )

    # Store aggregated result for this run
    grouped = user_profiles.groupby('treated').agg({
        'match_score': 'mean',
        'retained': 'mean',
        'wage': 'mean'
    }).rename(index={0: 'Control', 1: 'Treated'})

    grouped['group'] = grouped.index
    results.append(grouped.reset_index(drop=True))

# Combine results from all runs
results_df = pd.concat(results, ignore_index=True)

# Cell 9: Plot Boxplots Across Runs
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

metrics = ['match_score', 'retained', 'wage']
titles = ['Match Score', 'Retention Rate', 'Average Wage']

for i, metric in enumerate(metrics):
    axs[i].boxplot([
        results_df[results_df['group'] == 'Control'][metric],
        results_df[results_df['group'] == 'Treated'][metric]
    ], labels=['Control', 'Treated'], patch_artist=True)
    axs[i].set_title(titles[i])

plt.tight_layout()
plt.show()