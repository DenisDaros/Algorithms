def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for i, j in permanence_period:
            if i <= target_time <= j:
                count += 1
    except (ValueError, TypeError, AssertionError):
        return None
    return count
