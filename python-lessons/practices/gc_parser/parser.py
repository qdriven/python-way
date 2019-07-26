# -*- coding: utf-8 -*-
import re
from string import ascii_letters

real_time_re = re.compile('real=(.*?) secs')
heap = re.compile('Full GC.*?\[.*?\] \[.*?\] (\d+)K->(\d+)K\((\d+)K\)')


def parse(_format, file_name):
    with open(file_name, 'r') as f:
        one_gc_line = f.readline()
        stop_time = 0.0
        app_time = 0.0
        letts = ascii_letters + ':'

        last_gc_time = None
        young_gc = []
        old_gc = []
        full_gc = []
        heap_usg = []
        max_heap = 0
        while (one_gc_line):
            if one_gc_line.startswith('Application time:'):
                atime = one_gc_line.translate(None, letts)
                val = atime.replace(',','.')
                if val.strip():
                    try:
                        app_time+=float(val)
                    except:
                        pass
                one_gc_line=f.readline()
                continue
            if one_gc_line.startswith('Total time for which'):
                atime = one_gc_line.translate(None,ascii_letters+':')
                val=atime.replace(',','.')
                if val.strip():
                    try:
                        stop_time+=float(val)
                    except:
                        pass
                one_gc_line=f.readline()
                continue
            if one_gc_line.find('[Fill GC')!=-1:
                gc_time=float(one_gc_line[0:one_gc_line.find(':')].replace(',','.'))
                match=real_time_re.search(one_gc_line)
                full_gc_time_cur=0
                if match:
                    used = match.group(1)
                    after = match.group(2)
                    total = match.group(3)
                    freed = int(used) - int(after)
                    full_gc.append((gc_time, full_gc_time_cur, int(after), freed, int(total)))
                else:
                    full_gc.append((gc_time, full_gc_time_cur, 0))

            one_gc_line = f.readline()

        f.close()
        return full_gc