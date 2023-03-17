text = "AwsAAwwSSwaawss"
final_text = []

for i in range(len(text)):
    final_text.append(text[(i+1)*-1])
    
print("".join(final_text))
    