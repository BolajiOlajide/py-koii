# KOII

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

Python module for displaying routes in a flask application. This is a python variant for [Koii](https://github.com/BolajiOlajide/koii). It's a simple to use flask middleware that simply prints all the routes in a Flask application on the console.

## Installation

Koii is easy to install - it currently can be installed using the `pip` or `pipenv` command.

```sh
pip install koii
```

```sh
pipenv install koii
```

### Usage

To make use of Koii, ensure you initialize the middleware by passing the instance of your flaks app into the class or the `init_app` method. Ensure the class is initialized after your routes have been defined. If you're making use of blueprints, the same also applies, place the initialisation of the class after your blue print registration.

```py
from koii import Koii

app = Flask(__name__)

Koii(app)  # alternatively Koii.init_app(app)
```

An example file can be [found here](https://github.com/BolajiOlajide/koii-py/blob/master/example.py).

![Koii is inspired by Jackie and the fish](images/screenshot.png)

[![Support me via Patreon](https://github.com/BolajiOlajide/folly/blob/master/static/patreon.png)](https://www.patreon.com/bePatron?u=14962348)
