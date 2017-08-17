#######################
from __future__ import unicode_literals, print_function
#######################
METADATA_VERSIONS = {
    '1.0': ('platform','summary','description','keywords','home_page',
            'author','author_email', 'license', ),
    '1.1': ('platform','supported_platform','summary','description',
            'keywords','home_page','download_url','author','author_email',
            'license','classifier','requires','provides','obsoletes',),
    '1.2': ('platform','supported_platform','summary','description',
            'keywords','home_page','download_url','author','author_email',
            'maintainer','maintainer_email','license','classifier',
            'requires_dist','provides_dist','obsoletes_dist',
            'requires_python','requires_external','project_url')}

METADATA_LICENSES = (
    'Artistic',
    'BSD',
    'DFSG',
    'GNU GPL',
    'GNU LGPL',
    'MIT',
    'Mozilla PL',
    'public domain',
    'Python',
    'Qt',
    'PL',
    'Zope PL',
    'unknown',
    'nocommercial',
    'nosell',
    'nosource',
    'shareware',
    'other',
)
