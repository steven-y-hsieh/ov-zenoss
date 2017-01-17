from tool import transUTF8toAscii

collectors = ['sjdc-1', 'udc2-1', 'sjc1-1', 'iad1-1',
			  'iad1-2', 'muc1-1', 'fra1-1', 'aws-use',
              'aws-usw2', 'aws-eu', 'aws-jp', 'aws-au',
              'aws-br', 'localhost']

def process_rrd_result(result):
	start_time = result[0][0]
	end_time = result[0][1]
    time_resolution = result[0][2]
    value = result[2]
    return (start_time, end_time, time_resolution, value)

def get_cpu_from_usage_file(machine_list):
	cpu_usage_list = []
    for machine_name in machine_list:
	    for collector in collectors:
	        CPUUsageFile = "%s%s/Devices/%s/CPUUsage_cpu_usage.rrd" % (
	            DST_DIR, collector, machine_name)
	        CPUUsageFile = transUTF8toAscii(CPUUsageFile)
	        if os.path.isfile(CPUUsageFile):
	            end = str(int(os.path.getmtime(CPUUsageFile)))
	            result = get_rrd_avg(CPUUsageFile, start, end)
	            start_time, end_time, time_resolution, cpu_util_avg_list = process_rrd_result(result)
	            for cpu_util_avg in cpu_util_avg_list:
	                start_time += time_resolution
	                if cpu_util_avg[0] != None:
	                	cpu_usage = (machine_name, 
	                				 str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))), 
	                				 str(cpu_util_avg[0]))
	                	cpu_usage_list.append(cpu_usage)
	return cpu_usage_list


def get_cpu_utilization(machine_list)
	result = get_cpu_from_cpu_usage_file(machine_list)
	print result