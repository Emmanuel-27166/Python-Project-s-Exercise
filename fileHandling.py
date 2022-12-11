
# =====EXAMPLE OF READ=============

test = open('fileHandlingOpen.txt', 'r')
print (test.read())


# =====EXAMPLE OF WRITE===========

# test1 = open('fileHandlingWrite.txt', 'w')
# test1.write('this is an example of wirite of files')

# ==============APPEND============
# test = open('fileHandlingWrite.txt ', 'a')
# test.write(' this is an example of wirite of files')
for ex in test:
    test.write(ex)
