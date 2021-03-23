# Fix LGPL and GPL

# unique name of a node -> licences in that node
nodes = {
    'public-domain': ['Unlicense'],
    'zlib/libpng': ['Zlib', 'Libpng'],
    'MIT/X11': ['MIT', 'MIT-0', 'X11', 'ISC'],
    'AFL-3.0': ['AFL-3.0'],
    'Apache-2.0': ['Apache-2.0'],
    '3-clause / New BSD': ['BSD-3-Clause'],
    '2-clause / Free BSD': ['BSD-2-Clause'],
    'MPL-1.1': ['MPL-1.1'],
    'MPL-1.1+': ['MPL-1.1+'], # why + ?
    'MPL-2.0': ['MPL-2.0'],
    'CDDL-1.0': ['CDDL-1.0'],
    'LGPL-2.1': ['LGPL-2.1', 'LGPL-2.1-only'],
    'LGPL-2.1+': ['LGPL-2.1+', 'LGPL-2.1-or-later'],
    'LGPL-3.0 or LGPL-3.0+': ['LGPL-3.0-only', 'LGPL-3.0-or-later', 'LGPL-3.0', 'LGPL-3.0+'],
    'OSL-3.0': ['OSL-3.0'],
    'GPL-2.0': ['GPL-2.0', 'GPL-2.0-only'], # many excpetions left out
    'GPL-2.0+': ['GPL-2.0+', 'GPL-2.0-or-later'],
    'GPL-3.0 or GPL-3.0+': ['GPL-3.0-only', 'GPL-3.0-or-later', 'GPL-3.0', 'GPL-3.0+'],
    'AGPL-3.0': ['AGPL-3.0', 'AGPL-3.0-only'],
    'AGPL-1.0+': ['AGPL-1.0+', 'AGPL-1.0-or-later']
}

# True = transitive edge

compatibility_graph = {
    **dict.fromkeys(nodes['public-domain'], {
            **dict.fromkeys(nodes['MIT/X11'], True)
        }
    ),
    **dict.fromkeys(nodes['MIT/X11'], { 
            **dict.fromkeys(nodes['3-clause / New BSD'], True),
            **dict.fromkeys(nodes['2-clause / Free BSD'], True)
        }
    ),
    **dict.fromkeys(nodes['2-clause / Free BSD'], {
            **dict.fromkeys(nodes['3-clause / New BSD'], True)
        }
    ),
    **dict.fromkeys(nodes['3-clause / New BSD'], {
            **dict.fromkeys(nodes['Apache-2.0'], True),
            **dict.fromkeys(nodes['MPL-2.0'], True)
        }
    ),
    **dict.fromkeys(nodes['zlib/libpng'], {
            **dict.fromkeys(nodes['Apache-2.0'], True)
        }
    ),
    **dict.fromkeys(nodes['Apache-2.0'], {
            **dict.fromkeys(nodes['AFL-3.0'], True),
            **dict.fromkeys(nodes['LGPL-3.0 or LGPL-3.0+'], True),
            **dict.fromkeys(nodes['MPL-2.0'], False)
        }
    ),
    **dict.fromkeys(nodes['AFL-3.0'], {
            **dict.fromkeys(nodes['OSL-3.0'], True)
        }
    ),
    **dict.fromkeys(nodes['MPL-1.1'], {
            **dict.fromkeys(nodes['MPL-2.0'], False),
            **dict.fromkeys(nodes['CDDL-1.0'], True),
        }
    ),
    **dict.fromkeys(nodes['MPL-1.1+'], {
            **dict.fromkeys(nodes['MPL-1.1'], True),
            **dict.fromkeys(nodes['CDDL-1.0'], True),
            **dict.fromkeys(nodes['MPL-2.0'], True),
        }
    ),
    **dict.fromkeys(nodes['MPL-2.0'], {
            **dict.fromkeys(nodes['LGPL-2.1+'], True)
        }
    ),
    **dict.fromkeys(nodes['LGPL-2.1+'], {
            **dict.fromkeys(nodes['LGPL-3.0 or LGPL-3.0+'], True),
            **dict.fromkeys(nodes['LGPL-2.1'], True),
            **dict.fromkeys(nodes['GPL-2.0+'], True),
        }
    ),
    **dict.fromkeys(nodes['LGPL-3.0 or LGPL-3.0+'], {
            **dict.fromkeys(nodes['GPL-3.0 or GPL-3.0+'], True),
        }
    ),
    **dict.fromkeys(nodes['LGPL-2.1'], {
            **dict.fromkeys(nodes['GPL-2.0'], True),
            **dict.fromkeys(nodes['GPL-2.0+'], True),
        }
    ),
    **dict.fromkeys(nodes['GPL-2.0+'], {
            **dict.fromkeys(nodes['GPL-2.0'], True),
            **dict.fromkeys(nodes['GPL-3.0 or GPL-3.0+'], True),
        }
    ),
    **dict.fromkeys(nodes['GPL-3.0 or GPL-3.0+'], {
            **dict.fromkeys(nodes['AGPL-3.0'], True),
        }
    ),
    **dict.fromkeys(nodes['AGPL-1.0+'], {
            **dict.fromkeys(nodes['AGPL-3.0'], True),
        }
    ),
    **dict.fromkeys(nodes['CDDL-1.0'], {}),
    **dict.fromkeys(nodes['OSL-3.0'], {}),
    **dict.fromkeys(nodes['GPL-2.0'], {}),
    **dict.fromkeys(nodes['AGPL-3.0'], {}),
}