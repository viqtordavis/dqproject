FROM python:3.7.7-slim-stretch

ENV PYTHONUNBUFFERED 1
# Project files
ARG PROJECT_DIR=/project_dq/app/
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

# Copy drivers
COPY ./init/drivers ./drivers

# Add dependencies for Python package pyodbc
RUN apt-get update \
    && apt-get install -y g++ unixodbc-dev

RUN apt-get install -y default-libmysqlclient-dev

# Add Cloudera Hive ODBC driver
RUN dpkg -i ./drivers/clouderahiveodbc_2.5.25.1020-2_amd64.deb

# Add FreeTDS ODBC driver for Microsoft SQL Server
RUN apt-get install -y tdsodbc

# Add MySQL ODBC driver
RUN tar xvzf ./drivers/mysql-connector-odbc-8.0.12-linux-debian9-x86-64bit.tar.gz \
    && cp ./mysql-connector-odbc-8.0.12-linux-debian9-x86-64bit/lib/libmyodbc8* /usr/lib/x86_64-linux-gnu/odbc/ \
    && rm -R ./mysql-connector-odbc-8.0.12-linux-debian9-x86-64bit

# Add PostgreSQL ODBC driver
RUN apt-get install -y odbc-postgresql

# Add Teradata ODBC driver
RUN apt-get install -y lib32stdc++6 \
    && tar xvzf ./drivers/tdodbc1620__ubuntu_indep.16.20.00.36-1.tar.gz \
    && dpkg -i ./tdodbc1620/tdodbc1620-16.20.00.36-1.noarch.deb \
    && rm -R ./tdodbc1620


# Install Python dependencies
COPY ./init/requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Move ODBC configuration file
COPY ./init/odbcinst.ini /etc



# Deleting drivers packages
RUN rm -R drivers

# Copy code as late as possible
COPY ./ ./

#CMD [ "python","manage.py","createsuperuser" ]

