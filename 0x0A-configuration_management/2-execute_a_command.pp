#This manifest kills the killmenow process using pkill
exec { 'pkill -f killmenow':
    command => '/usr/bin/pkill -f killmenow'
}
