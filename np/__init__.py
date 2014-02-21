from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import pyramid_beaker
import os
import ConfigParser
from np.lib import store

from .models import (
    DBSession,
    Base,
    )


def loadSafe(safePath):
    """
    Load information that we do not want to include in the repository
    """
    # Validate
    if not os.path.exists(safePath):
        print 'Missing configuration: ' + safePath
        safePath = store.expandBasePath('default.cfg')
    # Initialize
    valueByName = {}
    # Load
    configuration = ConfigParser.ConfigParser() 
    configuration.read(safePath)
    for sectionName in configuration.sections(): 
        valueByName[sectionName] = dict(configuration.items(sectionName)) 
    # Return
    return valueByName

def main(global_config, **settings):
    """ 
    This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.include(pyramid_beaker)
    config.scan()
    config['safe'] = loadSafe(config['safe_path'])
    return config.make_wsgi_app()
