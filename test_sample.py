import os
def test_sample_true():
    assert True
    secret = os.getenv('super_secret')
    print("secret")
    print(secret)
   
