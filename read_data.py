import os

def main():
	os.chdir('Final_Data')

	#put the beginning of the files that you want to concatenate here
	find_files = 'delay_FIFO'

	files = os.listdir('.')
	try:
		os.remove('combined_data_' + find_files)
	except OSError:
		pass

	files = filter(lambda x: True if find_files in x else False, files)

	for f in files:
		with open(f, 'r') as ofile:
			with open('combined_data_' + find_files, 'a') as dfile:
				for line in ofile:
					dfile.write(line)
				dfile.write('\n')

main()