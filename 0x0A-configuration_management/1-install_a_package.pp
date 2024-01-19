#install flast on agent sever
exec { 'install_flask':
  command => 'usr/bin/pip3 install Flask==2.1.0',
  path    => ['usr/bin/pip3', 'usr/local/bin/pip3'],
  unless  => 'usr/bin/pip3' show Flask | grep -q 'version: 2.1.0',
}
