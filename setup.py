from setuptools import setup

setup(
    name="sphinx-au-theme",
    entry_points={
        "sphinx.html_themes": [
            "au = sphinx_au_theme",
        ]
    },
    zip_safe=False,
    packages=['sphinx_au_theme'],
    package_data={'sphinx_au_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    install_requires=["sphinx"],
)

