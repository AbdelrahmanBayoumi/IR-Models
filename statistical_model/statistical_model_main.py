from random import randint
import os


def create_random_string(num=100):
    s = ""
    for i in range(0, num):
        s += chr(randint(65, 90)) + " "
    return s


def create_files(num=1, path="files"):
    file_name = []
    for i in range(0, num):
        file_name.append(path + "/file" + str(i + 1) + ".txt")

    for i in range(0, len(file_name)):
        write_file(file_name[i], create_random_string(randint(1, 20)))
    return file_name


def get_file_names(path='files'):
    file_names = []
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):  # whatever file types you're using...
            file_names.append("files/" + filename)
    return file_names


def read_files():
    file_names = get_file_names()
    string_file_dictionary = {}
    for i in range(0, len(file_names)):
        string_file_dictionary[format_filename(file_names[i])] = read_file(file_names[i])
    return string_file_dictionary


# Console Input
# def input_from_user(input_dic=None):
#     # num = int(input("Enter Number of Char in Query :- "))
#     # input_dic = {"A": 0.2, "B": 0.9, "D": 0.8}
#     # for i in range(0, num):
#     #     c = input("Character : ")
#     #     n = input("value : ")
#     #     input_dic[c] = n
#     if input_dic is None:
#         input_dic = {"A": 0.2, "B": 0.9, "D": 0.8}
#     return input_dic


def count_frequency(string, dic):
    d = {}
    for i in dic:
        d[i] = 0
    for i in range(0, len(string)):
        char = string[i]
        if char in d:
            d[char] += 1
    return d


def divide_size_from_dic(dic, size):
    for i in dic:
        if size==0:
            dic[i]=0
        else:
            dic[i] = format_float(dic[i] / size)
        # dic[i] = dic[i] / size
    return dic


def size_of_char_file(file_path):
    return len(read_file(file_path).replace(" ", ""))


def read_file(file_path):
    file_str = open(file_path).read()
    return file_str


def write_file(file_path, string_input):
    file = open(file_path, "w")
    file.write(string_input)
    file.close()


def score(input_dict, file_dict):
    score_dict = 0
    for i in input_dict:
        score_dict += float(float(input_dict[i]) * float(file_dict[i]))
    return score_dict


def format_float(x):
    return round(x, 3)


def format_input(input_str):
    if input_str == "":
        return {}
    dict_input = {}
    input_str = input_str.split(";")
    for i in input_str:
        x = i.replace(" ", "").split(":")
        dict_input[x[0]] = x[1]
    return dict_input


def print_score(sorted_score):
    for y in range(0, len(sorted_score)):
        print(y + 1, "- ", sorted_score[y][0], " : ", sorted_score[y][1])
    print()
    return sorted_score


def format_filename(file_name=""):
    if file_name == "":
        print("Error in ", __name__, " -> format_filename() , Empty String ")
        return file_name
    file_name = file_name.replace(".txt", "")
    while '/' in file_name:
        file_name = file_name.replace(file_name[0:file_name.rindex('/') + 1], "")
    return file_name


def main_fun(input_str="A:0.2; B:0.9; D:0.8"):
    # create_files(3, 'files')
    input_dictionary = format_input(input_str)
    files_dictionary = read_files()
    file_names = get_file_names()
    num_of_files = len(files_dictionary)
    list_of_files = []
    unsorted_score = {}
    for i in range(0, num_of_files):
        file_name = file_names[i]
        list_of_files.append(divide_size_from_dic(
            count_frequency(files_dictionary[format_filename(file_name)].replace(" ", ""), input_dictionary)
            , size_of_char_file(file_name)))
        unsorted_score[file_name] = format_float(score(input_dictionary, list_of_files[i]))

    # sorted_score = collections.OrderedDict(unsorted_score, reverse=True)
    sorted_score = sorted(unsorted_score.items(), key=lambda kv: kv[1], reverse=True)

    print("In ", __name__, "Module .")
    print_score(sorted_score)

    dict_out = {}
    for i in sorted_score:
        dict_out[format_filename(i[0])] = [str(i[1]), read_file(i[0])]

    print("Return dict is :\n", dict_out)
    return dict_out


if __name__ == '__main__':
    main_fun()
