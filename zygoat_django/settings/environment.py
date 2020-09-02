import environ

env = environ.Env()

PRODUCTION = env.bool("DJANGO_PRODUCTION", default=False)


def prod_required_env(key, default, method="str"):
    """Throw an exception if PRODUCTION is true and key is not provided"""
    if PRODUCTION:
        default = environ.Env.NOTSET
    return getattr(env, method)(key, default)


ALLOWED_HOSTS = [prod_required_env("DJANGO_ALLOWED_HOST", default="*")]
