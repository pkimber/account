finance
*******

Django application for accounting/financial transactions.

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-finance
  source venv-finance/bin/activate
  pip install --upgrade pip

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

https://www.kbsoftware.co.uk/docs/
