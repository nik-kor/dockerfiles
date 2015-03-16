FROM stilliard/pure-ftpd
MAINTAINER Nikita Korotkih <nikita.korotkih@gmail.com>

RUN apt-get install -y expect
ADD create_user.exp /

RUN expect -f /create_user.exp
RUN pure-pw mkdb
