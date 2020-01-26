import subprocess
import optparse


def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-n", "--name", dest ="name", help = "Name of the c file")
	(options, arguments) = parser.parse_args()
	if not options.name:
		print('[-] Please provide the name of the .c file. For more details do --help ')
		return 0
	else:
		return options.name


def run(name):
	if name:
		subprocess.call(["gcc",name,"-o","output"])
		subprocess.call(["./output"])
		subprocess.call(["rm","output"])
	else:
		pass


name = get_args()
run(name)
