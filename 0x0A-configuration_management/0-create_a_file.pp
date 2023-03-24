# CREATE A FILE AT /TMP
file { '/tmp/school/:
    ensure => 'file'
    owner => 'www-data'
    group => 'www-dsta'
    mode => '0744'
    content => 'I love Puppet'
}
