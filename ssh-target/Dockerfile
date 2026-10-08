FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y openssh-server sudo && \
    mkdir /var/run/sshd

RUN useradd -m -s /bin/bash analyst && \
    echo "analyst:BrokenGate123" | chpasswd

RUN echo "FLAG{initial_access_success}" > /home/analyst/user.txt && \
    chown analyst:analyst /home/analyst/user.txt

RUN echo "FLAG{root_access_complete}" > /root/root.txt

# Intentionally vulnerable backup script for the CTF
RUN echo '#!/bin/bash' > /usr/local/bin/backup.sh && \
    echo 'echo "Backup completed successfully."' >> /usr/local/bin/backup.sh && \
    chmod 777 /usr/local/bin/backup.sh

# Allow analyst to run the backup script as root without a password
RUN echo 'analyst ALL=(root) NOPASSWD: /usr/local/bin/backup.sh' \
    > /etc/sudoers.d/analyst-backup && \
    chmod 440 /etc/sudoers.d/analyst-backup

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]