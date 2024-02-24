#!/usr/bin/pup
#install an especific version of pip
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}


