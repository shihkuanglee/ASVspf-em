import numpy as np
from em import eval_metrics_2019 as em

def get_eer(bona__cm, spoof_cm):

    return em.compute_eer(bona__cm, spoof_cm)

def get_tDCF(asv_data_val, bona__cm_val, spoof_cm_val):
    """Modify from software implementations provide by ASVspoof,
    the evaluate_tDCF_asvspoof19.py in tDCF_python_v1.zip.

    LICENSE from software implementations provide by ASVspoof:
    This work is licensed under the Creative Commons
    Attribution-NonCommercial-ShareAlike 4.0 International
    License. To view a copy of this license, visit
    http://creativecommons.org/licenses/by-nc-sa/4.0/
    or send a letter to
    Creative Commons, 444 Castro Street, Suite 900,
    Mountain View, California, 94041, USA.
    """

    Pspoof = 0.05
    cost_model = {
        'Pspoof': Pspoof,  # Prior probability of a spoofing attack
        'Ptar': (1 - Pspoof) * 0.99,  # Prior probability of target speaker
        'Pnon': (1 - Pspoof) * 0.01,  # Prior probability of nontarget speaker
        'Cmiss_asv': 1,  # Cost of ASV system falsely rejecting target speaker
        'Cfa_asv': 10,  # Cost of ASV system falsely accepting nontarget speaker
        'Cmiss_cm': 1,  # Cost of CM system falsely rejecting target speaker
        'Cfa_cm': 10,  # Cost of CM system falsely accepting spoof
    }

    asv___keys_val = asv_data_val[:, 1]
    asv_scores_val = asv_data_val[:, 2].astype(np.single)
    tar___asv_val = asv_scores_val[asv___keys_val ==    'target']
    non___asv_val = asv_scores_val[asv___keys_val == 'nontarget']
    spoof_asv_val = asv_scores_val[asv___keys_val ==     'spoof']
    eer___asv_val,  asv_threshold_val = em.compute_eer(tar___asv_val, non___asv_val)
    [Pfa_asv, Pmiss_asv, Pmiss_spoof_asv] = em.obtain_asv_error_rates(tar___asv_val, non___asv_val, spoof_asv_val, asv_threshold_val)

    tDCF_curve, CM_thresholds = em.compute_tDCF(bona__cm_val, spoof_cm_val, Pfa_asv, Pmiss_asv, Pmiss_spoof_asv, cost_model, False)
    min_tDCF_index = np.argmin(tDCF_curve)
    min_tDCF_val = tDCF_curve[min_tDCF_index]

    return min_tDCF_val
