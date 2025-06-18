# --- Header -------------------------------------------------------------------
# Automates running AI job matching simulation and generating outcomes
# If you are new to Makefiles: https://makefiletutorial.com
# (C) Mel Mzv - See LICENSE file for details
# ------------------------------------------------------------------------------

OUTCOME_DATA := data/generated/simulated_outcomes.parquet

.PHONY: all clean very-clean

all: $(OUTCOME_DATA)

# Run simulation script to generate outcomes
$(OUTCOME_DATA): code/python/ai_job_matching_simulation.py
	mkdir -p data/generated
	python $<

# Clean output data
clean:
	rm -f $(OUTCOME_DATA)

# Clean everything including pulled data (if added later)
very-clean: clean
	rm -rf data/pulled