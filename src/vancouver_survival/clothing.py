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
    """
    # Validate inputs
    if temp_celsius < -273.15:
        raise ValueError("Temperature below absolute zero")
    if wind_speed_kmh < 0:
        raise ValueError("Wind speed cannot be negative")

    wind_chill_reduction = wind_speed_kmh / 10
    effective_temp = temp_celsius - wind_chill_reduction

    # Determine base score from effective temperature
    if effective_temp > 10:
        base_score = 1
    elif effective_temp >= 0:
        base_score = 3
    elif effective_temp < -20:
        base_score = 10
    else:
        base_score = 0

    # We use helper function w/2 branches on 1 executed line
    return base_score + _bus_penalty(is_waiting_for_bus)


def _bus_penalty(is_waiting_for_bus):
    # One physical line, two possible paths:
    # line coverage marks it covered,
    # branch coverage correctly reports the untaken path.
    if is_waiting_for_bus:
        return 2
    else:
        return 0


def suggest_rain_gear(precip_probability, wind_speed_kmh):
    """
    Suggest rain gear based on precipitation probability and wind conditions.

    In Vancouver, using an umbrella during high winds is a recipe for disaster.
    This function helps decide between an umbrella and a waterproof jacket.

    Parameters
    ----------
    precip_probability : float
        Probability of precipitation (0 to 100).
    wind_speed_kmh : float
        Wind speed in km/h.

    Returns
    -------
    str
        "No rain gear needed", "Umbrella", or "Waterproof Jacket".

    Examples
    --------
    >>> suggest_rain_gear(20, 10)
    'No rain gear needed'
    >>> suggest_rain_gear(80, 10)
    'Umbrella'
    >>> suggest_rain_gear(80, 40)
    'Waterproof Jacket'
    """
    if precip_probability < 30:
        return "No rain gear needed"

    if wind_speed_kmh > 35:
        return "Waterproof Jacket"

    return "Umbrella"
