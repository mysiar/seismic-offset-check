import os
import db
from SpsParser import Sps21Parser, Point

CHECK_CSV_HEADER = 'line,point,easting,northing,check_easting,check_northing,error_easting,error_northing'
CHECK_EXT = '.check.csv'


def process(db_file, sps_file, limit_easting, limit_northing):
    connection = db.create_connection(db_file)
    parser = Sps21Parser()
    check_file = sps_file + CHECK_EXT

    check_csv_file_create(check_file)

    with open(sps_file) as sps:
        line = sps.readline()
        sps_counter = 0
        offset_counter_easting = 0
        offset_counter_northing = 0
        while line:
            stats = parser.parse_point(line)
            point = Point(stats)

            stats = db.get_record_for_point(connection, point)
            de = point.easting - stats[0]
            dn = point.northing - stats[1]

            error_easting = 0
            if abs(de) > limit_easting:
                offset_counter_easting += 1
                error_easting = 1

            error_northing = 0
            if abs(dn) > limit_northing:
                offset_counter_northing += 1
                error_northing = 1

            record = "%.2f,%.2f,%.1f,%.1f,%.1f,%.1f,%d,%d" \
                     % (point.line, point.point, point.easting, point.northing, de, dn, error_easting, error_northing)
            add_check_csv_record(check_file, record)

            line = sps.readline()
            sps_counter += 1
        sps.close()

        stats = {
            'SP': sps_counter,
            'OCE': offset_counter_easting,
            'OCN': offset_counter_northing
        }

        connection.close()

        return stats


def check_csv_file_create(filename):
    check_file = open(filename, 'w')
    check_file.write(CHECK_CSV_HEADER + os.linesep)
    check_file.close()


def add_check_csv_record(filename, record):
    check_file = open(filename, 'a')
    check_file.write(record + os.linesep)
    check_file.close()
