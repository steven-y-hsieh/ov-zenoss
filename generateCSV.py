#!/usr/bin/env python
import sys
import logging
from datetime import date
from queryDB import select_query

def process_to_machine_list(result):
	machine_list = set()
	for each_tuple in result:
		for element in each_tuple:
			machine_list.add(element)
	return machine_list


def get_machine_list(machine_type):
	yearmonths = date.today().strftime("%Y%m")
	if machine_type == 'phy':
		sql_command = 'select fqdn, name from PhysicalInfo where yearsmonths = ' + yearmonths + ';'
	elif machine_type == 'vm':
		sql_command = 'select fqdn, name from VMInfo where yearsmonths = ' + yearmonths + ';'
	else:
		print 'wrong machine type'
		sys.exit()
	result = select_query(sql_command)
	machine_list = process_to_machine_list(result)
	return machine_list
	


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'generateCSVReport.py file_path machine_type(vm, phy) data_type(cpu, mem, disk, network) output_file_name'
        sys.exit()
    else:
        file_path = sys.argv[1] + '/'
        machine_type = sys.argv[2]
        data_type = sys.argv[3]
        output_file_name = sys.argv[4]
    machine_list = get_machine_list(machine_type)
    if data_type == 'cpu':
        get_cpu_utilization(machine_list, output_file_name)
    # elif data_type == 'mem':
    #     get_mem_utilzation(machine_list, output_file_name)
