file {'~/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => '
    #configuration file
	PasswordAuthentication no
	PubkeyAuthentication yes
	',
}
