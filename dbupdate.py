import db
from SpsParser import Sps21Parser


def process(progress_bar, db_file, sps_file):
    connection = db.create_connection(db_file)
    parser = Sps21Parser()

    with open(sps_file) as sps:
        line = sps.readline()
        sps_counter = 0

        while line:
            parsed = parser.parse_point(line)

            db.insert_record_from_parsed_sps(connection, parsed)

            line = sps.readline()
            sps_counter += 1
            progress_bar.setValue(sps_counter)

        sps.close()

        connection.close()

    return sps_counter
