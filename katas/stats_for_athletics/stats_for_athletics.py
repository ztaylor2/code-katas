"""Output statistics from an input.

#1 Best Practices Solution:

def stat(strg):

    def get_time(s):
        '''Returns the time, in seconds, represented by s.'''
        hh, mm, ss = [int(v) for v in s.split('|')]
        return hh * 3600 + mm * 60 + ss

    def format_time(time):
        '''Returns the given time as a string in the form "hh|mm|ss".'''
        hh = time // 3600
        mm = time // 60 % 60
        ss = time % 60
        return '{hh:02d}|{mm:02d}|{ss:02d}'.format(**locals())

    def get_range(times):
        return times[-1] - times[0]

    def get_average(times):
        return sum(times) // len(times)

    def get_median(times):
        middle = len(times) >> 1
        return (times[middle] if len(times) & 1 else
                (times[middle - 1] + times[middle]) // 2)

    if strg == '':
        return strg
    times = [get_time(s) for s in strg.split(', ')]
    times.sort()
    rng = format_time(get_range(times))
    avg = format_time(get_average(times))
    mdn = format_time(get_median(times))
    return 'Range: {rng} Average: {avg} Median: {mdn}'.format(**locals())
"""


# import statistics


def get_totals(string):
    """Get totals from input."""
    values = []
    totals = []
    totals_in_seconds = []
    values = string.split(', ')
    for val in values:
        totals.append(val.split('|'))

    for tot in totals:
        h_to_s = int(tot[0]) * 3600
        m_to_s = int(tot[1]) * 60
        s = int(tot[2])

        totals_in_seconds.append(h_to_s + m_to_s + s)

    return totals_in_seconds


def get_range(totals_in_seconds):
    """Get range from totals array."""
    return max(totals_in_seconds) - min(totals_in_seconds)


def get_average(totals_in_seconds):
    """Get average from totals array."""
    return sum(totals_in_seconds) / len(totals_in_seconds)


def get_median(totals_in_seconds):
    """Get medial from totals array."""
    totals_in_seconds.sort()
    middle = len(totals_in_seconds) >> 1
    return (totals_in_seconds[middle] if len(totals_in_seconds) & 1 else
            (totals_in_seconds[middle - 1] + totals_in_seconds[middle]) // 2)
    # return statistics.median(totals_in_seconds)


def format_s_to_hms(seconds):
    """Format the output."""
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{:02}|{:02}|{:02}".format(int(h), int(m), int(s))


def stat(strg):
    """Call all other functions and return output."""
    if strg == '':
        return ''
    totals_in_seconds = get_totals(strg)
    the_range = format_s_to_hms(get_range(totals_in_seconds))
    the_avg = format_s_to_hms(get_average(totals_in_seconds))
    the_median = format_s_to_hms(get_median(totals_in_seconds))
    return "Range: {} Average: {} Median: {}".format(the_range, the_avg, the_median)
