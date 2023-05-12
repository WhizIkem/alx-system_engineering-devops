# Use Puppet to automate the task of creating a custom HTTP header response

exec {'update':
  command   => '/usr/bin/apt-get -y update',
}

package {'nginx':
  ensure    => installed,
  require   => Exec['update']
}

file_line { 'redirect':
  ensure    => 'present',
  path      => '/etc/nginx/sites-available/default',
  after     => 'server_name _;',
  line      => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require   => Package['nginx'],
}

file_line { 'header':
  ensure    => 'present':
  path      => '/etc/nginx/sites-available/default',
  after     => 'server_name _',
  line      => 'add_header X-Served-By "$HOSTNAME";',
  require   => Package['nginx'],
}

file { '/var/www/html/index.html':
  content   => /'Hello World!',
  require   => Package['nginx'],
}

exec {'run':
  command   => '/usr/sbin/service nginx restart',
}
