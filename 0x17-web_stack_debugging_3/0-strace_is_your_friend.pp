# This puppet manifest corrects typo with sed
exec { 'sed text substitution':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}
