#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    old_list = []
    new_list = []
    with open('/home/paulo/.bash_history', 'r') as f:
        old_list = f.readlines()

    old_list = old_list[::-1]
    i = 0
    while i < len(old_list):
        if old_list[i] not in new_list:
            new_list.append(old_list[i])
        i+=1

    new_list = new_list[::-1]
    new_list.insert(0, "history clean\n")
    with open('/home/paulo/.bash_history', 'w') as nf:
        for line in new_list:
            nf.write(line)

if __name__ == "__main__":
    main()
