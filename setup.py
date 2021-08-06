import os
import sys

from setuptools import find_packages
from setuptools import setup

version = '0.2.1'
certbot_version = '0.31.0'

install_requires = [
    # This version of lexicon is required to address the problem described in
    # https://github.com/AnalogJ/lexicon/issues/387.
    'dns-lexicon>=3.2.3',
    'setuptools>=39.0.1',
    'zope.interface',
    'urllib3>=1.26.4'
]

# docs_extras = [
#     'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
#     'sphinx_rtd_theme',
# ]

if not os.environ.get('IS_SNAP'):
    install_requires.extend([
        # We specify the minimum acme and certbot version as the current plugin
        # version for simplicity. See
        # https://github.com/certbot/certbot/issues/8761 for more info.
        f'acme>={version}',
        f'certbot>={version}',
    ])
elif 'bdist_wheel' in sys.argv[1:]:
    raise RuntimeError('Unset SNAP_BUILD when building wheels '
                       'to include certbot dependencies.')

if os.environ.get('IS_SNAP'):
    install_requires.append('packaging')

setup(
    name='certbot-dns-godaddy',
    version=version,
    description="Godaddy DNS Authenticator plugin for Certbot",
    url='https://github.com/certbot/certbot',
    author="Certbot Project",
    author_email='certbot-dev@eff.org',
    license='Apache License 2.0',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={},
    entry_points={
        'certbot.plugins': [
            'dns-godaddy = certbot_dns_godaddy.certbot_dns_godaddy:Authenticator',
        ],
    },
)
