def most_frequency(word1):
    freq_dict = {}
    for letter in word1:
        if freq_dict.get(str(letter)) == None:
            freq_dict[str(letter)] = str(1)
        else :
            freq_dict[str(letter)] = str(int(freq_dict[str(letter)]) + 1)


    sort_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for i in sort_dict:
        print(i[0], i [1])

word = input("Please enter a String : ")
most_frequency(word)
