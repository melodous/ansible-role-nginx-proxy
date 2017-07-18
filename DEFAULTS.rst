.. vim: foldmarker=[[[,]]]:foldmethod=marker

nginx ansible role default variables
====================================

.. contents:: Sections
   :local:

nginx docker management
-----------------------

.. envvar:: nginx_docker_image

nginx docker image
::

  nginx_docker_image: nginx




.. envvar:: nginx_version

nginx docker image version (TAG)
::

  nginx_version: 1.13.3




.. envvar:: nginx_docker_labels

Yaml dictionary which maps Docker labels.
os_environment: Name of the environment, example: Production, by default "default".
os_contianer_type: Type of the container, by default nginx.
::

  nginx_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: nginx




nginx configuration management
------------------------------

.. envvar:: nginx_path

   Path for nginx configurations files

::

  nginx_path: /etc/nginx




.. envvar:: dh_size

   Diffie-Hellman size

::

  dh_size: 2048




.. envvar:: nginx_proxy_ssl_store_path

   Define path to store ssl certificates

::

  nginx_proxy_ssl_store_path: '{{ nginx_path }}/ssl'




.. envvar:: nginx_proxy_ssl_virtual_sites

   List of ssl virtual sites

::

  nginx_proxy_ssl_virtual_sites: ''


Example:

.. code::yaml

::

  #		nginx_proxy_ssl_virtual_sites:
  #			- {
  #			site_id: 'example.com', # will be the name for upstream server and the sites-available file, must be unique
  #			disable_http: true
  #			http_port: 80, # http port for nginx to listen to (default: 80)
  #			https_port: 443, # https port for nginx to listen to (default: 443)
  #			server_names: '*.se', # server names to listen for
  #			upstream_server: '10.10.10.10:80', # upstream server/port to connect to
  #			upstream_extras: [], # extra config directives for upstream
  #			proxy_pass: 'http://10.10.10.10', # proxy pass should be the http-link to pass requests to
  #			ssl_cert: 'certificate', # certificate data
  #			ssl_key: 'key', # key data
  #			ssl_protocols: 'TLSv1 TLSv1.1 TLSv1.2', # ssl protocols we should accept for this site (default: 'TLSv1 TLSv1.1 TLSv1.2')
  #			#proxy_redirect: ''
  #			#custom_http_block: '', # here we can substitute the standard http->https redirect block with a custom server {} block if we want
  #			#custom_https_block: '', # here we can substitute the standard https proxy pass block with a custom server {} block if we want
  #			}
  #			- {
  #			site_id: 'proxy_ssl2.com', # will be the name for upstream server and the sites-available file, must be unique
  #			http_port: 80, # http port for nginx to listen to (default: 80)
  #			https_port: 443, # https port for nginx to listen to (default: 443)
  #			server_names: 'proxy_ssl2.com', # server names to listen for
  #			upstream_server: '10.10.10.100:80', # upstream server/port to connect to
  #			upstream_extras: [], # extra config directives for upstream
  #			proxy_pass: 'http://10.10.10.100', # proxy pass should be the http-link to pass requests to
  #			ssl_cert: 'certificate', # certificate data
  #			ssl_key: 'key', # key data
  #			ssl_protocols: 'TLSv1 TLSv1.1 TLSv1.2', # ssl protocols we should accept for this site (default: 'TLSv1 TLSv1.1 TLSv1.2')
  #			#custom_http_block: '', # here we can substitute the standard http->https redirect block with a custom server {} block if we want
  #			#custom_https_block: '', # here we can substitute the standard https proxy pass block with a custom server {} block if we want
  #			#proxy_redirect: ''
  #			}





.. envvar:: nginx_proxy_virtual_sites

   List of non-ssl virtual sites

::

  nginx_proxy_virtual_sites: ''


Example:

.. code::yaml

::

  #		nginx_proxy_virtual_sites:
  #		  - {
  #		  site_id: 'proxy_http', # will be the name for upstream server and the sites-available file, must be unique
  #		  http_port: 80, # http port for nginx to listen to (default: 80)
  #		  server_names: 'proxy_http.com', # server names to listen for
  #		  upstream_server: '10.1.1.87:80', # upstream server/port to connect to
  #		  upstream_extras: [], # extra config directives for upstream
  #		  proxy_pass: 'http://10.1.1.87', # proxy pass should be the http-link to pass requests to
  #		  custom_http_block: '', # here we can substitute the standard http proxy pass block with a custom server {} block if we want
  #		  }






.. envvar:: nginx_redirect_ssl_virtual_sites

   List of http(s) 301 redirects

::

  nginx_redirect_ssl_virtual_sites: ''


Example:

.. code::yaml

::

  #	   nginx_redirect_ssl_virtual_sites:
  #	     - {
  #	     site_id: 'redirect_ssl', # will be the name for upstream server and the sites-available file, must be unique
  #	     http_port: 80, # http port for nginx to listen to (default: 80)
  #	     https_port: 443, # https port for nginx to listen to (default: 443)
  #	     server_names: 'redirect_ssl.com', # server names to listen for
  #	     http_redirect: 'https://domain.com', # URL that your http_port should redirect to
  #	     https_redirect: 'https://domain.com', # URL that your https_port should redirect to
  #	     ssl_cert: 'certificate', # certificate data
  #	     ssl_key: 'key', # key data
  #	     ssl_protocols: 'TLSv1 TLSv1.1 TLSv1.2', # ssl protocols we should accept for this site
  #	     custom_http_block: '', # here we can substitute the standard http->https redirect block with a custom server {} block if we want
  #	     custom_https_block: '', # here we can substitute the standard https proxy pass block with a custom server {} block if we want
  #	     }





.. envvar:: nginx_redirect_virtual_sites

   List of only http 301 redirects

::

  nginx_redirect_virtual_sites: ''


Example:

.. code::yaml

::

  #	   nginx_redirect_virtual_sites:
  #	     - {
  #	     site_id: 'redirect', # will be the name for upstream server and the sites-available file, must be unique
  #	     http_port: 80, # http port for nginx to listen to (default: 80)
  #	     server_names: 'redirect.com', # server names to listen for
  #	     http_redirect: 'https://domain.com', # URL that your http_port should redirect to
  #	     # custom_http_block: '' # here we can substitute the standard http proxy pass block with a custom server {} block if we want
  #	     }





.. envvar:: nginx_custom_vhosts

   Custom virtual host

::

  nginx_custom_vhosts: ''


Example:

.. code::yaml

::

  #	   nginx_custom_vhosts:
  #	     - name: test
  #	       content: |
  #	       nginx_full_vhost





