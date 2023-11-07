def write_to_database(messages, approval, review_date_time, moderator_name, moderator_email):
        connection = psycopg2.connect(
            user="postgres",
            password="********",
            host="localhost",
            port_id="5432",
            database="Moderatie"
        )
        print(connection)