from ldd_test import *

TEST_NUMBER = 0

def test0():
    global TEST_NUMBER

    TEST_NUMBER = 0

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 1

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 2

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 3

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 4

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 5

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 6

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 7

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 8

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 9

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 10

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test1():
    global TEST_NUMBER

    TEST_NUMBER = 11

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 12

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 13

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 14

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 15

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 16

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 17

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 18

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 19

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 20

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 21

    ldd = one_var_depth_2_ldd(X)
    cons = constraint("v1 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test2():
    global TEST_NUMBER

    TEST_NUMBER = 22

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 23

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 24

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 25

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 26

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 27

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 28

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 29

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 30

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 31

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 32

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test3():
    global TEST_NUMBER

    TEST_NUMBER = 33

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 34

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 35

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 36

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 37

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 38

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 39

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 40

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 41

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 42

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 43

    ldd = one_var_depth_2_ldd(Y)
    cons = constraint("v0 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test4():
    global TEST_NUMBER

    TEST_NUMBER = 44

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 45

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 46

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 47

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 48

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 49

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 50

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 51

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 52

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 53

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 54

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test5():
    global TEST_NUMBER

    TEST_NUMBER = 55

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 56

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 57

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 58

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 59

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 60

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 61

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 62

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 63

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 64

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 65

    ldd = two_var_depth_1_ldd()
    cons = constraint("v0 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test6():
    global TEST_NUMBER

    TEST_NUMBER = 66

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 67

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 68

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 69

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 70

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 71

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 72

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 73

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 74

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 75

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 76

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test7():
    global TEST_NUMBER

    TEST_NUMBER = 77

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 78

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 79

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 80

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 81

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 82

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 83

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 84

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 85

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 86

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 87

    ldd = two_var_depth_1_ldd()
    cons = constraint("v1 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test8():
    global TEST_NUMBER

    TEST_NUMBER = 88

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 89

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 90

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 91

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 92

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 93

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 94

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 95

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 96

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 97

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 98

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test9():
    global TEST_NUMBER

    TEST_NUMBER = 99

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 100

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 101

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 102

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 103

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 104

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 105

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 106

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 107

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 108

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 109

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v0 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test10():
    global TEST_NUMBER

    TEST_NUMBER = 110

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 111

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 112

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 113

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 114

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 115

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 116

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 117

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 118

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 119

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 120

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test11():
    global TEST_NUMBER

    TEST_NUMBER = 121

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 122

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 123

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 124

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 125

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 126

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 127

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 128

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 129

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 130

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 131

    ldd = two_var_depth_2_then_child_ldd()
    cons = constraint("v1 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test12():
    global TEST_NUMBER

    TEST_NUMBER = 132

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 133

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 134

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 135

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 136

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 137

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 138

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 139

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 140

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 141

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 142

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test13():
    global TEST_NUMBER

    TEST_NUMBER = 143

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 144

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 145

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 146

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 147

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 148

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 149

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 150

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 151

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 152

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 153

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v0 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test14():
    global TEST_NUMBER

    TEST_NUMBER = 154

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 155

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 156

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 157

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 158

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 159

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 160

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 161

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 162

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 163

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 164

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test15():
    global TEST_NUMBER

    TEST_NUMBER = 165

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 166

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 167

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 168

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 169

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 170

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 171

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 172

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 173

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 174

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 175

    ldd = two_var_depth_2_else_child_ldd()
    cons = constraint("v1 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test16():
    global TEST_NUMBER

    TEST_NUMBER = 176

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 177

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 178

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 179

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 180

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 181

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 182

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 183

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 184

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 185

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 186

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 >= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

def test17():
    global TEST_NUMBER

    TEST_NUMBER = 187

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 1")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 188

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 2")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 189

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 3")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 190

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 4")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 191

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 5")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 192

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 6")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 193

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 7")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 194

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 8")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 195

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 9")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 196

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 10")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

    TEST_NUMBER = 197

    ldd = one_var_depth_2_ldd()
    cons = constraint("v0 <= 11")
    test(x_range, y_range, ldd, cons, TEST_NUMBER)

test0()
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()