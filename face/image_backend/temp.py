from face.image_backend.Generating_Result import alignment_generate


# dict = {'kind': ['3', 0.87258327], 'aggressive': ['1', 0.823676169], 'caring': ['3', 0.7925667], 'confident': ['3', 0.7490495], 'sociable': ['3', 0.7143843], 'humble': ['3', 0.7111577], 'responsible': ['2', 0.6915853], 'calm': ['3', 0.6501443], 'attractive': ['1', 0.6453781], 'weird': ['2', 0.611205459], 'intelligent': ['2', 0.556929052], 'age': 28.0}
dict = {'kind': ['3', 0.8562403], 'confident': ['3', 0.7869959], 'aggressive': ['1', 0.7367703], 'humble': ['3', 0.715362847], 'responsible': ['2', 0.700152159], 'attractive': ['1', 0.6607002], 'caring': ['3', 0.635173857], 'calm': ['3', 0.617453635], 'weird': ['2', 0.6136293], 'sociable': ['3', 0.6057097], 'intelligent': ['3', 0.6001968], 'age': 39.0}
print(alignment_generate(dict))