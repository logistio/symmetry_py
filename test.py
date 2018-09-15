from symmetry_py.util import equinox 

timestamp = '2018-09-24 09:00:00.000000'
ts = equinox.from_postgres_timestamp(timestamp)

print(equinox.to_format(ts, equinox.DB_DATE_FORMAT))