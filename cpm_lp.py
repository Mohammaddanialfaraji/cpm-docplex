import numpy as np
np.set_printoptions(threshold=np.inf)
from docplex.mp.model import Model

# -------------------- Sets --------------------
S_activity_name = np.array(["A","B","C","D","E","F","G"], dtype=object)
N_activity = np.arange(len(S_activity_name))
S_activity = len(N_activity)
# -------------------- Parameters --------------------
P_duration = np.array([2, 3, 3, 4, 8, 6, 2], dtype=float)  # A..G
P_prec = np.array([
    [0,1],  # A->B
    [0,2],  # A->C
    [1,5],  # B->F
    [4,5],  # E->F
    [2,3],  # C->D
    [3,4],  # D->E
    [5,6],  # F->G
], dtype=int)

# -------------------- Optimization tool --------------------
Schedule = Model('schedule')
V_time = Schedule.continuous_var(lb=0, name='time')
V_s    = Schedule.continuous_var_list(S_activity, lb=0, name='s')
# -------------------- Constraints --------------------
Schedule.add_constraints(
    V_time >= V_s[i] + P_duration[i]
    for i in range(S_activity)
)
Schedule.add_constraints(
    V_s[i] + P_duration[i] <= V_s[j]
    for (i, j) in P_prec
)
# -------------------- Objective --------------------
Schedule.minimize(V_time)
# -------------------- Solve --------------------
sol = Schedule.solve(log_output=False)
if sol:
    print("time =", V_time.solution_value)
    for i in range(S_activity):
        print(S_activity_name[i], V_s[i].solution_value)
else:
    print("No feasible solution found.")