#install flast on agent sever
package { 'flask':
  ensure   => '2.1.0'
  provider => 'pip3',
}
