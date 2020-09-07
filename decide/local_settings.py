ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]
BASEAURL = 'http://127.0.0.1:8000'

APIS = {
    'authentication': 'http://127.0.0.1:8000',
    'base': 'http://127.0.0.1:8000',
    'booth': 'http://127.0.0.1:8000',
    'census': 'http://127.0.0.1:8000',
    'mixnet': 'http://127.0.0.1:8000',
    'postproc': 'http://127.0.0.1:8000',
    'store': 'http://127.0.0.1:8000',
    'visualizer': 'http://127.0.0.1:8000',
    'voting': 'http://127.0.0.1:8000',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_examen',
        'USER': 'sergio',
        'PASSWORD': 'serpermar2',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
