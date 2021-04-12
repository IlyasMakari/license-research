
# license identifiers that refer to a node --> unique name for that node

nodes = {
    **dict.fromkeys(['Unlicense', 'WTFPL', 'CC0-1.0', '0BSD', 'Other'], 'public-domain'), # Making the underestimation that "Other" (i.e. No license found) means public domain
    **dict.fromkeys(['Zlib', 'Libpng'], 'zlib/libpng'),
    **dict.fromkeys(['MIT', 'MIT-0', 'X11', 'ISC', 'ICU'], 'MIT/X11'), # Assuming ICU is equivalent to MIT
    **dict.fromkeys(['AFL-3.0'], 'AFL-3.0'),
    **dict.fromkeys(['Apache-2.0'], 'Apache-2.0'),
    **dict.fromkeys(['BSD-3-Clause'], '3-clause / New BSD'),
    **dict.fromkeys(['BSD-2-Clause'], '2-clause / Free BSD'),
    **dict.fromkeys(['MPL-1.1'], 'MPL-1.1'),
    **dict.fromkeys(['MPL-1.1+'], 'MPL-1.1+'), # why + ?
    **dict.fromkeys(['MPL-2.0'], 'MPL-2.0'),
    **dict.fromkeys(['CDDL-1.0'], 'CDDL-1.0'),
    **dict.fromkeys(['LGPL-2.1', 'LGPL-2.1-only'], 'LGPL-2.1'),
    **dict.fromkeys(['LGPL-2.1+', 'LGPL-2.1-or-later'], 'LGPL-2.1+'),
    **dict.fromkeys(['LGPL-3.0-only', 'LGPL-3.0-or-later', 'LGPL-3.0', 'LGPL-3.0+'], 'LGPL-3.0 or LGPL-3.0+'),
    **dict.fromkeys(['OSL-3.0'], 'OSL-3.0'),
    **dict.fromkeys(['GPL-2.0', 'GPL-2.0-only'], 'GPL-2.0'), # many excpetions left out
    **dict.fromkeys(['GPL-2.0+', 'GPL-2.0-or-later'], 'GPL-2.0+'),
    **dict.fromkeys(['GPL-3.0-only', 'GPL-3.0-or-later', 'GPL-3.0', 'GPL-3.0+'], 'GPL-3.0 or GPL-3.0+'),
    **dict.fromkeys(['AGPL-3.0', 'AGPL-3.0-only'], 'AGPL-3.0'),
    **dict.fromkeys(['AGPL-1.0+', 'AGPL-1.0-or-later'], 'AGPL-1.0+'),
}

# True = transitive edge
# False = non-transitive edge
# None = Exception, these edges will be ignored while making the transitive closure of the graph

edges = {

    'public-domain': {
        **dict.fromkeys(nodes.values(), "Exception"),
    },

    'MIT/X11': {
        '3-clause / New BSD': True,
        '2-clause / Free BSD': True,
    },

    '2-clause / Free BSD': {
        '3-clause / New BSD': True
    },

    '3-clause / New BSD': {
        'Apache-2.0': True,
        'MPL-2.0': True
    },

    'zlib/libpng': {
        'Apache-2.0': True
    },

    'Apache-2.0': {
        'AFL-3.0': True,
        'LGPL-3.0 or LGPL-3.0+': True,
        'MPL-2.0': False
    },

    'AFL-3.0': {
        'OSL-3.0': True
    },

    'MPL-1.1': {
        'MPL-2.0': False,
        'CDDL-1.0': True
    },

    'MPL-1.1+': {
        'MPL-1.1': True,
        'CDDL-1.0': True,
        'MPL-2.0': True
    },

    'MPL-2.0': {
        'LGPL-2.1+': True
    },

    'LGPL-2.1+': {
        'LGPL-3.0 or LGPL-3.0+': True,
        'LGPL-2.1': True,
        'GPL-2.0+': True,
        
        # LGPL makes an exception when work is used as library
        **dict.fromkeys([
            'public-domain',
            'MIT/X11',
            '3-clause / New BSD',
            '2-clause / Free BSD',
            'Apache-2.0',
            'zlib/libpng',
            'AFL-3.0',
            'MPL-1.1',
            'MPL-1.1+',
            'MPL-2.0',
            'CDDL-1.0'
        ], "Exception"),
    },

    'LGPL-3.0 or LGPL-3.0+': {
        'GPL-3.0 or GPL-3.0+': True,

        # LGPL makes an exception when work is used as library
        **dict.fromkeys([
            'public-domain',
            'MIT/X11',
            '3-clause / New BSD',
            '2-clause / Free BSD',
            'Apache-2.0',
            'zlib/libpng',
            'AFL-3.0',
            'MPL-1.1',
            'MPL-1.1+',
            'MPL-2.0',
            'CDDL-1.0'
        ], "Exception"),
    },

    'LGPL-2.1': {
        'GPL-2.0': True,
        'GPL-2.0+': True,

        # LGPL makes an exception when work is used as library
        **dict.fromkeys([
            'public-domain',
            'MIT/X11',
            '3-clause / New BSD',
            '2-clause / Free BSD',
            'Apache-2.0',
            'zlib/libpng',
            'AFL-3.0',
            'MPL-1.1',
            'MPL-1.1+',
            'MPL-2.0',
            'CDDL-1.0'
        ], "Exception"),
    },

    'GPL-2.0+': {
        'GPL-2.0': True,
        'GPL-3.0 or GPL-3.0+': True
    },

    'GPL-3.0 or GPL-3.0+': {
        'AGPL-3.0': True,
    },

    'AGPL-1.0+': {
        'AGPL-3.0': True
    },

    'CDDL-1.0' : {

    },

    'OSL-3.0' : {

    },

    'GPL-2.0' : {

    },

    'AGPL-3.0' : {

    },
}