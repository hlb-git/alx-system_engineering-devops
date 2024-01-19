#manifest to kill a process
exec{ 'kill process':
  command  => /usr/bin/pkill -f 'killmenow',
}
