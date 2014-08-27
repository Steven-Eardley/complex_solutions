# When updating the licenses in the DOAJ; the following code substitutes text according to a dict of corrections.
# note: the keys are sorted by length so the longest substitutions aren't ruined by their substrings.
# One day this may be useful for changing text in something.

import re

license_correct_dict = { "CC by" : "CC BY",
                         "CC by-nc" : "CC BY-NC",
                         "CC by-nc-nd" : "CC BY-NC-ND",
                         "CC by-nc-sa" : "CC BY-NC-SA",
                         "CC-BY-NC-SA" : "CC BY-NC-SA",
                         "CC by-sa" : "CC BY-SA",
                         "CC by-nd" : "CC BY-ND",
                         "not-cc-like" : "Not CC-like"
                        }

# Buld a regex to match any of our targets to change, e.g.:
# '\b(not-cc-like|CC by-nc-sa|CC by-nc-nd|CC-BY-NC-SA|CC by-nd|CC by-sa|CC by-nc|CC by)\b'
keys_by_len = sorted(license_correct_dict.keys(), key=len, reverse=True)
match_licenses = re.compile(r'(' + '|'.join(keys_by_len) + r')')

# Function to update the license in the json (as string)
def update_license_entry(old_string):
    return match_licenses.sub(lambda x: license_correct_dict[x.group()], old_string)
