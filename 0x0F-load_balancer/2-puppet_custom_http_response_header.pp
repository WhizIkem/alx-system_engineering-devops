# Use Puppet to automate the task of creating a custom HTTP header response

exec {'update':
  command   => '/usr/bin/apt-get -y update',
}

-> package {'nginx':
  ensure    => 'present',
}

-> file_line { 'header':
  path      => '/etc/nginx/sites-available/default',
  after     => 'server_name _',
  line      => 'add_header X-Served-By "$HOSTNAME";',
  require   => Package['nginx'],
}

-> service {'nginx':
  ensure   => running,
  require  => Package['nginx'],
}
