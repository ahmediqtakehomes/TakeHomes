"""This module calculates electricity bills."""

import pandas as pd

# ----------------------------------------------------------------------------
# Candidate work goes here


def energy_charge(data):
    """
    Calculate volumetric energy charge.

    Parameters
    ----------
    data : pd.DataFrame
        A dataframe returned from the `_get_data` method.

    Returns
    -------
    float
        Total monthly energy charge.

    """
    pass


def demand_charge(data):
    """
    Calculate max-demand charge.

    Parameters
    ----------
    data : pd.DataFrame

    Returns
    -------
    float
        Total monthly demand charge.

    """
    pass


# ----------------------------------------------------------------------------
# Candidate helpers


# ----------------------------------------------------------------------------
# Predefinied helpers


def _get_data():
    return pd.read_excel('data.xlsx')
