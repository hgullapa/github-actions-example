import os
def test_sample_true():
    assert True
    secret = os.getenv('super_secret')
    add = int(secret) + 20 
    print(add)
   
