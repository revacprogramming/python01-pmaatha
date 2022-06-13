# Strings

str="X-DSPAM-Confidence:0.8475"
X=str.find('0.8475')
Y=str[X+1:]
Z=float(Y)
print(Z)