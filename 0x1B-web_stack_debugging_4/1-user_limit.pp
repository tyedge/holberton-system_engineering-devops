# This manifest increases allowed requests allowed on server
exec {'increase allowed requests':
  command => 'sed -i "s/5/5000/g; s/4/5000/g" /etc/security/limits.conf',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}
