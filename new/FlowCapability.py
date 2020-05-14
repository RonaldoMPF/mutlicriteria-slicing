from Definitions import *
from Randomness import Randomness

class FlowCapability:
    def __init__(self, profile):
        self.r = Randomness(0, 0)
        self.values = {
            "latency": 0,
            "availability": 1,
            "frame_loss_ratio": 0.0,
            "throughput": 0,
        }
        self.resources_range = profiles[profile]

    def set_profile(self, profile):
        self.resources_range = profiles[profile]
	
	# Similar to HostCapability, but simpler
    def get(self, range=False):
        if range:
            self.values = {
                "latency": self.r.get(range=range, values=self.resources_range['LINK_DELAY_RANGE']),
                "availability": float(self.r.get(*self.resources_range['LINK_AVAILABILITY']) / 10000.0),
                "frame_loss_ratio": float(self.r.get(*self.resources_range['LINK_FRAME_LOSS']) / 1000.0),
                "throughput": self.r.get(range=range, values=self.resources_range['LINK_BANDWIDTH_RANGE'])*1000,
            }
        else:
            self.values = {
                "latency": self.r.get(*self.resources_range['LINK_DELAY']),
                "availability": float(self.r.get(*self.resources_range['LINK_AVAILABILITY'])/10000.0),
                "frame_loss_ratio": float(self.r.get(*self.resources_range['LINK_FRAME_LOSS'])/1000.0),
                "throughput": self.r.get(*self.resources_range['LINK_BANDWIDTH'])*1000,
            }
        return self.values
