def recommend_beverage(warmth_score):
    """
    Recommend the optimal beverage to maintain homeostasis based on the calculated warmth score.

    Parameters
    ----------
    warmth_score : float
        The numeric score returned by clothing.calculate_warmth_score().
        (e.g., 1.0 is warm, 10.0 is freezing).

    Returns
    -------
    str
        The recommended beverage name.

    Examples
    --------
    >>> recommend_beverage(1.0)
    'Iced Americano'
    >>> recommend_beverage(5.0)
    'Hot Coffee'
    """
    if warmth_score < 2:
        return "Iced Americano"
    elif warmth_score <= 8:
        return "Hot Coffee"
    else:
        return "Hot Chocolate"
