from random import randint
import operator
import math
import os
from copy import deepcopy


def read_tokens():
    d = {}
    file_names = get_file_names()
    for i in range(0, len(file_names)):
        d[file_names[i]] = {}
    for i in range(0, len(file_names)):
        str_file = read_file(file_names[i])
        list_str = str_file.split(" ")
        for j in range(0, len(list_str)):
            token = list_str[j]
            if token == '':
                continue
            # print("token : ", token)
            if token in d[file_names[i]]:
                d[file_names[i]][token] += 1
            else:
                d[file_names[i]][token] = 1
    return d


def get_tokens():
    d = read_tokens()
    out = {}
    for i in d:
        out.update(d[i])
    for i in out:
        out[i] = 0
    return out


def log2(x):
    return math.log(x, 2.0)


def create_random_string(num=100):
    s = ""
    for i in range(0, num):
        s += chr(randint(65, 90)) + " "
    return s


def get_alphabet_dict():
    # d = {}
    # for i in range(65, 91):
    #     d[chr(i)] = 0
    # return d
    return get_tokens()


def create_files(num=1, path="files"):
    file_name = []
    for i in range(0, num):
        file_name.append(path + "/file" + str(i + 1) + ".txt")

    for i in range(0, len(file_name)):
        write_file(file_name[i], create_random_string(randint(1, 5)))
    return file_name


def get_file_names(path='files'):
    file_names = []
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):  # whatever file types you're using...
            file_names.append("files/" + filename)
    return file_names


# def read_tokens_file(string):
#     list_str = string.split(" ")
#     d = {}
#     for i in range(0, len(list_str)):
#         token = list_str[i]
#         if token in d:
#             d[token] += 1
#     return d


def read_files():
    file_names = get_file_names()
    string_file_dictionary = {}
    for i in range(0, len(file_names)):
        string_file_dictionary[format_filename(file_names[i])] = count_frequency(read_file(file_names[i]))

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
#


# def read_tokens():
#     file_names = get_file_names()
#     str_file = read_file(file_names[i])
#     list_str = string.split(" ")
#     d = {}
#     for i in range(0, len(list_str)):
#         token = list_str[i]
#         if token in d:
#             d[token] += 1
#     return d


# for i in range(0, len(file_names)):
#     read_tokens_file()
# return


def count_frequency(string):
    string = string.split(' ')
    d = get_alphabet_dict()
    for i in range(0, len(string)):
        char = string[i]
        if char in d:
            d[char] += 1
    return d


def divide_size_from_dic(dic, size):
    for i in dic:
        dic[i] = format_float(dic[i] / size)
        # dic[i] = dic[i] / size
    return dic


def size_of_char_file(file_path):
    return len(read_file(file_path).replace(" ", ""))


def read_file(file_path):
    file_str = open(file_path).read()
    return file_str


def write_file(file_path, string_input):
    # os.chdir(os.getcwd()+ "/files")
    # file = open(file_path, "w")
    file = open("" + file_path, "w", encoding='utf8')
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
    dict_input = get_alphabet_dict()
    input_str = input_str.split(" ")
    for i in range(0, len(input_str)):
        char = input_str[i].replace(" ", "")
        if char.isalpha() and char in dict_input:
            dict_input[char] += 1
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


def get_max_freq_in_dict(d):
    return max(d.items(), key=operator.itemgetter(1))[1] if d else 0


def calc_tf(file_dict):
    freq = get_max_freq_in_dict(file_dict)
    if freq == 0:
        return file_dict
    for i in file_dict:
        file_dict[i] = format_float(file_dict[i] / freq)
    return file_dict


def calc_tf_files(d):
    files_dict = deepcopy(d)
    for j in files_dict:
        files_dict[j] = calc_tf(files_dict[j])
    return files_dict


def calc_df_files(files_dict):
    alpha = get_alphabet_dict()
    for j in alpha:
        for i in files_dict:
            if files_dict[i][j] != 0:
                alpha[j] += 1
    return alpha


def calc_idf_files(df, n):
    for i in df:
        if df[i] == 0:
            df[i] = 0
        else:
            df[i] = log2(n / df[i])
    return df


def print_files_dictionary(d):
    for i in d:
        print(i, " : ", d[i])


def get_score_dict(files_dict):
    score = {}
    for i in files_dict:
        score[i] = 0
    return score


def tf_idf_files(tf_files, idf):
    w_dict = deepcopy(tf_files)
    for alpha in idf:
        for file in tf_files:
            w_dict[file][alpha] = tf_files[file][alpha] * idf[alpha]
    return w_dict


def square_dict(tf_idf_dict, query_dict):
    alpha = get_alphabet_dict()
    d = {}
    for j in tf_idf_dict:
        d[j] = 0
        d["query"] = 0
        for i in alpha:
            c = i
            d[j] += (tf_idf_dict[j][c]) ** 2
            d["query"] += (query_dict["query"][c]) ** 2
    return d


def similarity(tf_idf_dict, query_dict):
    alpha = get_alphabet_dict()
    score_dict = get_score_dict(tf_idf_dict)
    for i in alpha:
        c = i
        for j in tf_idf_dict:
            score_dict[j] += tf_idf_dict[j][c] * query_dict["query"][c]
    return score_dict


def cos_similarity(tf_idf_dict, query_dict):
    score_dict = get_score_dict(tf_idf_dict)
    sim = similarity(tf_idf_dict, query_dict)
    sq = square_dict(tf_idf_dict, query_dict)
    for i in score_dict:
        x = math.sqrt(sq["query"] * sq[i])
        if x == 0:
            score_dict[i] = 0
        else:
            score_dict[i] = format_float(sim[i] / x)
    return score_dict


def main_fun(input_str="B D", random_files=False):
    if random_files:
        create_return = create_files(10, 'files')
        print("Create Files return :-\n", create_return)
        del create_return
    input_dictionary = format_input(input_str)
    print("input_dictionary :- \n", input_dictionary)
    files_dictionary = read_files()
    files_dictionary["query"] = input_dictionary
    num_of_files = len(files_dictionary)
    print("files_dictionary :- \n", files_dictionary)
    print("=========================================================")
    tf_files = calc_tf_files(files_dictionary)
    print("tf_files :- \n", tf_files)
    print("=========================================================")
    print("files_dictionary :- \n", files_dictionary)
    print("=========================================================")
    idf = calc_idf_files(calc_df_files(files_dictionary), num_of_files)
    print("idf :- \n", idf)
    print("=========================================================")
    file_names = get_file_names()
    print("file_names :- ", file_names)
    print("=========================================================")
    tf_idf = tf_idf_files(tf_files, idf)
    query_tf_idf = {"query": tf_idf["query"]}
    del tf_idf["query"]
    print("tf-idf :-")
    print_files_dictionary(tf_idf)
    print("=========================================================")
    print(query_tf_idf)
    print("get_score_dict(tf_idf) :- \n", get_score_dict(tf_idf))
    print("square_dict :- \n", square_dict(tf_idf, query_tf_idf))
    print("=========================================================")
    print("similarity :- \n", similarity(tf_idf, query_tf_idf))
    print("=========================================================")
    cos_sim = cos_similarity(tf_idf, query_tf_idf)
    print("cos-similarity :- \n", cos_sim)
    print("=========================================================")
    sorted_score = sorted(cos_sim.items(), key=lambda kv: kv[1], reverse=True)
    print("In ", __name__, "Module .")
    print_score(sorted_score)
    dict_out = {}
    for i in sorted_score:
        dict_out[format_filename(i[0])] = [str(i[1]), read_file("files/" + i[0] + ".txt")]

    print("Return dict is :\n", dict_out)
    return dict_out


if __name__ == '__main__':
    main_fun()
