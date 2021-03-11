sharedPrime = 23
sharedBase = 5

azatSecret = 6
dimaSecret = 15


print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)

A = (sharedBase ** azatSecret) % sharedPrime
print("\n  Azat Sends Over Public Chanel: ", A)

B = (sharedBase ** dimaSecret) % sharedPrime


print("\n------------\n")
print("Privately Calculated Shared Secret:")
aliceSharedSecret = (B ** azatSecret) % sharedPrime
print("    Azat Shared Secret: ", aliceSharedSecret)

bobSharedSecret = (A ** dimaSecret) % sharedPrime
print("    Dima Shared Secret: ", bobSharedSecret)