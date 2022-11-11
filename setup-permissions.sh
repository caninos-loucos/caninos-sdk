# gpio and i2c needs to be re-configured after every reboot
cat << EOF >/usr/local/sbin/caninos-sdk-permissions.sh
#!/bin/bash
# gpio
chown caninos /dev/gpiochip*
chmod g+rw /dev/gpiochip*
# i2c
chown caninos /dev/i2c-2
chmod g+rw /dev/i2c-2
EOF

# serial needs to be configured only once
usermod -aG dialout caninos

chmod 0700 /usr/local/sbin/caninos-sdk-permissions.sh

cat << EOF >/etc/systemd/system/caninos-sdk-permissions.service
[Unit]
Description=Enables the 'caninos' user to use gpio, i2c, and serial
[Service]
ExecStart=/usr/local/sbin/caninos-sdk-permissions.sh
[Install]
WantedBy=multi-user.target
EOF

systemctl enable caninos-sdk-permissions.service
systemctl start caninos-sdk-permissions.service