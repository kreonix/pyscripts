import unittest


def generate_table():
    table = '<html><table style="border-spacing: 0">'
    for i in range(255):
        table += "<tr><td style=\"width: 200px; height: 1px; border: none; border-spacing: 0px; background-color:rgb(" + str(
            i) + "," + str(i) + "," + str(
            i) + ");\"></td></tr>"
    table += '</table></html>'
    return table

class TestProgram(unittest.TestCase):
    def test_generate_table(self):
        print(generate_table().split())
        self.assertRegex(generate_table(), '<html><table style="border-spacing: 0">')

if __name__ == '__main__':
    unittest.main()
    f = open("table.html", "w+")
    f.write(generate_table())
    f.close()
