def unicode_dict(d):
    """ Recursively convert dictionary keys to unicode """
    if isinstance(d, dict):
        return dict((unicode(k), unicode_dict(v)) for k, v in d.items())
    elif isinstance(d, list):
        return [unicode_dict(e) for e in d]
    else:
        return d
