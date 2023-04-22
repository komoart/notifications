"""Module for extract data from postgres."""
import logging

import backoff
import contextlib
import psycopg2
from psycopg2.extras import DictCursor

from settings import settings


class PostgresExtractor:
    """This class extracts data from psql."""

    @backoff.on_exception(backoff.expo, exception=ConnectionError)
    def extract_modified_data(self, date: str, query: str, offset_counter: int):
        """Extract movies, checked modified movies.

        Returns:
            movies_modified_list(list): list with movies
        """
        with contextlib.closing(psycopg2.connect(**settings.dsn.dict(), cursor_factory=DictCursor)) \
                as conn, conn.cursor() as cursor:
            
            print(date)
            query = query%(date, offset_counter)
            print(query)
            cursor.execute(query)
            movies_modified_batch = cursor.fetchmany(settings.batch_size)
            if len(movies_modified_batch) == 0:
                return None
        logging.info("Data extracted from postgres!")
        return movies_modified_batch
