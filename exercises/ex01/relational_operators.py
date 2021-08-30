"""This is the relational operators program. """

__author__ = "730239378"

string_1: str = input("Left-hand side: ")
string_2: str =  input("Right-hand side: ")

integer_3 = int(string_1)
integer_4 = int(string_2)

print(string_1 + " < " + string_2 + " is " + str(integer_3<integer_4))
print(string_1 + " >= " + string_2 + " is " + str(integer_3>=integer_4))
print(string_1 + " == " + string_2 + " is " + str(integer_3==integer_4))
print(string_1 + " != " + string_2 + " is " + str(integer_3!=integer_4))
