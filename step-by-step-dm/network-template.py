

def generate_config(context):
  """Creates the network."""

  resources = [{
      'name': context.env['name'],
      'type': 'compute.v1.network',
      'properties': {
          'IPv4Range': '10.0.0.1/16'
      }
  }]
  return {'resources': resources}