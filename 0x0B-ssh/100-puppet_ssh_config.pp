file { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  content  => 'PasswordAuthentication no',
}

file { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  content  => 'IdentityFile ~/.ssh/school',
}
