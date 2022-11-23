from Crypto.Hash import MD5

def my_hash111(data):
    return MD5.new(data.encode('utf-8')).hexdigest()


def read_file(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            print(line)



