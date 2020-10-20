import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from FixedWidthTextParser.Seismic.SpsParser import Sps21Parser
from model.Plan import Plan
from model.Base import Base


def process(progress_bar, db_file, sps_file, fast, window):
    engine = create_engine('sqlite:///' + db_file)
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()

    parser = Sps21Parser()

    with open(sps_file) as sps:
        line = sps.readline()
        sps_counter = 0

        while line:
            sps_data = parser.parse_point(line)
            line = str(int(sps_data[1]))
            point = str(int(sps_data[2]))
            line_point = line + point
            easting = sps_data[10]
            northing = sps_data[11]

            p = Plan(lp=line_point, easting=easting, northing=northing)
            try:
                s.add(p)
                if fast is False:
                    s.commit()
            except:
                pass

            sps_counter += 1
            progress_bar.setValue(sps_counter)

            line = sps.readline()

        if fast is True:
            try:
                s.commit()
            except:
                window.warning_process()

        sps.close()

    return sps_counter


def process_old(progress_bar, db_file, sps_file):
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
