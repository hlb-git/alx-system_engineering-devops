#install flast on agent sever
exec { 'Flask':
  ensure   => '2.1.0'
  provider => pip3,
}
