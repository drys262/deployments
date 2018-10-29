

NETWORK_NAME = 'sample-network'

def generate_config(context):

    resources = []

    resources.extend([
        {
            'name': 'vm-1',
            'type': 'vm-template.py',
            'properties': {
                'machineType': 'f1-micro',
                'zone': 'asia-southeast1-b',
                'network': NETWORK_NAME
            }
        },
        {
            'name': 'vm-2',
            'type': 'vm-template.py',
            'properties': {
                'machineType': 'g1-small',
                'zone': 'asia-southeast1-b',
                'network': NETWORK_NAME
            }
        },
        {
            'name': 'sample-network',
            'type': 'network-template.py',
        },
        {
            'name': '%s-firewall' % (NETWORK_NAME),
            'type': 'firewall-template.py',
            'properties': {
                'network': NETWORK_NAME
            }
        },
    ])

    return {
        'resources': resources
    }