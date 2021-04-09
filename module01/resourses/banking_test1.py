from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73cclass CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.name = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self, data):
        with open(self.name, 'w') as f:
            str1 = self.sep.join([str(elm) for elm in data])
            f.write('\n' + str)
        f.close()

    def __exit__(self):
        return87',
        info=None,
        other='This is the vice president of the corporation'
    ))

    if bank.transfer('William John', 'Smith Jane', 545.0) is False:
        print('Failed')
    else:
        print('Success')
