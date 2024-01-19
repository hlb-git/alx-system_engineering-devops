#install flast on agent sever
exec { 'flask':
  command  => '/usr/bin/pip3 install Flask==2.1.0',
  path     => ['/usr/bin', '/usr/local/bin'],
  provider => 'pip3',
  unless   => '/usr/bin/pip3 show Flask | grep -q 'Version: 2.1.0'',
}
