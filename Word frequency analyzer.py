'''26/10/2020'''
'''Done By Diaa Almughrabi'''

def read_file_to_freq_dict(filename):
    '''The function takes in the file that includes the text that wanted to be analyzed'''
    textfile = open(filename,'r')
    dictionary= {}
    for line in textfile:
        words= line.split()
        for word in words:
            if word in dictionary:
                dictionary[word] += 1
            else: 
                dictionary[word] = 1
    textfile.close()
    return dictionary

def number_of_words(words_in_dictionary):
    '''This function calculate how many words there are in total and how many different words there are in the text'''
    num_words= words_in_dictionary.values()
    keys= words_in_dictionary.keys()
    number_of_all_words= sum(num_words)
    number_of_different_words= len(keys)
    return number_of_all_words , number_of_different_words

def most_repeated_words(words_in_text, num_of_most_repeated_word):
    '''Here we claculate the most used words and the most used word'''
    items = words_in_text.items()
    listan1= []
    for x,y in items:
        listan1.append((y,x))
    listan= sorted(listan1)
    most_ten_repeated_words= listan[-10:]
    most_ten_repeated_words.reverse()
    if len(most_ten_repeated_words) < 10:
        most_ten_repeated_words= items
    most_repeated= listan[-1]
    most_repeated_word= most_repeated[1]
    procent_of_most_repeated_word= (100 * most_repeated[0])/ num_of_most_repeated_word
    if (100 * most_repeated[0])% num_of_most_repeated_word != 0:
        procent_of_most_repeated_word= format(procent_of_most_repeated_word, ".3")   
    return listan , most_repeated_word, most_ten_repeated_words ,procent_of_most_repeated_word

def average_frequency(all_words, different_words):
    '''A function for medium frequency'''
    average_freq= int(all_words / different_words)
    decimal = all_words % different_words 
    if decimal != 0 :
        average_freq = int (all_words/different_words) +1
    return average_freq

def medelordfrekvens_words(num_average, in_dictionary):
    '''Which words that are repeated as many times as medium frequency'''
    listan3= []
    for x,y in in_dictionary :
        if x == num_average:
            listan3.append(y)
    return listan3

def median(diect, reversed_list):
    '''This function count the median and the words that repates as many times as the median'''
    keys= diect.values()
    keys_sorted= list(keys)
    length_index= int(len(keys)/ 2)
    median_is= keys_sorted[length_index]
    if len(keys) % 2 == 0:
        median_is= int((keys_sorted[length_index] + keys_sorted[length_index-1])/2) + 1
    elif len(keys) == 1 :
        median_is = keys_sorted[0]
    listan4 = []
    for x,y in reversed_list:
        if x == median_is :
            listan4.append(y)
    return median_is , listan4

def create_file(num_of_words, num_of_different_words, value_of_most_repeated, medelfrequence_number, average_frequence_words, median_value, median_words, The_most_repeated_word,procetage_of_median, file_N):
    '''Here we create the text file to print in all the extracted results''' 
    if ".txt" in file_N :
        used_filename= file_N.replace(".txt", "_report.txt")
    else :
        used_filename = file_N + "report.txt"
    write_file= open(used_filename, "w")
    write_file.writelines(f"Filen {file_N}, innehåller {num_of_words} ord varav {num_of_different_words} är olika\n \n \nDe vanligaste orden är :\n \n")
    for elements in value_of_most_repeated:
        write_file.writelines(f"{elements[1]} förekommer {elements[0]}\n")
    write_file.writelines(f"\n Medelfrekvensen i texten är {medelfrequence_number}, och den frekvensen har orden :\n")
    nr_of_words = 0
    column = 5 
    for elem in average_frequence_words :
        if nr_of_words % column == 0 :
            write_file.write("\n")
        write_file.write(f'{elem:15}')
        nr_of_words +=1
    write_file.writelines(f"\n\n Medianordfrekvensen i texten är {median_value}, och den frekvensen har orden:\n\n")
    for words in median_words : 
        if nr_of_words % column == 0 :
            write_file.write("\n")
        write_file.write(f'{words:15}')
        nr_of_words += 1
    write_file.writelines( f"\n\nDet vanligaste ordet är {The_most_repeated_word}, och det utgör {procetage_of_median},% ,av hela texeten.")
    write_file.close()
    return 

def main():
    '''The main function'''
    filename = input("Please type the name of the textfile you want to analyse: ")
    dictionary= read_file_to_freq_dict(filename)
    number= number_of_words(dictionary)
    number_and_procentage_of_most_repeated= most_repeated_words(dictionary, number[0])
    average_frequency_ = average_frequency(number[0], number[1])
    medelfrequence_word= medelordfrekvens_words(average_frequency_, number_and_procentage_of_most_repeated[0])
    the_median= median(dictionary, number_and_procentage_of_most_repeated[0])
    create_file(number[0], number[1], number_and_procentage_of_most_repeated[2], average_frequency_, medelfrequence_word, the_median[0], the_median[1],number_and_procentage_of_most_repeated[1],number_and_procentage_of_most_repeated[3], filename)
    return 
if __name__ == '__main__' : 
    main()