
only a try to use [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask) without [flask-admin](https://flask-admin.readthedocs.io/en/latest/). 

cookiecutter-flask provides a model User which has conflict with flask-admin.(see: (PR Add Flask-Admin)[https://github.com/sloria/cookiecutter-flask/pull/72/files]). So temp comment this line to disable cookiecutter User model `app.register_blueprint(user.views.blueprint)` in [app.py](https://github.com/scil/just-try-cookiecutter-flask/blob/master/uper/uper/app.py)

## flask-admin with flask-login?

Gived up at this stage: [This repository flask-react-spa is a good example of how flask-login and flask-security can be connected with flask-admin.](https://stackoverflow.com/questions/11804922/flask-admin-flask-login-and-or-flask-principal?rq=1)

These ways:
- [flask-react-spa](https://github.com/briancappello/flask-react-spa)
- [flask-admin flask-security](https://stackoverflow.com/questions/31091637/how-to-secure-the-flask-admin-panel-with-flask-security)
- [Flask-Admin vs Flask-AppBuilder](https://stackoverflow.com/questions/30126607/flask-admin-vs-flask-appbuilder)



