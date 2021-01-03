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


if __name__ == '__main__':
    get_data()
