def study_schedule(permanence_period, target_time):
    if not permanence_period or target_time is None:
        return None

    max_students = 0

    for period in permanence_period:
        if (
            len(period) != 2
            or not all(isinstance(val, (int, float)) for val in period)
            or period[0] < 0
            or period[1] < 0
        ):
            return None

        start_time, end_time = period
        if target_time >= start_time and target_time <= end_time:
            max_students += 1

    return max_students
