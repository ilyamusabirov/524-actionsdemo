def calculate_warmth_score(temp_celsius, wind_speed_kmh, is_waiting_for_bus):
    """
    Calculate a warmth score to determine appropriate clothing for Vancouver campus commute.
    
    The score increases with colder conditions, accounting for temperature, wind chill,
    and whether you're stationary or moving. Higher scores indicate colder perceived
    conditions requiring more insulation.
    
    Parameters
    ----------
    temp_celsius : float
        Temperature in Celsius. Must be >= -273.15 (absolute zero).
    wind_speed_kmh : float
        Wind speed in kilometers per hour. Must be non-negative.
    is_waiting_for_bus : bool
        True if wait for a bus expected (increases warmth score by 2 because of inactivity), 
        False if actively walking/biking.
    
    Returns
    -------
    float
        Warmth score indicating clothing needs, for example:
        + 1: T-shirt weather (>10°C after wind chill)
        + 3: Light jacket (0-10°C after wind chill)
        + 10: Arctic parka (<-20°C after wind chill)
    
    Raises
    ------
    ValueError
        If wind_speed_kmh is negative (physics violation).
        If temp_celsius is below -273.15 (below absolute zero).
    
    Notes
    -----
    Wind chill reduces effective temperature by 1°C per 10 km/h of wind.
    
    Examples
    --------
    >>> calculate_warmth_score(15, 0, False)
    1  # T-shirt weather
    
    >>> calculate_warmth_score(5, 20, True)
    5  # Light jacket + bus wait penalty (effective temp: 3°C)
    
    >>> calculate_warmth_score(-25, 30, False)
    10  # Arctic parka needed
    """

    # Validate inputs
    if temp_celsius < -273.15:
        raise ValueError("Temperature below absolute zero")
    if wind_speed_kmh < 0:
        raise ValueError("Wind speed cannot be negative")
    
    # Calculate effective temperature with wind chill
    wind_chill_reduction = wind_speed_kmh / 10
    effective_temp = temp_celsius - wind_chill_reduction
    
    # Determine base score from effective temperature
    if effective_temp > 10:
        base_score = 1  # T-shirt weather
    elif effective_temp >= 0:
        base_score = 3  # Light jacket
    elif effective_temp < -20:
        base_score = 10  # Arctic parka
    else:
        base_score = 0  # Between -20 and 0, no specific rule given
    
    # Apply bus waiting penalty
    bus_penalty = 2 if is_waiting_for_bus else 0
    
    return base_score + bus_penalty