from sys import argv

dd = {
  '35612346' : 'up',
  '1352356': 'up',
  '23612346': 'down',
  '13526': 'down',
  '51456': 'left',
  '545': 'left',
  '134561235': 'right',
  '1341235': 'right',
}

print dd[argv[1]]
