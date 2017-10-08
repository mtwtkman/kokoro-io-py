.. image:: https://badge.fury.io/py/kokoroio.svg
    :target: https://badge.fury.io/py/kokoroio

############
What is this
############
This is a client for `kokoro.io <https://kokoro.io/>`_ which is a chat service (maybe going to be) best ever.

I know that you want to join as soon as possible, please ask `me <https://twitter.com/mtwtkman>`_ or `supermomonga-san <https://twitter.com/supermomonga>`_ about how to create account.

############
Requirements
############
- Python3.6+
- kokoro.io account(using your access token)

########
Install
########
.. code-block:: bash

   $ pip install kokoroio

#########
Configure
#########
You must set an access token to sign in to kokoro.io by three way like follows.

- Set environ path named ``KOKOROIO_ACCESS_TOKEN``.
- Set your access token to any file your choice and pass it's file name to ``Kokoroio`` constructor as ``env_path``.
- Pass directly ``Kokoroio`` constructor as ``access_token``.

#####
Usage
#####
Once you create ``Kokoroio`` instance, you can request from two way syncronous or asyncronous.

.. code-block:: python

   from kokoroio import Kokoroio
   client = Kokoroio(access_token='xxxxxxx')
   client.channels.get()  # You received a response!

If an endpoint requires path parameters, you need to pass path parameters as arguments for request method.

.. code-block:: python

   # Assuming you want to post a message to channel whose channel_id is 'hogehoge'.
   # Url is `channels/<channel_id>`.
   o = client.channels.send_message(channle_id='hogehoge')
   # So you can request with a payload.
   o(message='hi')

   # Ordinary...
   client.channels.send_message(channle_id='hogehoge')(message='hi')

And you can find every client's methods.

.. code-block:: python

  clients.channels.method_names
  clients.channels.methods

===================
Syncronous request
===================
You will get ``requests's HttpResponse`` object.

If you want to know about response object, please refer `requests doc <http://docs.python-requests.org/en/master/>`_.

-------
Example
-------
.. code-block:: python

   >>> client.channels.get()

===================
Asyncronous request
===================
Different from syncronous version, request method has ``a`` prefix like ``channels.aget()`` and you don't need to create new event loop at every request.

You will get ``aiohttp's ClientResponse`` object because using ``aiohttp`` internally.

If you want to know about ``aiohttp``, please refer `aiohttp doc <http://aiohttp.readthedocs.io/en/stable/>`_.

-------
Example
-------
.. code-block:: python

   >>> client.channels.aget()

####
Test
####
Sorry now I have no test😭

############################
About kokoro.io's API detail
############################
You can find all of current API detail from `the official apidoc <https://kokoro.io/apidoc>`_.
