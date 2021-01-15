import numpy as np


class GPS_Container():
    """Docstring."""
    
    def __init__(self, event_id, visible, timestamp, loc_long, loc_lat,
                 comments, external_temperature, gps_dop, gps_fix_type_raw,
                 gps_sattelite_count, height_above_ellipsoid,
                 lotek_crc_status_text, manually_marked_outlier, sensor_type,
                 individual_taxon_canonical_name, tag_local_identifier,
                 individual_local_identifier, study_name):
        """Docstring."""
        self.timestamp = timestamp
        self.long = float(loc_long)
        self.lat = float(loc_lat)
        self.temp = float(external_temperature) if external_temperature else None
        self.convert_timestamp_to_absolute()
        return
    
    def convert_timestamp_to_absolute(self):
        """Docstring."""
        date_str, time_str = self.timestamp.split()
        
        # date
        y, m, d = (int(v) for v in date_str.split('-'))
        
        # determine if leap year
        if (((not y % 4) and (not y % 100) and (not y % 400))
            or ((not y % 4) and (y % 100))):
            days_per_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        else:
            days_per_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        
        self.date = ((np.sum(days_per_month[0:m - 1]) + d)
                     / np.sum(days_per_month))
        
        # time
        h, m, s = (float(v) for v in time_str.split(':'))
        self.time = (h * 3600 + m * 60 + s) / (24 * 3600)
        return


def get_data():
    """Docstring"""
    with open('../data/elk_in_southwestern_alberta.csv') as F:
        lines = F.readlines()
    data = []
    for line in lines[1:]:
        line = line.split(',')
        data.append(GPS_Container(*line))
    return data


def store_one():
    """Docstring"""
    with open('../data/elk_in_southwestern_alberta.csv') as F:
        lines = F.readlines()
    for line in lines[1:]:
        line = line.split(',')
        return GPS_Container(*line)


if __name__ == '__main__':
    store_one()
