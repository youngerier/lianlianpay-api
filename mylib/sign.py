from Crypto.Hash import MD5

def my_hash111(data):
    return MD5.new(data.encode('utf-8'))