#%% str.format(*args, **kwargs)
# Perform a string formatting operation. 
# The string on which this method is called can contain literal text or replacement fields delimited 
# by braces {}. 
# Each replacement field contains either the numeric index of a positional argument
# ,or the name of a keyword argument. 
# Returns a copy of the string where each replacement field is replaced with 
# the string value of the corresponding argument.

"The sum of 1 + 2 is {0}".format(1+2)
# 'The sum of 1 + 2 is 3'

# Format String Syntax
# replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
# field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
# arg_name          ::=  [identifier | digit+]
# attribute_name    ::=  identifier
# element_index     ::=  digit+ | index_string
# index_string      ::=  <any source character except "]"> +
# conversion        ::=  "r" | "s" | "a"
# format_spec       ::=  <described in the next section>

# 最简短的格式化字符串由{}中的三部分组成，这三部分都是可选的。、
# 其中！和:是二三部分的引导符
# { [field_name][! conversion][: format_spec] } filed_name后面不可接空格

'{a:+.4f}'.format(a=-3.14) 
# '-3.1400'

'{b!s}'.format(b=3.14)
# '3.14'

import numpy as np
c = np.array([1,2,3,4,5])
'{c}'.format(c=c)
# '[1 2 3 4 5]'
'{c!r}'.format(c=c)
# 'array([1, 2, 3, 4, 5])'

#%% replacement_field 解析
# The field_name itself begins with an arg_name that is either a number or a keyword.
# If it’s a number, it refers to a positional argument
# , and if it’s a keyword, it refers to a named keyword argument

# If the numerical arg_names in a format string are 0, 1, 2, … in sequence, 
# they can all be omitted (not just some) 
# and the numbers 0, 1, 2, … will be automatically inserted in that order.
'{0}:{1}:{2}'.format('a','b','c')
# 'a:b:c'
'{2}:{1}:{0}'.format('a','b','c')
# 'c:b:a'
'{}:{}:{}'.format('a','b','c')
# 'a:b:c'

# 关键字参数可以使用字典解包的方式
'{para1}:{para2}:{para3}'.format(para1='a',para2='b',para3='c')
# 'a:b:c'
'{para3}:{para2}:{para1}'.format(para1='a',para2='b',para3='c')
# 'c:b:a'
d={'para1':'a','para2':'b','para3':'c'}
'{para1}:{para2}:{para3}'.format(**d)
# 'a:b:c'

# The arg_name can be followed by any number of index or attribute expressions. 
# An expression of the form '.name' selects the named attribute using getattr()
# , while an expression of the form '[index]' does an index lookup using __getitem__().
l = list([1,2,3])
class person:
    def __init__(self):
        self.name = 'a'
        self.age = 18
d = person()

'{l[0]}:{l[1]}:{l[2]}'.format(l=l)
# '1:2:3'
'{d.name}:{d.age}'.format(d=d)
# 'a:18'

# Summary
# "First, thou shalt count to {0}"  # References first positional argument
# "Bring me a {}"                   # Implicitly references the first positional argument
# "From {} to {}"                   # Same as "From {0} to {1}"
# "My quest is {name}"              # References keyword argument 'name'
# "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
# "Units destroyed: {players[0]}"   # First element of keyword argument 'players'.


#%% conversion field 解析
# The conversion field causes a type coercion before formatting. 
# Normally, the job of formatting a value is done by the __format__() method of the value itself. 
# However, in some cases it is desirable to force a type to be formatted as a string
# , overriding its own definition of formatting. 
# By converting the value to a string before calling __format__()
# , the normal formatting logic is bypassed.

# '!s' which calls str() on the value
# '!r' which calls repr()  
# '!a' which calls ascii()


"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first

class person:
    def __init__(self):
        self.name = 'a'
        self.age = 18
    def __repr__(self):
        return "of course, this is a test"

"Hello world! {d!r}".format(d=person())
# 'Hello world! of course, this is a test'

#%% format_spec 解析/Format Specification Mini-Language 
# The format_spec field contains a specification of how the value should be presented
# , including such details as field width, alignment, padding, decimal precision and so on. 
# Each value type can define its own “formatting mini-language” or interpretation of the format_spec.

# Most built-in types support a common formatting mini-language, which is described in the next section.

#%% Format Specification Mini-Language**********************************************************************
# “Format specifications” are used within replacement fields contained within a format string
#  to define how individual values are presented (see Format String Syntax and Formatted string literals). 
# They can also be passed directly to the built-in format() function. 
# Each formattable type may define how the format specification is to be interpreted.

# A general convention is that an empty format specification produces the same result 。
#  as if you had called str() on the value. 
# A non-empty format specification typically modifies the result.

# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"


#%% [[fill]align]/这个要结合[width]选项
# If a valid align value is specified
# , it can be preceded by a fill character that can be any character and defaults to a space if omitted. 

# fill:<any character>
# The meaning of the various alignment options is as follows:
    # '<': Forces the field to be left-aligned within the available space 
    #       (this is the default for most objects).
    # '>': Forces the field to be right-aligned within the available space (this is the default for numbers).
    # '=': Forces the padding to be placed after the sign (if any) but before the digits. 
    #       This is used for printing fields in the form ‘+000000120’. 
    #       This alignment option is only valid for numeric types. 
    #       It becomes the default when ‘0’ immediately precedes the field width.
    # '^': Forces the field to be centered within the available space.

# Note that unless a minimum field width is defined
#  , the field width will always be the same size as the data to fill it
#  , so that the alignment option has no meaning in this case.


#%% [sign]

# The sign option is only valid for number types, and can be one of the following:
    # '+': indicates that a sign should be used for both positive as well as negative numbers.
    # '-': indicates that a sign should be used only for negative numbers (this is the default behavior).
    # space: indicates that a leading space should be used on positive numbers
    #   , and a minus sign on negative numbers.

'{:+}; {:+}'.format(3.14, -3.14)  # show it always
# '+3.14; -3.14'

'{:-}; {:-}'.format(3.14, -3.14) # show only the minus -- same as '{:}; {:}'
# '3.14; -3.14'

'{: }; {: }'.format(3.14, -3.14)  # show a space for positive numbers
# ' 3.14; -3.14'


#%% [#]
# The '#' option causes the “alternate form” to be used for the conversion. 
# The alternate form is defined differently for different types. 
# This option is only valid for integer, float, complex and Decimal types. **** 
# For integers, when binary, octal, or hexadecimal output is used
#   , this option adds the prefix respective '0b', '0o', or '0x' to the output value. ****
# For floats, complex and Decimal the alternate form causes the result of the conversion to always contain a decimal-point character
#   , even if no digits follow it. 
# Normally, a decimal-point character appears in the result of these conversions only if a digit follows it. 
# In addition, for 'g' and 'G' conversions, trailing zeros are not removed from the result.

"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
# 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'

"int: {0:#d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
# 'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

"int: {0:f};  hex: {1:f};  oct: {2:f};  bin: {3:b}".format(42.3, -42.3, 0, -0)
# 'int: 42.300000;  hex: -42.300000;  oct: 0.000000;  bin: 0' ???

"int: {0:#f};  hex: {1:#f};  oct: {2:#};  bin: {3:}".format(42.3, -42.3, 42., -42.)
# 'int: 42.300000;  hex: -42.300000;  oct: 0.000000;  bin: 0b0' ???



#%% [grouping_option]

# The ',' option signals the use of a comma for a thousands separator. 
# For a locale aware separator, use the 'n' integer presentation type instead.

# The '_' option signals the use of an underscore for a thousands separator 
#   for floating point presentation types and for integer presentation type 'd'. 
# For integer presentation types 'b', 'o', 'x', and 'X', underscores will be inserted every 4 digits. 
# For other presentation types, specifying this option is an error.

"{:_d}".format(4200000)
# '4_200_000'
"{:,d}".format(4200000)
# '4,200,000'

#%% [width]

# width is a decimal integer defining the minimum total field width
#   , including any prefixes, separators, and other formatting characters. 
# If not specified, then the field width will be determined by the content.

"{:20_d}".format(4200000)
# '           4_200_000'

"{:20,d}".format(4200000)
'           4,200,000'

"{:<20,d}".format(4200000)
# '4,200,000           '

"{:=20d}".format(4200000)
# '             4200000'

"{:a=20d}".format(4200000)
# 'aaaaaaaaaaaaa4200000'

# 留意这两种是一样的[[fill:0]align:'='] = [[fill:0]align:空]
"{:020d}".format(4200000)
# '00000000000004200000'
"{:0=20d}".format(4200000)
# '00000000000004200000'


#%% [.precision]：注意精度选项以小数点开头
# The precision is a decimal number indicating how many digits should be displayed after the decimal point
#   for a floating point value formatted with 'f' and 'F'
#   , or before and after the decimal point for a floating point value formatted with 'g' or 'G'. 
# For non-number types the field indicates the maximum field size - in other words
#   , how many characters will be used from the field content. 
# The precision is not allowed for integer values.

# 只能在type=f|F|g|G的时候使用。

"{:020.5d}".format(4200000)
# ValueError: Precision not allowed in integer format specifier

"{:020.5f}".format(4200000)
# '00000004200000.00000'
#注意，精度长度也包含在[width]的范围内。

"{:020d}".format(4200000)
# '00000000000004200000'


#%% [type] the type determines how the data should be presented.

# string types are:
#   's':String format. This is the default type for strings and may be omitted.
#   None:The same as 's'.

# "{:20s}".format(4200000)
# ValueError: Unknown format code 's' for object of type 'int'

"{:20s}".format('4200000')
# '4200000             '
"{:20}".format('4200000')
# '4200000             '

"{!r:20s}".format('4200000')
# "'4200000'           "
"{!s:20s}".format('4200000')
# '4200000             '

# integer types are:
# 'b': Binary format. Outputs the number in base 2.
# 'c': Character. Converts the integer to the corresponding unicode character before printing.
# 'd': Decimal Integer. Outputs the number in base 10.
# 'o': Octal format. Outputs the number in base 8.
# 'x': Hex format. Outputs the number in base 16
#   , using lower-case letters for the digits above 9.
# 'X': Hex format. Outputs the number in base 16
#   , using upper-case letters for the digits above 9.
# 'n': Number. This is the same as 'd'
#   , except that it uses the current locale setting to insert the appropriate number separator characters.
# None: The same as 'd'.

"{:b}".format(42)
# '101010'
"{:#b}".format(42)
# 0b101010'

"{:c}".format(42) #42对应的字符
# '*'
"{:c}".format(48)
# '0'

"{:d}".format(42)
# '42'
"{:n}".format(42)
# '42'
"{:}".format(42)
# '42'

"{:o}".format(42)
# '52'
"{:#o}".format(42)
# '0o52'

"{:x}".format(42)
# '2a'
"{:X}".format(42)
# '2A'

# floating point and decimal
# 'e': Exponent notation. Prints the number in scientific notation 
#   using the letter ‘e’ to indicate the exponent. The default precision is 6.

# 'E': Exponent notation. Same as 'e' except it uses an upper case ‘E’ as the separator character.

# 'f': Fixed-point notation. Displays the number as a fixed-point number. The default precision is 6.

# 'F': Fixed-point notation. Same as 'f', but converts nan to NAN and inf to INF.

# 'g': General format. For a given precision p >= 1
#   , this rounds the number to p significant digits 
#   and then formats the result in either fixed-point format or in scientific notation
#   , depending on its magnitude.

# The precise rules are as follows: suppose that the result formatted with presentation type 'e' 
#   and precision p-1 would have exponent exp. 
#   Then if -4 <= exp < p, the number is formatted with presentation type 'f' and precision p-1-exp. 
#   Otherwise, the number is formatted with presentation type 'e' and precision p-1. 
#   In both cases insignificant trailing zeros are removed from the significand, 
#   and the decimal point is also removed if there are no remaining digits following it, 
#   unless the '#' option is used.

# Positive and negative infinity, positive and negative zero, and nans, 
#   are formatted as inf, -inf, 0, -0 and nan respectively, regardless of the precision.

# A precision of 0 is treated as equivalent to a precision of 1. The default precision is 6.

# 'G': General format. Same as 'g' except switches to 'E' if the number gets too large. 
# The representations of infinity and NaN are uppercased, too.

# 'n': Number. This is the same as 'g'
#   , except that it uses the current locale setting to insert the appropriate number separator characters.

# '%': Percentage. Multiplies the number by 100 and displays in fixed ('f') format
#   , followed by a percent sign.

# None: Similar to 'g', except that fixed-point notation, when used,
#   , has at least one digit past the decimal point. The default precision is as high as needed to represent the particular value. The overall effect is to match the output of str() as altered by the other format modifiers.

"{:e}".format(4200000)
# '4.200000e+06'
"{:E}".format(4200000)
# '4.200000E+06'

"{:f}".format(4200000)
# '4200000.000000'
"{:.3f}".format(4200000)
# '4200000.000'
"{:.3f}".format(0.0042)
# '0.004'
"{:.4f}".format(0.0042)
# '0.0042'

import numpy as np
"{:.4f}".format(np.inf)
# 'inf'
"{:.4F}".format(np.inf)
# 'INF'

"{:g}".format(0.00000042)
# '4.2e-07'
"{:g}".format(0.000042)
# '4.2e-05'
"{:g}".format(0.00042)
# '0.00042'
"{:g}".format(42)
# '42'
"{:g}".format(420000)
# '420000'
"{:g}".format(4200000)
# '4.2e+06'

"{:.2%}".format(0.042)
# '4.20%'
"{:.4%}".format(0.042)
# '4.2000%'


#%% 参数的嵌套写法Nesting arguments and more complex examples:
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
# left<<<<<<<<<<<<
# ^^^^^center^^^^^
# >>>>>>>>>>>right

octets = [192, 168, 0, 1]
'{:02X}{:02X}{:02X}{:02X}'.format(*octets)
# 'C0A80001'

width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
#     5     5     5   101 
#     6     6     6   110 
#     7     7     7   111 
#     8     8    10  1000 
#     9     9    11  1001 
#    10     A    12  1010 
#    11     B    13  1011 


# %% 格式化字符串字面值 formatted string literal
# #########################
arg='YH'
f'Hello {arg}'
# 'Hello YH'

def greet(name, question):
    return f'Hello {name}! how\'s it {question}'

greet('bob','going')
# "Hello bob! how's it going"

name = 'bob'
errno=1
f'Hey {name}, there\'s a {errno:#x} error!'
# "Hey bob, there's a 0x1 error!"


import dis
dis.dis(greet)
#   7           0 LOAD_CONST               1 ('Hello ')
#               2 LOAD_FAST                0 (name)
#               4 FORMAT_VALUE             0
#               6 LOAD_CONST               2 ("! how's it ")
#               8 LOAD_FAST                1 (question)
#              10 FORMAT_VALUE             0
#              12 BUILD_STRING             4
#              14 RETURN_VALUE
# %%
