cat << EOF >/usr/local/sbin/gpio-rights.sh
#!/bin/bash
chown caninos /dev/gpiochip*
chmod g+rw /dev/gpiochip*
EOF

chmod 0700 /usr/local/sbin/gpio-rights.sh

cat << EOF >/etc/systemd/system/gpio-rights.service
[Unit]
Description=Fix permission for gpio owner
[Service]
ExecStart=/usr/local/sbin/gpio-rights.sh
[Install]
WantedBy=multi-user.target
EOF

systemctl enable gpio-rights.service
systemctl start gpio-rights.service