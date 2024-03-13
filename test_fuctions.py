import pytest
from functions_template import getAllEmpData, getDeptEmpData, getDesgEmpData
import toml
import pymysql

config = toml.load('secret.toml')

@pytest.fixture(scope='module')
def db_connection():
    # Establish a database connection for testing
    connection = pymysql.connect(
        host=config['database']['host'],
        user=config['database']['username'],
        password=config['database']['password'],
        database=config['database']['database'],
        port=config['database']['port']
    )
    yield connection
    connection.close()

def test_getAllEmpData(db_connection):
    result = getAllEmpData()
    assert isinstance(result, list)
    assert len(result) > 0

def test_getDeptEmpData(db_connection):
    result = getDeptEmpData("HR")
    assert isinstance(result, list)

def test_getDesgEmpData(db_connection):
    result = getDesgEmpData("Manager")
    assert isinstance(result, list)