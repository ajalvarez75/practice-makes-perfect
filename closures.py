def make_repeater_of(number):
    def repeater(string):
        assert type(string) == str, "you can only use strings"
        return string * number
    return repeater

def run():
	repeat_5 = make_repeater_of(5)
	print(repeat_5("hola "))

if __name__ == '__main__':
	run()