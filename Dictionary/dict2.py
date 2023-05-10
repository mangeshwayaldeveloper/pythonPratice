file_counts={"JPEG":10,"txt":14,"PNG":12,"MP4":34}
print(file_counts)
print(file_counts["JPEG"])
print(file_counts["MP4"])

#check whether the fil exist or not
print("JPEG" in file_counts)
# we can add the values inside of the dictionary
file_counts["CSV"]=23
print("this is the new count of the dictionary",file_counts)

# deleting from the dictionary
del file_counts["txt"]
print(file_counts)