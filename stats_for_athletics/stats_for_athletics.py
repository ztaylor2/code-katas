"""."""


import statistics


def get_totals(string):
    """."""
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
    """."""
    return max(totals_in_seconds) - min(totals_in_seconds)


def get_average(totals_in_seconds):
    """."""
    return sum(totals_in_seconds) / len(totals_in_seconds)


def get_median(totals_in_seconds):
    """."""
    return statistics.median(totals_in_seconds)


def format_s_to_hms(seconds):
    """."""
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{:02}|{:02}|{:02}".format(int(h), int(m), int(s))


def stat(strg):
    """."""
    if strg == '':
        return ''
    totals_in_seconds = get_totals(strg)
    the_range = format_s_to_hms(get_range(totals_in_seconds))
    the_avg = format_s_to_hms(get_average(totals_in_seconds))
    the_median = format_s_to_hms(get_median(totals_in_seconds))
    return "Range: {} Average: {} Median: {}".format(the_range, the_avg, the_median)
