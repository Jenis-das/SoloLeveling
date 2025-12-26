from datetime import datetime

def calcTime(fromTime=None, toTime=None, duration=None):
    """
    fromTime: str -> 'HH:MM' or 'HH:MM AM/PM'
    toTime: str   -> 'HH:MM' or 'HH:MM AM/PM'
    duration: int -> minutes
    """

    result = {
        "fromTime": fromTime,
        "toTime": toTime,
        "duration": None
    }

    # ---------- Case 1: fromTime & toTime ----------
    if fromTime and toTime:
        time_formats = ["%H:%M", "%I:%M %p"]  # 24h and AM/PM
        start = end = None

        # Try parsing fromTime
        for fmt in time_formats:
            try:
                start = datetime.strptime(fromTime.strip(), fmt)
                break
            except ValueError:
                pass

        if not start:
            raise ValueError("Invalid fromTime format")

        # Try parsing toTime
        for fmt in time_formats:
            try:
                end = datetime.strptime(toTime.strip(), fmt)
                break
            except ValueError:
                pass

        if not end:
            raise ValueError("Invalid toTime format")

        diff = (end - start).total_seconds() / 60

        # ❌ No next-day allowed
        if diff < 0:
            raise ValueError("toTime must be after fromTime (next-day not allowed)")

        result["duration"] = int(diff)
        return result

    # ---------- Case 2: duration only ----------
    if duration is not None:
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer (minutes)")

        result["duration"] = duration
        return result

    # ---------- Case 3: invalid ----------
    raise ValueError("Provide either fromTime & toTime OR duration")



calcTime()