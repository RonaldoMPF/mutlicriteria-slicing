from Definitions import *
from Randomness import Randomness

class HostCapability:
    def __init__(self, profile, profile_nf=False):
        self.r = Randomness(0,0)
        self.values = {
            'num_cpus':0,
            'mem_size':0,
            'disk_size':0,
        }

		# Choose between a certain Infra or VNF profile

        if profile_nf:
            self.resources_range = nf_profiles[profile]
            # self.set_profile(profile)
        else:
            self.resources_range = profiles[profile]
            # self.set_profile(profile)
	
	# Assign information from an Infra profile
    def set_profile(self, profile):
        self.resources_range = profiles[profile]
		
		# Create new attributes in the Class

        self.cpu_min, self.cpu_max = self.resources_range['NODE_CPU']
        self.mem_min, self.mem_max = self.resources_range['NODE_MEM']
        self.storage_min, self.storage_max = self.resources_range['NODE_STORAGE']

    def get(self, range=False, suffix=False):

		# If range = True, choose a random element from the list

        if range:
            cpus = self.r.get(range=range, values=self.resources_range['NODE_CPU_RANGE'])
            mem = self.r.get(range=range, values=self.resources_range['NODE_MEM_RANGE'])
            disk = self.r.get(range=range, values=self.resources_range['NODE_STORAGE_RANGE'])

			#If suffix = True, save the value in the dictionary as String

            self.values = {
                'num_cpus': str(cpus) if suffix else cpus,
                'mem_size': str(mem) + ' GB' if suffix else mem,
                'disk_size': str(disk) + ' GB' if suffix else disk,
            }

		# If range = False, choose a random number in the range [min, max]

        else:
            cpus = self.r.get(self.cpu_min, self.cpu_max)
            mem = self.r.get(self.mem_min, self.mem_max)
            disk = self.r.get(self.storage_min, self.storage_max)
            self.values = {
                'num_cpus': str(cpus) if suffix else cpus,
                'mem_size': str(mem) + ' GB' if suffix else mem,
                'disk_size': str(disk) + ' GB' if suffix else disk,
            }
        return self.values
