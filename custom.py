import numpy as np
import SciFiReaders
from tiled.adapters.array import ArrayAdapter
from urllib.parse import urlparse

import numpy as np
import hyperspy.api as hs
from tiled.adapters.mapping import MapAdapter

import numpy as np
import SciFiReaders
from urllib.parse import urlparse
from tiled.adapters.array import ArrayAdapter
from tiled.adapters.mapping import MapAdapter


# class EMDAdapter(MapAdapter):

#     @classmethod
#     def from_uris(cls, data_uri, metadata=None, **kwargs):
#         filepath = urlparse(data_uri).path

#         reader = SciFiReaders.EMDReader(filepath)
#         result = reader.read()

#         # EMDReader returns a dict of {name: sidpy.Dataset}
#         if isinstance(result, dict):
#             datasets = result
#         elif isinstance(result, list):
#             datasets = {str(i): d for i, d in enumerate(result)}
#         else:
#             datasets = {"0": result}

#         children = {}
#         for key, dataset in datasets.items():
#             array_data = np.asarray(dataset)
#             file_metadata = {}
#             if hasattr(dataset, 'original_metadata'):
#                 file_metadata = dict(dataset.original_metadata)
#             if metadata is not None:
#                 file_metadata.update(metadata)
#             children[key] = ArrayAdapter.from_array(array_data, metadata=file_metadata)

#         return cls(children)

#     @classmethod
#     def from_catalog(cls, data_source, metadata=None, **kwargs):
#         data_uri = data_source.assets[0].data_uri
#         return cls.from_uris(data_uri, metadata=metadata, **kwargs)

import numpy as np
import hyperspy.api as hs
from urllib.parse import urlparse
from tiled.adapters.array import ArrayAdapter
from tiled.adapters.mapping import MapAdapter

class EMDAdapter(MapAdapter):
    @classmethod
    def from_uris(cls, data_uri, metadata=None, **kwargs):
        filepath = urlparse(data_uri).path
        
        signals = hs.load(filepath)
        if not isinstance(signals, list):
            signals = [signals]
        
        children = {}
        for i, signal in enumerate(signals):
            array_data = signal.data
            file_metadata = dict(signal.metadata.as_dictionary())
            key = signal.metadata.General.title or str(i)
            children[key] = ArrayAdapter.from_array(array_data, metadata=file_metadata)
        
        return cls(children)

    @classmethod
    def from_catalog(cls, data_source, metadata=None, **kwargs):
        # DataSource object has a .assets attribute, each asset has a .data_uri
        data_uri = data_source.assets[0].data_uri
        return cls.from_uris(data_uri, metadata=metadata, **kwargs)