import os.path
print(os.path.isfile("a22.py"))

# Import the 'struct' module, which provides pack and unpack functions for working with variable-length binary data.
import struct

# Use the 'calcsize' function to determine the size (in bytes) of the C int type for the current platform.
# The format string "P" is used to represent the C void pointer type, and multiplying it by 8 gives the size in bits.
# The result will be 32 for 32-bit platforms and 64 for 64-bit platforms.
print(struct.calcsize("P") * 8)

# Import the 'platform' and 'struct' modules.
import platform
import struct

# Use the 'architecture' function from the 'platform' module to get the bit architecture (32-bit or 64-bit) of the current platform.
# The [0] index retrieves the first element of the result, which is the architecture string.
architecture = platform.architecture()[0]

# Print the bit architecture string, which will be "32bit" or "64bit."
print(architecture)

# Use the 'calcsize' function from the 'struct' module to determine the size (in bytes) of the C int type for the current platform.
# The format string "P" is used to represent the C void pointer type, and multiplying it by 8 gives the size in bits.
# The result will be 32 for 32-bit platforms and 64 for 64-bit platforms.
print(struct.calcsize("P") * 8)

# Import the 'platform' and 'os' modules.
import platform
import os

# Print the name of the operating system based on the 'os.name' attribute.
# 'os.name' provides the name of the operating system dependent module imported.
print("Name of the operating system:", os.name)

# Print the name of the OS system using the 'platform.system()' function.
# 'platform.system()' returns the name of the operating system, such as 'Windows', 'Linux', or 'Darwin' (macOS).
print("\nName of the OS system:", platform.system())

# Print the version of the operating system using the 'platform.release()' function.
# 'platform.release()' returns the version or release of the operating system.
print("\nVersion of the operating system:", platform.release())


# Import the 'multiprocessing' module to work with multi-processing features.
import multiprocessing

# Use 'multiprocessing.cpu_count()' to determine the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()

# Print the number of CPU cores available on the system.
print(cpu_count)


# Import the 'site' module.
import site

# Use the 'site.getsitepackages()' function to retrieve site packages' paths.
# 'site.getsitepackages()' returns a list of paths where site packages are installed.
print(site.getsitepackages())


# Import the 'os' module to work with the operating system.
import os
# Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
# This will print the path of the current file.
print("Current File Name: ", os.path.realpath(__file__))


# Import the 'call' function from the 'subprocess' module.
from subprocess import call

# Use the 'call' function to execute the "ls -l" command.
# This command lists the files and directories in the current directory with details.
call(["ls", "-l"])
# Import the 'multiprocessing' module to work with multi-processing features.
import multiprocessing

# Use 'multiprocessing.cpu_count()' to determine the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()

# Print the number of CPU cores available on the system.
print(cpu_count)


