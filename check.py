import os
import db
from SpsParser import Sps21Parser, Point

CHECK_CSV_HEADER = 'line,point,easting,northing,check_easting,check_northing,error_easting,error_northing'
CHECK_EXT = '.check.csv'
NOT_IN_DB_CSV_HEADER = 'line,point,easting,northing'
NOT_IN_DB_EXT = '.not-in-db.csv'


def process(db_file, sps_file, limit_easting, limit_northing):
    connection = db.create_connection(db_file)
    parser = Sps21Parser()
    check_file = sps_file + CHECK_EXT
    not_in_db_file = sps_file + NOT_IN_DB_EXT

    csv_file_create(check_file, CHECK_CSV_HEADER)
    csv_file_create(not_in_db_file, NOT_IN_DB_CSV_HEADER)

    with open(sps_file) as sps:
        line = sps.readline()
        sps_counter = 0
        offset_counter_easting = 0
        offset_counter_northing = 0
        while line:
            stats = parser.parse_point(line)
            point = Point(stats)

            stats = db.get_record_for_point(connection, point)

            if stats is None:
                record = "%.2f,%.2f,%.1f,%.1f" \
                         % (
                         point.line, point.point, point.easting, point.northing)
                csv_file_record_add(not_in_db_file, record)
                line = sps.readline()
                continue
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
            csv_file_record_add(check_file, record)

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


def csv_file_create(filename, header):
    check_file = open(filename, 'w')
    check_file.write(header + os.linesep)
    check_file.close()


def csv_file_record_add(filename, record):
    check_file = open(filename, 'a')
    check_file.write(record + os.linesep)
    check_file.close()
