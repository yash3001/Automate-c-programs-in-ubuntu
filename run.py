import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-n", "--name", dest ="name", help = "Name of the c file")

(options, arguments) = parser.parse_args()

name = options.name

subprocess.call(f"gcc {name} -o output && ./output",shell=True)
subprocess.call("rm output",shell=True)

