def study_schedule(permanence_period, target_time):
    if not permanence_period or target_time is None:
        return None

    max_students = 0

    for start_time, end_time in permanence_period:
        if (
            not isinstance(start_time, (int, float))
            or not isinstance(end_time, (int, float))
            or start_time < 0
            or end_time < 0
        ):
            return None

        if start_time <= target_time <= end_time:
            max_students += 1

    return max_students
