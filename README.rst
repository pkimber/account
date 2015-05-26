finance
*******

Django application for accounting/financial transactions.

Install
=======

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-finance
  source venv-finance/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Update your environment with these variables::

  source venv-finance/bin/activate

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Release
=======

https://www.pkimber.net/open/
