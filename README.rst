============
What is this
============
This is a client for `kokoro.io <https://kokoro.io/>`_ which is a chat service (maybe going to be) best ever.

I know that you want to join as soon as possible, please ask `me <https://twitter.com/mtwtkman>`_ or `supermomonga-san <https://twitter.com/supermomonga>`_ about how to create account.

============
Requirements
============
- Python3.6+
- kokoro.io account(using your access token)

========
Install
========
.. code-block:: bash

   $ pip install kokoroio

=========
Configure
=========
You must set an access token to sign in to kokoro.io by three way like follows.

- Set environ path named ``KOKOROIO_ACCESS_TOKEN``.
- Set your access token to any file your choice and pass it's file name to ``Kokoroio`` constructor as ``env_path``.
- Pass directly ``Kokoroio`` constructor as ``access_token``.

=====
Usage
=====
Once you create ``Kokoroio`` instance, you can get requests's HttpResponse instance anytime your request.

If you want to know about response object, please reference `requests doc <http://docs.python-requests.org/en/master/>`_.

Very simple✨

=======
Example
=======
.. code-block:: python

   >>> from kokoroio import Kokoroio
   >>> client = Kokoroio(access_token='xxxxxxxxx')
   >>> json_response = client.channels.get().json()

====
Test
====
Sorry now I have no test😭

============================
About kokoro.io's API detail
============================
You can find all of current API detail from `the official apidoc <https://kokoro.io/apidoc>`_.
