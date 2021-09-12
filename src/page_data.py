from data import EN_DATA, PT_DATA


class PageData:
    def __init__(self, language):
        if language not in ['pt', 'en']:
            raise ValueError('Unsupported language. Supported language types `pt` and `en`')

        datas = {'pt': PT_DATA,
                 'en': EN_DATA}
        self.data = obj(datas[language])


class obj(object):
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [obj(item) if isinstance(item, dict) else item for item in value])
            else:
                setattr(self, key, obj(value) if isinstance(value, dict) else value)
