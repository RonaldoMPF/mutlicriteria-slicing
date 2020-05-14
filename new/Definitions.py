
NODES = 100
DEGREE = 5
EDGES_PROB = 0.5
NEIGHBOUR_EDGES = 5

NFS = 1000
NFS_NODE_PROB = 0.6

FLOWS_LINK_PROB = 0.6

NODES_LINK_PROB = 0.7

NODE_CPU_MAX = 16
NODE_CPU_MIN = 1
NODE_MEM_MAX = 64
NODE_MEM_MIN = 8
NODE_STORAGE_MAX = 1000
NODE_STORAGE_MIN = 10

NODE_CPU_RANGE = [4, 8, 16, 32, 64]
NODE_MEM_RANGE = [8, 16, 32, 64]
NODE_STORAGE_RANGE = [100, 500, 1000, 2000, 10000]

LINK_DELAY_MAX = 10
LINK_DELAY_MIN = 1
LINK_BANDWIDTH_MAX = 100
LINK_BANDWIDTH_MIN = 1
LINK_AVAILABILITY_MIN = 95
LINK_AVAILABILITY_MAX = 99
LINK_FRAME_LOSS_MIN = 0
LINK_FRAME_LOSS_MAX = 5

LINK_DELAY_RANGE = [2, 4, 6, 8]
LINK_BANDWIDTH_RANGE = [1, 10, 40, 100]


NF_PROFILE_1 = {
    'NODE_CPU_RANGE': [2, 4],
    'NODE_MEM_RANGE': [2, 4],
    'NODE_STORAGE_RANGE': [20],
    'NODE_CPU': (2, 4),
    'NODE_MEM': (2, 4),
    'NODE_STORAGE': (20, 20),
}

NF_PROFILE_2 = {
    'NODE_CPU_RANGE': [4, 8],
    'NODE_MEM_RANGE': [4, 8],
    'NODE_STORAGE_RANGE': [50],
    'NODE_CPU': (4, 8),
    'NODE_MEM': (4, 8),
    'NODE_STORAGE': (50, 50),
}

NF_PROFILE_3 = {
    'NODE_CPU_RANGE': [8, 16],
    'NODE_MEM_RANGE': [8, 16],
    'NODE_STORAGE_RANGE': [100, 100],
    'NODE_CPU': (8, 16),
    'NODE_MEM': (8, 16),
    'NODE_STORAGE': (100, 100),
}

# Profile 4 is incomplete in relation to the others
NF_PROFILE_4 = {
    'NODE_CPU_RANGE': [2, 4, 8],
    'NODE_MEM_RANGE': [4, 8, 16],
    'NODE_STORAGE_RANGE': [20, 50, 100],
}


INFRA_PROFILE_1 = {
    'NODE_CPU_RANGE': [2, 4, 8],
    'NODE_MEM_RANGE': [4, 8, 16],
    'NODE_STORAGE_RANGE': [100, 500, 1000],
    'LINK_DELAY_RANGE': [6, 8, 10],
    'LINK_BANDWIDTH_RANGE': [1, 2, 5, 10],
    'LINK_AVAILABILITY': (9990, 9995),
    'LINK_FRAME_LOSS': (4, 8),
    'NODE_CPU': (2, 8),
    'NODE_MEM': (2, 16),
    'NODE_STORAGE': (100, 1000),
    'LINK_DELAY': (6, 10),
    'LINK_BANDWIDTH': (1, 10),
}

INFRA_PROFILE_2 = {
    'NODE_CPU_RANGE': [8, 16, 32],
    'NODE_MEM_RANGE': [4, 8, 16, 32],
    'NODE_STORAGE_RANGE': [500, 1000, 2000],
    'LINK_DELAY_RANGE': [4, 6, 8],
    'LINK_BANDWIDTH_RANGE': [5, 10, 20, 40],
    'LINK_AVAILABILITY': (9995, 9998),
    'LINK_FRAME_LOSS': (2, 6),
    'NODE_CPU': (8, 32),
    'NODE_MEM': (4, 32),
    'NODE_STORAGE': (500, 2000),
    'LINK_DELAY': (4, 8),
    'LINK_BANDWIDTH': (10, 40),
}

INFRA_PROFILE_3 = {
    'NODE_CPU_RANGE': [16, 32, 64],
    'NODE_MEM_RANGE': [16, 32, 64, 128],
    'NODE_STORAGE_RANGE': [1000, 2000, 10000],
    'LINK_DELAY_RANGE': [1, 2, 4],
    'LINK_BANDWIDTH_RANGE': [20, 40, 80, 100],
    'LINK_AVAILABILITY': (9998, 9999),
    'LINK_FRAME_LOSS': (1, 4),
    'NODE_CPU': (16, 64),
    'NODE_MEM': (16, 128),
    'NODE_STORAGE': (1000, 10000),
    'LINK_DELAY': (1, 4),
    'LINK_BANDWIDTH': (40, 1000),
}

INFRA_PROFILE_4 = {
    'NODE_CPU_RANGE': [2, 4, 8, 16, 32, 64],
    'NODE_MEM_RANGE': [8, 16, 32, 64],
    'NODE_STORAGE_RANGE': [100, 500, 1000, 2000, 10000],
    'LINK_DELAY_RANGE': [1, 2, 4, 6, 8, 10],
    'LINK_BANDWIDTH_RANGE': [1, 2, 5, 10, 20, 40, 80, 100],
    'LINK_AVAILABILITY': (9990, 9999),
    'LINK_FRAME_LOSS': (1, 10),
    'NODE_CPU': (4, 64),
    'NODE_MEM': (8, 128),
    'NODE_STORAGE': (100, 10000),
    'LINK_DELAY': (1, 10),
    'LINK_BANDWIDTH': (1, 1000),
}

# Profile mapping Dictionary

profiles = {
    1: INFRA_PROFILE_1,
    2: INFRA_PROFILE_2,
    3: INFRA_PROFILE_3,
    4: INFRA_PROFILE_4,
}

nf_profiles = {
    1: NF_PROFILE_1,
    2: NF_PROFILE_2,
    3: NF_PROFILE_3,
    4: NF_PROFILE_4,
}



