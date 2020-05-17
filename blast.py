# -*- coding: utf-8 -*-
# 开发团队   ：边界漫游
# 开发人员   ：Akira
# 开发时间   ：2020/4/7  9:10
# 文件名称   ：blast.PY
# 开发工具   ：PyCharm

import zipfile
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Blast zip_file')
    parser.add_argument('-t', '--target', required=True, help='Please input the target......')
    parser.add_argument('-d', '--dict', required=True, help='Please input the dict......')
    parser.add_argument('-o', '--output', required=True, help='Please output the result......')
    return parser


def read_dict(filename):
    with open(filename, 'r')as fp:
        dicts = [pwd.strip() for pwd in fp.readlines()]
    return dicts


def blast(zip_file, pwd, outfile):
    zip_f = zipfile.ZipFile(zip_file)
    try:
        zip_f.extractall(path=outfile, pwd=pwd.encode())
        return pwd
    except Exception as e:
        print(f'error:{e}')


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    for password in read_dict(args.dict):
        result = blast(args.target, password, args.output)
        if result:
            print(f'[+] password is :{result}')
            break
    else:
        print(f'[-] not found password')
