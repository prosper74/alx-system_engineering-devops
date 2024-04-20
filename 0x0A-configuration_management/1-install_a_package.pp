#!/usr/bin/pup
# Install flask from pip3.
# Requirements:
#   Install flask
#   Version must be 2.1.0
exec { 'install flask':
  command =>  'pip3 install flask==2.1.0',
  path    =>  '/usr/bin/',
  unless  =>  'pip3 list | grep flask',
}
