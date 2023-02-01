#!/bin/bash
# Renew all expiring active certificates on a host (add --force-renew for all)

sudo find /etc/letsencrypt/live/ -maxdepth 1 -type d -not -name live -exec sh -c 'for domain do ~/letsencrypt/letsencrypt-auto renew --cert-name $(basename $domain); done' sh {} \;

# Then test and restart nginx
