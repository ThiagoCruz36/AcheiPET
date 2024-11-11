from setuptools import setup, find_packages

setup(
    name="achei_pet",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'altair==5.3.0',
        'attrs==24.2.0',
        'bcrypt==4.2.0',
        'blinker==1.8.2',
        'cachetools==5.4.0',
        'certifi==2024.7.4',
        'charset-normalizer==3.3.2',
        'click==8.1.7',
        'colorama==0.4.6',
        'cssselect==1.2.0',
        'cssutils==2.11.1',
        'gitdb==4.0.11',
        'GitPython==3.1.43',
        'idna==3.7',
        'Jinja2==3.1.4',
        'jsonschema==4.23.0',
        'jsonschema-specifications==2023.12.1',
        'lxml==5.2.2',
        'markdown-it-py==3.0.0',
        'MarkupSafe==2.1.5',
        'mdurl==0.1.2',
        'more-itertools==10.4.0',
        'numpy==2.0.1',
        'packaging==24.1',
        'pandas==2.2.2',
        'pillow==10.4.0',
        'premailer==3.10.0',
        'protobuf==5.27.3',
        'psycopg2==2.9.9',
        'pyarrow==17.0.0',
        'pydeck==0.9.1',
        'Pygments==2.18.0', 
        'python-dateutil==2.9.0.post0',
        'python-dotenv==1.0.1',
        'pytz==2024.1',
        'referencing==0.35.1',
        'requests==2.32.3',
        'rich==13.7.1',
        'rpds-py==0.20.0',
        'six==1.16.0',
        'smmap==5.0.1',
        'streamlit==1.37.1',
        'streamlit-folium==0.23.1',
        'tenacity==8.5.0',
        'toml==0.10.2',
        'toolz==0.12.1',
        'tornado==6.4.1',
        'typing_extensions==4.12.2',
        'tzdata==2024.1',
        'urllib3==2.2.2',
        'watchdog==4.0.1',
    ],
    entry_points={
        'console_scripts': [
            'achei_pet = main:main',
        ],
    },
    include_package_data=True,
    description="Projeto para cadastro e visualização de PETs abandonados ou perdidos",
    author="Thiago Augusto Silva da Cruz",
    author_email="thiagoaugustocruz@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.*",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)