import re

__author__ = 'patrick'


def get_requests(log):
    log_line = log.read()
    pat = (r''
           '(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP address
           '\[(.+)\]\s'  # datetime
           '"GET\s(.+)\s\w+/.+"\s\d+\s'  # requested file
           '\d+\s"(.+)"\s'  # referrer
           '"(.+)"'  # user agent
           )
    requests = find(pat, log_line)
    return requests


def find(pattern, text):
    """
    find matched items
    :param pattern:
    :param text:
    :return:
    """
    match = re.findall(pattern, text)
    return match if match else False


def get_files(requests):
    """
    get requests into array
    :param requests:
    :return:
    """
    requested_files = []
    for req in requests:
        requested_files.append(req[2])
    return requested_files


def file_occur(files):
    """
    get files
    :param files:
    :return:
    """
    d = {}
    for file in files:
        d[file] = d.get(file, 0) + 1  ## easyuse for JAVA Map
    return d


def process_log(log):
    requests = get_requests(log)
    files = get_files(requests)
    totals = file_occur(files)
    return totals


if __name__ == '__main__':
    log_file = open('example.log', 'r')
    print(process_log(log_file))
