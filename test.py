import logging
import ddlogs
import json

logger = logging.getLogger('test')
h = ddlogs.DatadogLogsHandler(
    source_category='samplecategory',
    source='samplesource',
    service='sampleservice',
    host='localhost')
h.setFormatter(ddlogs.DictFormatter())
logger.addHandler(h)
logger.error({'foo': 'bar'})
