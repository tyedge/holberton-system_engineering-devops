# This manifest changes limit of allowed requests
exec { 'increase allowed requests':
    command => 'sed -i "s/15/15000/g" /etc/default/nginx; sudo service nginx restart',
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}
