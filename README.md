# CPM in DOcplex (LP)

A minimal DOcplex (IBM CPLEX) implementation of the Critical Path Method (CPM) formulated as a Linear Program (LP). The model computes feasible start times for activities and minimizes the overall project completion time under precedence constraints.

## Problem
Given:
- activity durations
- precedence relations (i must finish before j starts)

Find:
- start time of each activity
- minimum project completion time

This is a pure CPM setting (no resource constraints).

## Modeling overview (plain language)
- Decision variables:
  - `s[i]` start time of activity i
  - `time` project completion time
- Objective:
  - minimize `time`
- Constraints:
  - `time >= s[i] + duration[i]` for each activity
  - `s[i] + duration[i] <= s[j]` for each precedence arc (i -> j)



## Install
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
```
## Model Source
Model SOURCE (NEOS Guide case study): https://neos-guide.org/case-studies/sc/mfg/project-scheduling-with-cpm/
