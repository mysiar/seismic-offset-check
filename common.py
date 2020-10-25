import os

DB_LOG_FILE_EXT = '.log'


def csv_file_create(filename, header):
    check_file = open(filename, 'w')
    check_file.write(header + os.linesep)
    check_file.close()


def csv_file_record_add(filename, record):
    check_file = open(filename, 'a')
    check_file.write(record + os.linesep)
    check_file.close()


def log_file_create(filename):
    log_file = open(filename, 'w')
    log_file.close()


def log_file_record_add(filename, record):
    log_file = open(filename, 'a')
    log_file.write(record + os.linesep)
    log_file.close()


def count_file_line_number(filename):
    return sum(1 for line in open(filename))
