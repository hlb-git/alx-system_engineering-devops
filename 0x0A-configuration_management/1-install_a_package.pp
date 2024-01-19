#install flast on agent sever
exec { 'flask':
  ensure   => '2.1.0'
  provider => pip3,
}
