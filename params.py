

rhythms_freqs_range = {
    # Гц
    "delta": [1, 4],
    "theta": [4, 12],
    "slow_gamma": [25, 45],
    "middle_gamma": [45, 80],
    "fast_gamma": [80, 150],
    "ripples": [120, 250],
}

theta_epoches_params = {
    "theta_shreshold" : 2,
    "accept_window_theta_shreshold" : 2, # секунды
}

feasures_names = ["theta_phi", "theta_R"]
# gamma phases in theta state, s - slow, m - medium, f - fast
feasures_names.extend(["ts_gamma_s_phi", "ts_gamma_s_R"])
feasures_names.extend(["ts_gamma_m_phi", "ts_gamma_m_R"])
feasures_names.extend(["ts_gamma_f_phi", "ts_gamma_f_R"])

# gamma phases in non-theta state, s - slow, m - medium, f - fast
feasures_names.extend(["non_ts_gamma_s_phi", "non_ts_gamma_s_R"])
feasures_names.extend(["non_ts_gamma_m_phi", "non_ts_gamma_m_R"])
feasures_names.extend(["non_ts_gamma_f_phi", "non_ts_gamma_f_R"])

# phases during ripples
feasures_names.extend(["ripples_phi", "ripples_R"])

# spike rate in theta, non-theta state and ripples
feasures_names.extend(["ts_mean_spike_rate", "ts_std_spike_rate"])
feasures_names.extend(["non_ts_mean_spike_rate", "non_ts_std_spike_rate"])
feasures_names.extend(["ripple_ts_mean_spike_rate", "ripple_ts_std_spike_rate"])
