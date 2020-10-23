a, b, c = input().split(" ")
MaiorAB = ((int(a)+int(b)+(abs(int(a)-int(b))))/2)
MaiorABC = ((int(MaiorAB)+int(c)+(abs(int(MaiorAB)-int(c))))/2)
print(int(MaiorABC), "eh o maior")
#bla