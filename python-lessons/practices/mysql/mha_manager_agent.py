# -*- coding:utf-8 -*-
import subprocess


def check_binary_logs():
    save_bin_log_params = "--command=test --start_pos=4 --binlog_dir=/data/d10/mariadb/binlog " \
                          "--output_file=/var/log/masterha//save_binary_logs_test " \
                          "--manager_version=0.56 " \
                          "--binlog_prefix=master-bin"
    check_bin_logs = subprocess.run(["save_binary_logs", save_bin_log_params]
                                    ,stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

    print(check_bin_logs.returncode)
    print(check_bin_logs.stdout.decode('utf-8'))
