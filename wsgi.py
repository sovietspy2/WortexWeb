from app import app
import config

if __name__ == "__main__":
    app.run(host=config.settings['HOST'], debug=config.settings['DEBUG'], port=config.settings['PORT'])