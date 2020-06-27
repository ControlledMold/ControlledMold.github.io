"""
Our model is

 log(cell/ml) = alpha * (secchi stick depth) + intercept + Noise

However, our cell/mL comes from a noisy hemocytometer, and our
depth measured with the secchi stick is also noisy. Our goal is
still to infer alpha & intercept as well as possible, so we can
dump the hemocytometer.

"""


import pymc3 as pm

BILLION = 1e9
TOTAL_SQUARES = 25

squares_counted = 5
cells_counted = np.array([310, 148, 241])
depth_observed = np.array([1.4, 2.4, 1.7])
N = cells_counted.shape[0]

with pm.Model() as model:

    depth_observed = pm.Data('depth_observed', depth_observed)

    alpha = pm.HalfNormal("alpha", sd=2.5)

    # I need a test value here because of under/over flow problems.
    intercept = pm.HalfNormal("intercept", sd=10, testval=10)
    tau = pm.Exponential("tau", 0.1)

    cells_conc = pm.Lognormal("cells/mL", mu=-alpha * depth_observed + intercept, tau=tau, shape=N, testval=np.exp(np.array([15, 15, 15])))

    final_dilution_factor = 1
    # the manufacturer suggests that depth of the chamber is 0.01cm ± 0.0004cm. Let's assume the worst and double the error.
    # the length of the 5x5 square grid is 1mm = 0.1cm, so the volume is 0.01 * 0.1 * 0.1 = 0.0001, with error 0.1 * 0.1 * 0.0004 * 2
    volume_of_chamber = pm.Normal("volume of chamber (mL)", mu=1e-4, sd=8e-6, testval=1e-4)

    # why is Poisson justified? in my final shaker, I have cells_conc * final_dilution_factor * shaker3_volume number of cells
    # I remove volume_of_chamber / shaker3_volume fraction of them, hence it's a binomial with very high count, and very low probability.
    cells_visible = pm.Poisson("cells in visible portion", mu=cells_conc * final_dilution_factor * volume_of_chamber, shape=N)

    number_of_counted_cells1 = pm.Binomial("number of counted cells", cells_visible, squares_counted/TOTAL_SQUARES, observed=cells_counted)
    trace = pm.sample(18000, tune=14000)


pm.plot_posterior(trace, var_names=['cells/mL', 'alpha', "tau", "intercept"])
pm.summary(trace, var_names=['cells/mL', 'alpha', "tau", "intercept"])
