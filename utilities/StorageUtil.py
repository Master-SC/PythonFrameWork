d = {}


def rememberTheValue(key, value):
    d[key] = value


def whatIsTheValue(key):
    return d.get(key)
