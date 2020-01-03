# <-- EXPAND to see the data classes
import fileinput


class TimeRange(object):
    """Represents a time range (the time between a start time and an end time)

    Example usage:
        >>> time_range = TimeRange('3-5')
        >>> print(time_range.start)
        3.0
        >>> print(time_range.end)
        5.0
        >>> print(time_range.end - time_range.start)
        2.0
    """

    def __init__(self, range_string):
        # for example, convert "3-5" into start=3.0 and end=5.0
        self.start, self.end = [float(time) for time in range_string.split('-')]

def open_hours_ratio(query_time_range, open_hours):
    """
    Inputs:
        A time range to query for (as a TimeRange object)
        A business's open hours (as a list of TimeRanges)

    Output:
        The fraction OF THE QUERY TIME RANGE that the business is open.
        (In other words, the percentage of the query time range in which the business is open.)
        Return this number as a float. This function should NOT do any rounding.

    Examples of time ranges:
        (0, 24)        the whole day
        (9, 17)        9 AM to 5 PM
        (18, 23.75)    6 PM to 11:45 PM

    Examples of open hours:
        []                       closed the entire day
        [(0, 24)]                open the entire day
        [(9.5, 17)]              open from 9:30 AM to 5 PM
        [(11, 14), (18, 22)]     open from 11 AM to 2 PM, and from 6 PM to 10 PM

    Assume that the open hours time ranges are in order and non-overlapping.

    Furthermore, all time ranges (start, end) have the property 0 <= start < end <= 24.

    Examples:
        Query Time Range    Open Hours            Answer
        (4, 10)             [(0, 24)]             1.0
        (7, 11)             [(9, 17)]             0.5
        (0, 24)             [(0, 2), (20, 24)]    0.25
        (5, 22)             []                    0.0
    """
    # TODO: COMPLETE ME
    

if __name__ == "__main__":
    main()
    