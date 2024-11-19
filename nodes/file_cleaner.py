import os.path

from folder_paths import output_directory, input_directory


class FileCleaner:
    @classmethod
    def INPUT_TYPES(s):
        return {
            'required': {
                'type': (
                    ('input', 'output'),
                    {
                        'multiline': False,
                        'default': 'input',
                    }
                ),
                'path': ('STRING', {'multiline': False}),
            },
        }

    RETURN_TYPES = ('STRING',)
    FUNCTION = 'clean'
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)
    CATEGORY = 'utils'

    def clean(self, type, path):
        full_path = os.path.join(output_directory, path) if type == 'output' else os.path.join(input_directory, path)
        if os.path.exists(full_path):
            os.remove(full_path)
            return f'{full_path} removed'
        raise FileNotFoundError(f'{full_path} not found')