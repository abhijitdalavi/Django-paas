# Developer Notes
## Library
The goal of this article is to keep track the libraries that this project is dependent on.

### Python
Here are the libraries that this project utilizes, please update this list as
new libraries get added.

```bash
pip install pytz                          # World Timezone Definitions
pip install django                        # Our MVC Framework
pip install django-environ                # Environment Variables with 12factorization
pip install Pillow                        # Req: ImageField
pip install django-cors-headers           # Enable CORS in Headers
pip install gunicorn                      # Web-Server Helper
pip install django-htmlmin                # HTML Minify
pip install django-trapdoor               # Automatically Exploit Scanners
pip install psycopg2-binary               # Postgres SQL ODBC
pip install django-tenants                # Multi-Tenancy Handler
pip install djangorestframework           # RESTful API Endpoint Generator
pip install django-starterkit             # Django starter kit
pip install django_filter                 # Filter querysets dynamically
pip install djangorestframework-msgpack   # MessagePack support for Django REST framework
pip install djangorestframework-jwt       # JSON Web Token Authentication support for Django REST Framework
pip install django-rq                     # Redis Queue Library
pip install rq-scheduler                  # Redis Queue Scheduler Library
pip install django-anymail                # Third-Party Email
pip install whitenoise                    # Simplified static file serving for Python web apps
pip install brotlipy                      # Brotli compression format to be used by "whitenoise" library.
pip install django-filter                 # A generic system for filtering Django QuerySets based on user selections.
pip install django-money                  # Money fields for django forms and models.
pip install django-phonenumber-field      # Telephone field using Google's libphonenumber


#TODO: IMPLEMENT...
pip install dateutil                      # Useful extensions to the standard Python datetime features
# pip install django-crispy-forms           # Req: djangorestframework
pip install --upgrade django-brotli       # Middleware that compresses response using brotli algorithm
```
