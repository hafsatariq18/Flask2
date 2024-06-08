from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://admin:darkspell@database-1.cxg6uyogcz4r.us-east-2.rds.amazonaws.com/project?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
           "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

