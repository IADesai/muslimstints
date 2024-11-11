const { getDataConnect, validateArgs } = require('firebase/data-connect');

const connectorConfig = {
  connector: 'default',
  service: 'muslimstints',
  location: 'europe-west2'
};
exports.connectorConfig = connectorConfig;

