

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def generate_config(context):
    resources = []

    machineType = ''.join([COMPUTE_URL_BASE, 'projects/%s' % (context.env['project']) , '/zones/%s/machineTypes/%s' % (context.properties.get('zone'), context.properties['machineType'])])

    resources.append({
        'name': context.env['name'],
        'type': 'compute.v1.instance',
        'properties': {
            'zone': context.properties['zone'],
            'machineType': machineType,
            'disks': [{
                'deviceName': 'boot',
                'type': 'PERSISTENT',
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/debian-cloud/global/images/family/debian-9'])
                },
            }],
            'networkInterfaces': [{
                'network': '$(ref.%s.selfLink)' % (context.properties['network']),
                'accessConfigs': [{
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT',
                }]
            }],
            'metadata': {
                'items': [{
                    'key': 'startup-script-url',
                    'value': 'gs://dkbucketsample/startup-scripts/apache-script.sh'
                }]
            }
        }
    })

    return {
        'resources': resources
    }