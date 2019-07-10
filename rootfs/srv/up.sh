#!/usr/bin/with-contenv /bin/sh
set -eu
# Init database

chown shepherd.nogroup /srv/shepherd
cd /srv/shepherd
[ -e "/local/venv_shepherd/bin/activate" ] && . /local/venv_shepherd/bin/activate
init-flask-db.sh shepherd apluslms_shepherd
# wait for it to start
while ! setuidgid shepherd psql "--command=SELECT version();" >/dev/null 2>&1; do
    sleep 0.2
done

# Starting main server
setuidgid shepherd python3 app.py
# Starting message broker
#setuidgid shepherd python /apluslms_shepherd/message_broker/broker.py