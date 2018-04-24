
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1/52         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

TRANSITION_MATRIX_NODRUG = [
    [0, 0.0135, 0, 0.01938],
    [0, 0, 52, 0],
    [0, 0.029812, 0, 0.025091],
    [0, 0, 0, 0]
]


TRANSITION_MATRIX_ANTICOAGULATION = [
    [0, 0.0135, 0, 0.01938],
    [0, 0, 52, 0],
    [0, 0.022359, 0, 0.024107],
    [0, 0, 0, 0]
]


# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]

Anticoag_COST = [
    0,
    5000,
    750,
    0
]

