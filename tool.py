import rrdtool



def transUTF8toAscii(fs_path):
    if isinstance(fs_path,unicode) :
        fs_path = fs_path.decode('utf8').encode('ascii')
    return fs_path

def get_rrd_avg(rrd_file, start, end, resolution):
    rrd = rrdtool.fetch (rrd_file, 'AVERAGE',
                     '--resolution', resolution,
                     '--start', start,
                     '--end', end)
    return rrd