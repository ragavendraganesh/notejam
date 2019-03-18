from notejam import app
from notejam.config import DevelopmentConfig, ProductionConfig, TestingConfig
import os

environ_type = os.getenv("ENVTYPE", ProductionConfig)
app.config.from_object(environ_type)

if __name__ == '__main__':
    app.run()
